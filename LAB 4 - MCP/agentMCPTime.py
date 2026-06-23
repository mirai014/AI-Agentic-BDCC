import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_ollama import ChatOllama

async def main():
    # 1. Initialisation du client pour le serveur de temps via uvx
    client = MultiServerMCPClient(
        {
            "time": {
                "transport": "stdio",
                "command": "uvx",
                "args": [
                    "mcp-server-time",
                    "--local-timezone=America/New_York"
                ]
            }
        }
    )
    
    print("Connexion au serveur de temps MCP...")
    tools = await client.get_tools()
    
    # 2. Initialiser le modèle Ollama
    model = ChatOllama(
        model="llama3.2:3b",
        temperature=0
    )
    
    # 3. Création de l'agent
    agent = create_agent(
        model=model,
        tools=tools,
    )
    
    # 4. Question sur le fuseau horaire
    question = HumanMessage(content="What time is it in Japan?")
    
    print("L'agent cherche l'heure au Japon...")
    response = await agent.ainvoke(
        {"messages": [question]}
    )
    
    print("\nRéponse finale de l'agent :")
    print(response['messages'][-1].content)

if __name__ == "__main__":
    asyncio.run(main())