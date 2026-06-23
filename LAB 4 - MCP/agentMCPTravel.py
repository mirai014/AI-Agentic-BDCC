import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain_ollama import ChatOllama

async def main():
    # 1. Initialisation du client MCP distant
    client = MultiServerMCPClient(
        {
            "travel_server": {
                "transport": "streamable_http",
                "url": "https://mcp.kiwi.com"
            }
        }
    )
    
    print("1. Connexion au serveur MCP distant de Kiwi.com...")
    tools = await client.get_tools()
    print(f"   -> Outils récupérés avec succès !")
    
    # 2. Initialisation de Llama 3.2
    model = ChatOllama(
        model="llama3.2:3b",
        temperature=0
    )
    
    # 3. Création de l'agent (Correction du premier argument avec 'model')
    print("2. Initialisation de l'agent de voyage...")
    agent = create_agent(
        model,  # <-- CORRECTION ICI (On passe l'objet model, pas une string)
        tools=tools,
        checkpointer=InMemorySaver(),
        system_prompt="You are a travel agent. No follow up questions."
    )
    
    # 4. Question avec arguments explicites pour éviter les erreurs d'arguments
    config = {"configurable": {"thread_id": "1"}}
    question = HumanMessage(
        content=(
            "Give me direct flight from Rabat to Agadir. "
            "Use '25/08/2026' as departureDate and '30/08/2026' as returnDate. "
            "Set sort to 'price' and locale to 'en'."
        )
    )
    
    print("3. L'agent interroge l'API distante (cela peut prendre 10 à 20 secondes)...")
    response = await agent.ainvoke(
        {"messages": [question]},
        config=config
    )
   
 # 5. Affichage forcé du résultat
    print("\n================ RÉPONSE DE L'AGENT ================")
    print(response['messages'][-1].content)
    print("====================================================")

if __name__ == "__main__":
    asyncio.run(main())
