# TP : LangGraph Studio - Visualiser, Tester et Déboguer un Agent RAG

Ce projet est un guide d'exécution rapide pour le **TP 5** du Master BDCC, encadré par le Prof. RETAL SARA. Il permet de déployer un agent de recherche (RAG) local avec Ollama et de le visualiser graphiquement via LangGraph Studio

---

## 🛠️ Prérequis

Avant de commencer, assurez-vous d'avoir installé :
1. **Python** (version 3.10 ou supérieure)
2. **Ollama** avec le modèle téléchargé : `ollama run llama3.2:latest`
3. L'outil de gestion de packages **`uv`**

---

## 📂 Structure du Projet

Créez un dossier sur votre machine contenant les 3 fichiers suivants :

1. **`.env`** : Vos clés d'API (OpenAI, Groq, Tavily, LangSmith).
2. **`agent_simple.py`** : Le code source Python définissant l'agent et son outil `rag_search_opt`.
3. **`langgraph.json`** : Le fichier de configuration reliant votre code au runtime LangGraph.

### Configuration du fichier `langgraph.json`
```json
{
  "graphs": {
    "agent_simple": "./agent_simple.py:agent"
  },
  "env": "./.env",
  "source": {
    "kind": "uv",
    "root": "."
  }
}

http://googleusercontent.com/immersive_entry_chip/0
http://googleusercontent.com/immersive_entry_chip/1

---

## 💻 Utilisation dans LangGraph Studio

1. Une fois le serveur lancé, cliquez sur le lien généré dans votre terminal pour ouvrir l'interface **LangGraph Studio** sur LangSmith.
2. Vérifiez que le statut indique **`• Connected`**.
3. Dans la section **Input** (en bas à gauche), cliquez sur **`+ Message`**
4. Saisissez une question (ex: *"Qui est le personnage principal ?"*).
5. Cliquez sur **`Submit`** pour observer l'agent appeler l'outil et générer sa réponse en temps réel.