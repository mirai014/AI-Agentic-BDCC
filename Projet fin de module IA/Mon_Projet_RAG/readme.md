# 🤖 Agentic-RAG Helpdesk Informatique v1.0

# A propos
Ce projet implémente un système d'**Agentic-RAG (Retrieval-Augmented Generation)** dédié au support informatique de premier niveau (Helpdesk). Propulsé par **LangGraph**, **ChromaDB** et l'API **Groq (Llama 3.1)**, cet agent est capable de décider de manière autonome s'il doit consulter une base de connaissances locale avant de formuler un plan d'action précis pour l'utilisateur.

---

## 🚀 Fonctionnalités
* **Routage Dynamique :** L'agent analyse la question et appelle un outil de recherche si nécessaire.
* **Base Vectorielle Locale :** Indexation sémantique des procédures techniques avec `all-MiniLM-L6-v2` et ChromaDB.
* **Sécurité Anti-Boucle :** Contrôle strict de la récursion pour éviter l'épuisement des quotas d'API.
* **Réponses Concision-Focus :** Synthèse sous forme de fiches solutions prêtes à l'emploi.

---

## 🛠️ Architecture du Projet

* `base_helpdesk.txt` : Base de connaissances brute contenant les consignes et pannes.
* `etape1_base.py` : Script de segmentation, vectorisation et stockage dans ChromaDB.
* `etape2_outils.py` : Définition des outils LangChain intégrés à l'agent (`@tool`).
* `etape3_graphe.py` : Modélisation de la machine à états et du routage avec LangGraph.
* `lancement_test.py` : Interface utilisateur interactive dans le terminal.

---

## 📦 Installation et Lancement

### 1. Prérequis
Assurez-vous d'avoir Python 3.10+ installé. Installez ensuite les dépendances requises :

> pip install langchain langchain-groq langgraph langchain-community langchain-huggingface chromadb sentence-transformers

ou bien :
> pip install -r requirements.txt

### 2. Configuration de la clé API
Générez une clé API sur le tableau de bord Groq Cloud et configurez-la dans votre environnement ou directement au début du fichier etape3_graphe.py :


> os.environ["GROQ_API_KEY"] = "VOTRE_CLE_GROQ"

### 3. Exécution
# Étape 1 :
 Initialiser la base vectorielle (à ne faire qu'une seule fois ou en cas de modification de base_helpdesk.txt en supprimant le dossier chroma.db) :

> python etape1_base.py
# Étape 2 : 
Lancer l'agent interactif :

> python lancement_test.py
