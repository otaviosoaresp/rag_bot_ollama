import os

DATA_DIR = os.path.join(os.getcwd(), 'cerebro')

QDRANT_HOST = "localhost"
QDRANT_PORT = 6333
QDRANT_COLLECTION_NAME = "document_collection"

MODELS = {
    'primary_model': 'llama3.1:8b-instruct-q8_0',
    'secondary_model': 'mistral:latest',
}
