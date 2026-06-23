import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from dataclasses import dataclass
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime
from langchain.messages import HumanMessage

# --- PARTIE 1: Définir une classe de contexte structurée appelée ColourContext ---
@dataclass
class ColourContext:
    favourite_colour: str = "blue"
    least_favourite_colour: str = "yellow"

# Initialisation du modèle
model = ChatOllama(model="llama3.2:3b", temperature=0)

# --- PARTIE 2: Agent sans contexte --- 
agent_sans_outils = create_agent(model=model, context_schema=ColourContext)

print("--- PARTIE 2 : Agent sans outils d'accès au contexte ---")
response = agent_sans_outils.invoke(
    {"messages": [HumanMessage(content="What is my favourite colour?")]},
    context=ColourContext()
)
print(response['messages'][-1].content)


# --- PARTIE 3: Agent avec contexte (Outils d'accès) ---
@tool
def get_favourite_colour(runtime: ToolRuntime) -> str:
    """Get the favourite colour of the user"""
    return runtime.context.favourite_colour

@tool
def get_least_favourite_colour(runtime: ToolRuntime) -> str:
    """Get the least favourite colour of the user"""
    return runtime.context.least_favourite_colour

# Création de l'agent avec les outils appropriés
agent_avec_contexte = create_agent(
    model=model,
    tools=[get_favourite_colour, get_least_favourite_colour],
    context_schema=ColourContext
)

print("\n--- PARTIE 3 : Agent avec outils d'accès (Contexte par défaut) ---")
response = agent_avec_contexte.invoke(
    {"messages": [HumanMessage(content="What is my favourite colour?")]},
    context=ColourContext()
)
print(response['messages'][-1].content)


# --- PARTIE 4: Changement de contexte ---
print("\n--- PARTIE 4 : Changement dynamique de contexte ---")
response = agent_avec_contexte.invoke(
    {"messages": [HumanMessage(content="What is my favourite colour?")]},
    context=ColourContext(favourite_colour="green")
)
print(response['messages'][-1].content)