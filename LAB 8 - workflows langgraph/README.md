## 🛠️ Installation et Configuration : 
Préréquis : 
Assurez-vous d'avoir Python (version 3.12 ou supérieure) et uv installés sur votre machine.Initialisation de l'environnement.Activer l'environnement virtuel :
> .venv\\Scripts\\activate
# Installer les dépendances requises :
Les dépendances nécessaires au bon fonctionnement de l'ensemble des scripts de ce laboratoire sont :
> uv add langgraph langchain-core ipython
# 🚀 Détail des Parties & Commandes d'Exécution :
Tous les scripts s'exécutent via l'environnement actif avec la commande 
>uv run --active python <chemin_du_fichier>.
## PARTIE 1 : 
Nouveau projet Hello Graph (hello_graph.py)
# Concept : 
Initialisation d'un graphe d'état rudimentaire utilisant MessagesState, l'ajout d'un nœud unique (hello_node), et l'exécution via la méthode .invoke().
Commande : 
>uv run --active python hello_graph.py
## PARTIE 2 :
 Un Workflow avec deux étapes (workflows/two_step_workflow.py)
 # Concept : 
 Définition d'un état personnalisé via un TypedDict (topic, joke). Transmission séquentielle d'un nœud modificateur de sujet (refine_topic) vers un nœud générateur (write_joke).Commande :
 >uv run --active python workflows/two_step_workflow.py
## PARTIE 3 : 
Ajouter un Reducer (workflows/reducers_demo.py)
# Concept :
 Introduction des reducers avec Annotated[list[str], add]. Permet d'éviter que les nœuds successifs n'écrasent l'état précédent en fusionnant progressivement (accumulation) les logs dans une liste.
 Commande :
 >uv run --active python workflows/reducers_demo.py
## PARTIE 4 :
 Ajouter un état du graphe de type message (workflows/message_state.py)
 # Concept : 
 Gestion de l'état conversationnel (ChatState) combinant une liste de messages accumulés grâce au réducteur add et le suivi d'un compteur d'étapes (steps) pour suivre la progression au sein des nœuds d'écho.
 Commande :
 >uv run --active python workflows/message_state.py

## PARTIE 5 : 
Workflow conditionnel (workflows/conditional_workflow.py) 
# Concept :
 Utilisation de add_conditional_edges pour ajouter de l'intelligence et du dynamisme au workflow. Une fonction de routage (check_joke) analyse l'état pour décider s'il faut passer à un nœud d'amélioration (improve_joke) ou terminer immédiatement (END).
 Commande :
 >uv run --active python workflows/conditional_workflow.py

## PARTIE 6 : 
Workflow en boucle (workflows/workflow_loop.py)
# Concept : 
Mise en place d'une structure cyclique. Le nœud step incrémente une variable n et boucle sur lui-même via une condition d'arrêt (should_continue) jusqu'à ce que n = 5. En fin de cycle, l'architecture du graphe est exportée sous forme d'image PNG (graph2.png) à l'aide de Mermaid.
Commande :
>uv run --active python workflows/workflow_loop.py

📊 Technologies utilisées: 
* LangGraph 
* LangChain Core
* uv 
* IPython 
