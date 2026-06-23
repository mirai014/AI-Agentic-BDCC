
# PARTIE 1 : Définition des outils
from langchain.tools import tool, ToolRuntime

@tool
def read_email(runtime: ToolRuntime) -> str:
    """Read an email from the given address."""
    # take email from state
    return runtime.state["email"]

@tool
def send_email(body: str) -> str:
    """Send an email to the given address with the given subject and body."""
    # fake email sending
    return f"Email sent"

#PARTIE 2 : Création d’un agent HITL
#Ajouter l’agent

from langchain.agents import create_agent, AgentState
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain_ollama import ChatOllama
class EmailState(AgentState):
    email: str
agent = create_agent(
model="gpt-5-nano",
tools=[read_email, send_email],
state_schema=EmailState,
checkpointer=InMemorySaver(),
middleware=[
HumanInTheLoopMiddleware(
interrupt_on={
"read_email": False,
"send_email": True,
},
description_prefix="Tool execution requires approval",
),
],
)

#Tester l’agent
from langchain.messages import HumanMessage
config = {"configurable": {"thread_id": "1"}}
response = agent.invoke(
{
"messages": [HumanMessage(content="Veuillez lire mon e-mail et envoyer une réponse immédiatement. Envoyez la réponse maintenant dans le même fil de discussion.")],
"email": "Bonjour Sara, je vais être en retard pour notre réunion de demain. Pouvons-nous la reprogrammer ? Cordialement, Sofia"
},
config=config
)
print(response)

#Afficher le message interrompu avec metadata
print(response['__interrupt__'])

#Afficher seulement le message interrompu

print(response['__interrupt__'][0].value['action_re-quests'][0]['args']['body'])

#PARTIE 3 : Approuver le résultat
from langgraph.types import Command
response = agent.invoke(
Command(
resume={"decisions": [{"type": "approve"}]}
),
config=config # Le même thread ID pour reprendre la conversation
)
print(response['messages'][-1].content)

#PARTIE 4 : Refuser le résultat

response = agent.invoke(
Command(
resume={
"decisions": [
{
"type": "reject",
# Une explication sur les raisons du rejet
"message": " J’annule notre rendez-vous."
}
]
}
),
config=config # Le même thread ID pour reprendre la conversation
)
print(response)

#PARTIE 5 :Modifier le résultat

from langgraph.types import Command
response = agent.invoke(
Command(
resume={
"decisions": [
{
"type": "edit",
"edited_action": {
# Le nom du Tool.
"name": "send_email",
# Les arguments à passer au tool.
"args": {"body": "Je suis désolée mais je dois annuler notre rendez-vous je ne serais pas libre. Sara"},

}
}
]
}
),
config=config # Le même thread ID pour reprendre la conversation
)
print(response['messages'][-1].content)