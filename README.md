
# Retrieval-Augmented Generation (RAG) Chatbot Project

This project implements a chatbot using **Retrieval-Augmented Generation (RAG)** techniques, capable of answering questions based on documents loaded from a specific folder (e.g., `/cerebro`). The chatbot uses a local language model via **Ollama** and vector search through **Qdrant** to find and return relevant responses from text, PDF, CSV, and XLSX files.

## Features

- Document ingestion from the `/cerebro` folder containing `.txt`, `.pdf`, `.csv`, and `.xlsx` files.
- Indexing of documents into the **Qdrant** vector database.
- Response generation using **local language models** with **Ollama API**.
- Search and retrieve relevant information based on questions.
- Supports multiple language models such as `llama3.1:8b-instruct-q8_0`, `codellama`, and others.

---

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Project Setup](#project-setup)
4. [Running the Chatbot](#running-the-chatbot)
5. [Fine-tuning the Model](#fine-tuning-the-model)
6. [Troubleshooting](#troubleshooting)

---

## Requirements

- **Python 3.10+**
- **Qdrant** running locally or via Docker
- **Ollama API** installed and configured with local models available
- Libraries for handling various document types (e.g., `pdfplumber`, `openpyxl`)
  
Make sure you have sufficient hardware resources if working with large models such as `llama` or `codellama`.

---

## Installation

### 1. Clone the repository

First, clone this repository to your local machine:

```bash
git clone git@github.com:otaviosoaresp/rag_bot_ollama.git
cd rag_bot_ollama
```

### 2. Create a virtual environment

Create and activate a virtual environment to manage dependencies:

```bash
# For Linux/macOS
python3 -m venv .venv
source .venv/bin/activate

# For Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install the required dependencies

Install the required Python libraries from `requirements.txt`:

```bash
pip install -r requirements.txt
```

In case you encounter errors with `grpcio-tools`, use the following command:

```bash
pip install grpcio-tools --no-binary=grpcio-tools
```

Make sure all dependencies like `qdrant-client`, `ollama-api`, `pdfplumber`, `sentence-transformers`, and `openpyxl` are installed correctly.

### 4. Set up Qdrant

Ensure **Qdrant** is running locally. If you don’t have it installed, you can quickly run it using Docker:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

This will start Qdrant and make it accessible at `http://localhost:6333`.

---

## Project Setup

### 1. Configure the Models

Ensure the models you plan to use are available locally and configured in the `config.py` file. For example, to use `llama3.1:8b-instruct-q8_0`, ensure that the configuration looks like this:

```python
MODELS = {
    "primary_model": "llama3.1:8b-instruct-q8_0",
    "embedding_model": "nomic-embed-text:latest"
}
```

### 2. Data Loading

Place the files (e.g., `.txt`, `.pdf`, `.csv`, `.xlsx`) you want to load into the folder `/cerebro`. The project will read all files from this directory, process them, and index the contents into Qdrant for vector search.

---

## Running the Chatbot

1. **Run the Main Script**:
   After everything is set up, you can run the chatbot with:

   ```bash
   python main.py
   ```

   This script will:
   - Load the specified model (e.g., `llama3.1:8b-instruct-q8_0`).
   - Process the documents in `/cerebro` and index them into Qdrant.
   - Allow the user to input questions via the console.

2. **Example**:
   ```plaintext
   Loading language model and embedding model...
   Loading model: llama3.1:8b-instruct-q8_0
   Processing documents and indexing into Qdrant...
   Documents loaded: 3 documents.

   Enter your question (or 'exit' to stop): What is rural credit?
   Processing the question: What is rural credit?
   Chatbot Response: Rural credit is a form of financing aimed at supporting agricultural production through credit for investment, working capital, and other agricultural operations.
   ```

3. **Exit**:
   To exit, type `'exit'` in the prompt.

---

## Troubleshooting

### Common Issues and Fixes

#### 1. **`grpcio-tools` installation issues**:
   - Use the following command to avoid issues:
     ```bash
     pip install grpcio-tools --no-binary=grpcio-tools
     ```

#### 2. **Missing Models**:
   - Ensure the model names in `config.py` match the ones you have installed locally.

#### 3. **Qdrant 404 or 400 errors**:
   - If you receive an error like `404 Not Found: Collection doesn't exist!`, ensure that your documents are correctly indexed, and Qdrant is running.

#### 4. **No or Inaccurate Responses**:
   - Make sure the documents were processed and indexed correctly.
   - Verify that the model and Qdrant are properly configured.




---

