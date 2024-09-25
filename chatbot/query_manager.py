from data_loader.qdrant_manager import search_documents
from models.model_loader import ask_ollama


def handle_query(query, model_name, client, embedder):
    query_embedding = embedder.encode(query).tolist()

    search_results = search_documents(client, query_embedding)

    context = " ".join([result.payload["text"] for result in search_results])

    return ask_ollama(query, context, model_name)
