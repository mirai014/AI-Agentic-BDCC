import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from langchain.agents import AgentState, create_agent
from langchain.messages import HumanMessage, ToolMessage
from langchain.tools import tool, ToolRuntime
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

# --- PARTIE 5: Définir un état personnalisé d'agent en héritant de AgentState ---
class CustomState(AgentState):
    favourite_colour: str

# Initialisation du modèle
model = ChatOllama(model="llama3.2:3b", temperature=0)

# --- PARTIE 6: Agent qui modifie un état ---
@tool
def update_favourite_colour(favourite_colour: str, runtime: ToolRuntime) -> Command:
    """Update the favourite colour of the user in the state once they've revealed it."""
    return Command(
        update={
            "favourite_colour": favourite_colour,
            "messages": [
                ToolMessage(
                    "Successfully updated favourite colour", 
                    tool_call_id=runtime.tool_call_id
                )
            ]
        }
    )

# --- PARTIE 6 (Suite): Agent qui récupère un état ---
@tool
def read_favourite_colour(runtime: ToolRuntime) -> str:
    """Read the favourite colour of the user from the state."""
    try:
        return runtime.state["favourite_colour"]
    except KeyError:
        return "No favourite colour found in state"

# Assemblage de l'agent avec sa mémoire (InMemorySaver)
agent = create_agent(
    model=model,
    tools=[update_favourite_colour, read_favourite_colour],
    checkpointer=InMemorySaver(),
    state_schema=CustomState
)

# Configuration de la session (Thread 1)
config = {"configurable": {"thread_id": "1"}}

# 1. On informe l'agent (Déclenche la modification de l'état)
print("--- PARTIE 6 : Modification de l'état (Sauvegarde de la couleur) ---")
response = agent.invoke(
    {"messages": [HumanMessage(content="My favourite colour is green")]},
    config
)
print(response['messages'][-1].content)

# 2. On demande à l'agent de s'en souvenir (Lecture de l'état sauvegardé)
print("\n--- PARTIE 6 : Récupération de l'état persistant ---")
response = agent.invoke(
    {"messages": [HumanMessage(content="What's my favourite colour?")]},
    config
)
print(response['messages'][-1].content)