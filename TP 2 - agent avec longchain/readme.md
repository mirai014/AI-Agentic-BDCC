# TP : Agent Chef Personnel 
Projet réalisé dans le cadre du Master BDCC pour la Prof. RETAL SARA

# Objectif
Créer un agent intelligent avec LangChain capable de :
* Mémoriser les préférences de l'utilisateur (Mémoire)
* Utiliser la recherche internet pour trouver des recettes (Web Search Tool)
* S'adapter aux ingrédients disponibles dans le frigo

#Installation rapide
1. Installez les bibliothèques nécessaires :
 bash pip install langchain langchain-ollama langchain-community tavily-python langgraph python-dotenv

2.Créez un fichier .env avec votre clé Tavily :

Extrait de code :

TAVILY_API_KEY=votre_cle_ici

Lancez le projet :

Bash python chef_agent.py