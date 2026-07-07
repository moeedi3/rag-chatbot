import faiss
import numpy as np

EMBEDDING_DIM = 384


def create_index(vectors):

    if len(vectors) == 0:
        return faiss.IndexFlatL2(EMBEDDING_DIM)

    vectors = np.asarray(vectors).astype("float32")

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
