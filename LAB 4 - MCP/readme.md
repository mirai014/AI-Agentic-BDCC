# LAB 4 : Model Context Protocol (MCP)

Ce projet implémente les concepts du protocole **MCP (Model Context Protocol)** développé par Anthropic. L'objectif est de connecter un agent LLM local (**Llama 3.2** via Ollama) à différents serveurs MCP afin de récupérer dynamiquement des outils (tools), des ressources et des prompts système.
## Prérequis et Installation

### 1. Modèle LLM (Ollama)
Lancez Ollama en arrière-plan et téléchargez le modèle :

> ollama run llama3.2:3b

(Tapez /exit pour quitter le chat, le service reste actif).

2. Environnement virtuel & Dépendances
Créez l'environnement avec uv et installez tous les packages requis pour les 3 parties du TP :

# Créer l'environnement virtuel local
> uv venv

# Installer l'ensemble des bibliothèques nécessaires
uv pip install langchain langchain-ollama langchain-mcp-adapters langgraph python-dotenv mcp fastmcp tavily-python

# Exécution des Exercices
Partie 1 : Serveur MCP Local (Tavily Search)

> uv run --active python agentMCP.py

Partie 2 : Serveur de Temps (uvx)

> uv run --active python agentMCPTime.py

Partie 3 : Serveur Distant (Kiwi.com Travel Agent)

> uv run --active python agentMCPTravel.py