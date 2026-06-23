import asyncio
import sys
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_ollama import ChatOllama

async def main():
    # 1. Initialisation du client MCP
    client = MultiServerMCPClient(
        {
            "local_server": {
                "transport": "stdio",
                "command": "python",
                "args": ["resources/mcp_local_server.py"],
            }
        }
    )
    
    # 2. Récupération dynamique des outils, ressources et prompts du serveur
    tools = await client.get_tools()
    resources = await client.get_resources("local_server")
    
    prompt_data = await client.get_prompt("local_server", "prompt") 
    system_prompt = prompt_data[0].content
    
    # 3. Initialisation du modèle Ollama (Llama 3.2)
    model = ChatOllama(
        model="llama3.2:3b",
        temperature=0 
    )
    
    # 4. Création de l'agent modulaire avec les éléments du serveur MCP
    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt 
    )
    
    # 5. Exécution de l'agent avec une question
    config = {"configurable": {"thread_id": "1"}} 
    response = await agent.ainvoke(
        {"messages": [HumanMessage(content="Tell me about the langchain-mcp-adapters library")]},
        config=config 
    )
    
    print(response)

# Lancement de la fonction principale asynchrone
if __name__ == "__main__":
    asyncio.run(main())