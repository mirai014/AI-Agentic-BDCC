import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.tools import tool

# 1. Configurer la connexion avec notre base de données créée à l'étape 1
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
base_vectorielle = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
retriever = base_vectorielle.as_retriever(search_kwargs={"k": 2}) # Récupère les 2 meilleurs morceaux

# 2. Définition de l'outil de recherche pour l'agent
@tool
def chercher_dans_base_helpdesk(requete: str) -> str:
    """Consulte la base de connaissances Helpdesk pour trouver des solutions 
    aux pannes (Réseau, Connexion, Imprimante, Active Directory, Comptes verrouillés)."""
    
    docs = retriever.invoke(requete)
    
    # Rassembler les morceaux trouvés en un seul texte
    resultat = "\n\n".join([d.page_content for d in docs])
    return resultat

# Liste des outils officiels que l'agent pourra utiliser
liste_outils = [chercher_dans_base_helpdesk]