import os
import pdfplumber
import pandas as pd


def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        return " ".join([page.extract_text() for page in pdf.pages])


def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def extract_text_from_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_string()


def extract_text_from_xlsx(file_path):
    df = pd.read_excel(file_path)
    return df.to_string()


def process_files(data_dir):
    documents = []
    for filename in os.listdir(data_dir):
        file_path = os.path.join(data_dir, filename)
        if filename.endswith(".pdf"):
            documents.append(extract_text_from_pdf(file_path))
        elif filename.endswith(".txt"):
            documents.append(extract_text_from_txt(file_path))
        elif filename.endswith(".csv"):
            documents.append(extract_text_from_csv(file_path))
        elif filename.endswith(".xlsx"):
            documents.append(extract_text_from_xlsx(file_path))
    return documents
