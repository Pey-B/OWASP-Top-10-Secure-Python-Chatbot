from sentence_transformers import SentenceTransformer
from app.kb_loader import load_documents

model = SentenceTransformer("all-MiniLM-L6-v2")

documents, index = load_documents()

def search_kb(query: str, top_k: int = 2):
    if not documents or index is None:
        return []

    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_k)

    results = []
    for idx in indices[0]:
        if idx < len(documents):
            results.append(documents[idx])

    return results

