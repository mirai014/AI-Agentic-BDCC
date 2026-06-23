import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain.tools import tool
from typing import Dict, Any
from tavily import TavilyClient
from langgraph.checkpoint.memory import InMemorySaver

# Charger la clé API Tavily depuis le fichier .env
load_dotenv()

# 1. Initialiser le modèle local Ollama
model = ChatOllama(
    model="llama3.2:3b", 
    temperature=0.7     
)

# 2. Création de l'outil de recherche Web (Web Search Tool)
tavily_client = TavilyClient()

@tool
def web_search(query: str) -> Dict[str, Any]:
    """Recherche des recettes de cuisine ou des associations d'ingrédients sur internet."""
    return tavily_client.search(query)

# 3. Définition du comportement global de l'agent (System Message)
chef_prompt = (
    "Vous êtes un Chef Cuisinier Personnel étoilé. Votre rôle est d'aider l'utilisateur "
    "à concevoir des repas en fonction des ingrédients disponibles dans son réfrigérateur.\n\n"
    "Consignes :\n"
    "- Proposez des recettes adaptées aux ingrédients fournis.\n"
    "- Utilisez l'outil de recherche web si nécessaire pour compléter vos connaissances.\n"
    "- Prenez TOUJOURS en compte les préférences enregistrées dans la mémoire (allergies, régimes)."
)

# 4. Assemblage de l'agent avec sa Mémoire et son Outil
memory_saver = InMemorySaver()

chef_agent = create_agent(
    model=model,
    tools=[web_search],        # Intégration du Web Search Tool
    system_prompt=chef_prompt, # Intégration du rôle de Chef
    checkpointer=memory_saver  # Intégration de la mémoire
)

# ==========================================
# SCÉNARIO DE TEST (Simulation de dialogue)
# ==========================================

# Identifiant unique pour la session de discussion (Thread)
config = {"configurable": {"thread_id": "session_cuisine_1"}}

print("--- Début de la discussion avec le Chef ---\n")

# Étape A : Donner une préférence (Test de la mémoire)
print("-> Envoi du message de profil...")
msg1 = HumanMessage(content="Bonjour Chef ! Je suis végétarien.")
response1 = chef_agent.invoke({"messages": [msg1]}, config) 
print(f"Chef : {response1['messages'][-1].content}\n") 

# Étape B : Demander un plat avec des ingrédients (Doit se souvenir qu'on est végétarien)
print("-> Demande de recette avec le frigo...")
msg2 = HumanMessage(content="Qu'est-ce que je peux cuisiner avec : des tomates, des pâtes et du fromage ?")
response2 = chef_agent.invoke({"messages": [msg2]}, config)
print(f"Chef : {response2['messages'][-1].content}\n") 