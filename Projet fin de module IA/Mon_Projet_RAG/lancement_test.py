import os
from langchain_core.messages import HumanMessage
from etape3_graphe import app_graphe

def lancer_chat_interactif():
    print("========================================================")
    # RAG Agent informatique en Master Big Data
    print("🤖 BIENVENUE SUR VOTRE AGENT AGENTIC-RAG HELPDESK v1.0")
    print("========================================================")
    print("👉 Tapez votre question de panne (Réseau, Imprimante, AD...)")
    print("👉 Tapez 'quitter' pour fermer le programme.\n")

    while True:
        # Attendre que tu tapes une question dans le terminal
        question = input("\n👤 Vous : ")
        
        if question.lower() == 'quitter':
            print("Fermeture de l'agent. Merci !")
            break
            
        if not question.strip():
            continue

        print("\n⚙️  [L'Agent analyse et consulte le graphe LangGraph...]")
        
        # Initialiser l'état avec la question
        inputs = {"messages": [HumanMessage(content=question)]}
        
        # Exécuter le graphe
        try:
            for historique in app_graphe.stream(inputs, config={"recursion_limit": 5}, stream_mode="values"):
                dernier_message = historique["messages"][-1]
            
            print("\n🤖 Agent Helpdesk :")
            print(dernier_message.content)
            print("\n--------------------------------------------------------")
            
        except Exception as e:
            print(f"\n❌ Une erreur est survenue : {e}")

if __name__ == "__main__":
    lancer_chat_interactif()