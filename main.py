from models.model_loader import load_model
from data_loader.file_processor import process_files
from data_loader.qdrant_manager import connect_qdrant, index_documents
from chatbot.query_manager import handle_query
from sentence_transformers import SentenceTransformer
import config


def main():
    print("Loading language model and embedding model...")
    model_name = load_model(config.MODELS['primary_model'])
    embedder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    print("Processing documents and indexing in Qdrant...")
    documents = process_files(config.DATA_DIR)

    if not documents:
        print("No documents were loaded. Check the /cerebro folder.")
        return

    print(f"Documents loaded: {len(documents)} documents")

    client = connect_qdrant()
    index_documents(client, documents, embedder)
    print("Documents processed and indexed successfully!")

    print("Entering chatbot interaction loop...")
    while True:
        query = input("\nType your question (or 'exit' to quit): ")

        if query.lower() == 'sair':
            print("Shutting down the chatbot...")
            break

        print(f"Processing the question: {query}")
        response = handle_query(query, model_name, client, embedder)
        print(f"\nChatbot Response: {response}")


if __name__ == "__main__":
    main()
