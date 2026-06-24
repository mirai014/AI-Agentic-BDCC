import os
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage
from langchain_groq import ChatGroq
from langgraph.graph import END, StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

# 1. Configuration de la clé API Groq
os.environ["GROQ_API_KEY"] = "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"

# Importer les outils créés à l'étape 2
from etape2_outils import liste_outils

# 2. Définition du State (Mémoire du graphe)
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

# 3. Initialisation du modèle (Version 8B Instant pour éviter l'expiration des quotas 429)
llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0.1)
llm_avec_outils = llm.bind_tools(liste_outils)

# 4. Définition du Nœud Agent (Modifié pour forcer la réponse finale)
def noeud_agent(state: AgentState):
    messages = state["messages"]
    
    # Si le dernier message vient de l'outil (ToolMessage), on force le LLM à rédiger la synthèse
    if messages and hasattr(messages[-1], 'content') and messages[-1].type == "tool":
        contexte_base = messages[-1].content
        question_utilisateur = messages[0].content
        
        prompt_synthese = (
            "Voici les instructions issues de la base de connaissances Helpdesk :\n"
            f"{contexte_base}\n\n"
            f"Rédige une réponse claire et structurée à l'utilisateur pour résoudre son problème : '{question_utilisateur}'"
        )
        reponse = llm.invoke([{"role": "user", "content": prompt_synthese}])
        return {"messages": [reponse]}
        
    # Sinon (premier passage), le LLM appelle l'outil normalement
    reponse = llm_avec_outils.invoke(messages)
    return {"messages": [reponse]}

# 5. Logique de routage forcée pour la démonstration (Anti-boucle garantie)
def continuer_ou_arreter(state: AgentState):
    messages = state["messages"]
    dernier_message = messages[-1]
    
    # Compter combien de messages d'outils (ToolMessage) ou d'appels sont présents
    nb_messages = len(messages)
    
    # Si on a déjà fait une recherche (historique contient plus de 2 messages), on s'arrête direct !
    if nb_messages >= 3:
        print("-> L'agent a récupéré les données de la base. Fin du graphe.")
        return "fin"
        
    # Si le LLM demande un outil pour la première fois, on l'exécute
    if dernier_message.tool_calls:
        nom_outil = dernier_message.tool_calls[0]['name']
        print(f"-> L'agent décide d'appeler l'outil : {nom_outil}")
        return "action"
    
    # Sinon, fin par défaut
    print("-> L'agent répond directement. Fin du graphe.")
    return "fin"

# 6. Construction du Graphe
workflow = StateGraph(AgentState)

# Ajouter les nœuds fonctionnels
workflow.add_node("technicien_agent", noeud_agent)
workflow.add_node("outils_action", ToolNode(liste_outils))

# Définir les connexions et points de départ
workflow.add_edge(START, "technicien_agent")

# Ajouter les liaisons conditionnelles (Routage valide)
workflow.add_conditional_edges(
    "technicien_agent",
    continuer_ou_arreter,
    {
        "action": "outils_action",
        "fin": END
    }
)

# Boucle : Toujours revenir à l'agent après l'action de l'outil
workflow.add_edge("outils_action", "technicien_agent")

# Compiler le graphe
app_graphe = workflow.compile()
print("Graphe LangGraph compilé avec succès et prêt à l'emploi !")