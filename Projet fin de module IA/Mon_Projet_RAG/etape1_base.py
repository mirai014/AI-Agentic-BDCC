import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def preparer_base_documentaire():
    print("Début du traitement de la base helpdesk...")
    
    # 1. Charger le fichier texte
    loader = TextLoader("base_helpdesk.txt", encoding="utf-8")
    documents = loader.load()
    
    # 2. Découper le texte en morceaux (chunks)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300, 
        chunk_overlap=50
    )
    docs_decoupes = text_splitter.split_documents(documents)
    print(f"Texte découpé en {len(docs_decoupes)} morceaux.")
    
    # 3. Utiliser un modèle d'embedding gratuit (HuggingFace)
    print("Chargement du modèle d'embedding gratuit...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # 4. Créer la base vectorielle locale Chroma
    print("Création de la base de données locale 'chroma_db'...")
    Chroma.from_documents(
        documents=docs_decoupes, 
        embedding=embeddings, 
        persist_directory="./chroma_db"
    )
    
    print("\nFélicitations ! La base 'chroma_db' est prête. (2 points acquis !) [cite: 33]")

if __name__ == "__main__":
    preparer_base_documentaire()