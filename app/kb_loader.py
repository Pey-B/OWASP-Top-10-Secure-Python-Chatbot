from sentence_transformers import SentenceTransformer
import faiss
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

def load_documents():
    kb_path = "app/kb/clinic_info.txt"

    if not os.path.exists(kb_path):
        return [], None

    with open(kb_path, "r", encoding="utf-8") as f:
        documents = [line.strip() for line in f if line.strip()]

    embeddings = model.encode(documents)
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return documents, index

