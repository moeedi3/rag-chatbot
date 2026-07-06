import faiss
import numpy as np


def create_index(vectors):

    vectors = np.array(vectors, dtype="float32")

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(vectors)

    return index


def save_index(index):

    print("SAVING NEW FAISS INDEX")

    faiss.write_index(index, "storage/index.faiss")


def load_index():

    print("LOADING FAISS INDEX")

    return faiss.read_index("storage/index.faiss")
