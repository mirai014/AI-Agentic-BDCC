### LAB 9 : Agent avec LangGraph
# 🎯 Objectif
Construire un agent conversationnel autonome capable d'exécuter des outils arithmétiques, d'intégrer une validation humaine (HITL), et de manipuler l'historique des états (Time Travel / Forking).

# 📂 Structure du Projet
tools_setup.py : Configuration du LLM local (Ollama llama3.2:3b) et des outils (add, multiply, divide).

agent_node.py : Agent basique en boucle fermée avec streaming.

hitl_workflow.py : Introduction de la validation humaine via interrupt().

tp_advanced_agent.py : Agent complet combinant outils, validation, historique et forking.

# 🚀 Commandes de Test
1. Prérequis
Lancez votre LLM local dans un terminal :


>ollama run llama3.2:3b

2. Exécution des parties
Exécutez chaque script pour valider les étapes du TP :


# Partie 2 : Tester l'agent autonome et le streaming
>uv run python agent_node.py

# Partie 3 : Tester le workflow HITL basique
>uv run python hitl_workflow.py

# Partie 4 : Tester l'agent complet (Interruption, Rejet et Voyage dans le temps)
>uv run python tp_advanced_agent.py

# 💡 Concepts Clés Validés
Outils autonomes : Le LLM choisit et appelle le bon outil selon le besoin.

Human-In-The-Loop (HITL) : Le graphe se met en pause via interrupt(), attend un signal humain (Command(resume=...)), puis bifurque ou continue.

Time Travel (Forking) : Récupération d'un état passé dans l'historique (get_state_history) pour modifier les variables et relancer une exécution alternative.