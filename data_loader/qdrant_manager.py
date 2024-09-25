from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, SearchRequest


def connect_qdrant():
    client = QdrantClient(host="localhost", port=6333)
    return client


def create_collection(client, collection_name, vector_size):
    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=vector_size, distance="Cosine")
    )


def index_documents(client, documents, embedder):
    vector_size = 384  # Ajuste conforme o tamanho do embedding
    create_collection(client, "document_collection", vector_size)

    points = [
        PointStruct(id=i, vector=embedder.encode(document).tolist(), payload={"text": document})
        for i, document in enumerate(documents) if document.strip()  # Ignorar documentos vazios
    ]

    if not points:
        print("Nenhum ponto foi gerado para indexação. Verifique os documentos.")
        return

    client.upsert(collection_name="document_collection", points=points)


def search_documents(client, query_embedding, top_k=3):
    search_result = client.search(
        collection_name="document_collection",
        query_vector=query_embedding,
        limit=top_k
    )
    return search_result

