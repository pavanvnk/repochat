import os
import shutil
import streamlit as st
# Old import (deprecated)
# from langchain.vectorstores import Chroma
# New import (recommended)
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import NotebookLoader, TextLoader

from langchain_community.vectorstores import Chroma

def vector_db(embeddings, code):
    collection_name = "db_collection"
    local_directory = "db_" + st.session_state["db_name"]
    persist_directory = os.path.join(os.getcwd(), local_directory)
    
    if os.path.exists(persist_directory):
        shutil.rmtree(persist_directory)

    vec_db = Chroma.from_documents(
        documents=code,
        embedding=embeddings,
        collection_name=collection_name,
        persist_directory=persist_directory
    )

    vec_db.persist()

    return vec_db

def load_to_db(repo_path):
    docs = []
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for filename in files:
            if filename.startswith('.'):
                continue
            if filename == 'package-lock.json':
                continue
            file_path = os.path.join(root, filename)
            try:
                if file_path.endswith('.ipynb'):
                    loader = NotebookLoader(file_path)
                else:
                    loader = TextLoader(file_path, encoding="utf-8")
                    docs.extend(loader.load_and_split())
            except Exception as e:
                pass
            
    code_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    code = code_splitter.split_documents(docs)
    return code
