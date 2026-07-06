from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
import shutil
import os

from app.services.chat_service import ask_question
from app.services.document_service import (
    process_document,
    get_documents,
    delete_document,
)

router = APIRouter()


# ==========================
# Request Models
# ==========================


class ChatRequest(BaseModel):
    question: str


# ==========================
# Chat Endpoint
# ==========================


@router.post("/chat")
def chat(request: ChatRequest):

    result = ask_question(request.question)

    return result


# ==========================
# Upload Document
# ==========================


@router.post("/documents/upload")
def upload(file: UploadFile = File(...)):

    os.makedirs("data/pdfs", exist_ok=True)

    file_path = f"data/pdfs/{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    process_document(file_path, file.filename)

    return {"message": "Document uploaded successfully"}


# ==========================
# List Documents
# ==========================


@router.get("/documents")
def list_documents():

    documents = get_documents()

    return documents


# ==========================
# Delete Document
# ==========================


@router.delete("/documents/{document_id}")
def remove_document(document_id: int):

    deleted = delete_document(document_id)

    if not deleted:

        raise HTTPException(status_code=404, detail="Document not found.")

    return {"message": "Document deleted successfully."}
