🛠️ Installation et Préparation
1. Prérequis
Assurez-vous d'avoir Python 3.10 ou supérieur installé sur votre machine.

2. Installation des dépendances
Ouvrez votre invite de commandes (CMD) ou votre terminal dans le dossier du projet et exécutez la commande suivante :


> pip install langchain langchain-core langgraph langchain-ollama

🚀 Utilisation et Tests
Le script principal test_hitl.py simule le cycle de vie complet de l'agent face à un e-mail reçu de Sofia concernant le report d'une réunion.

Pour lancer le test, exécutez simplement :

> python hitl.py


Approuver (Partie 3) : Autorise l'agent à exécuter l'action en attente (send_email) avec le texte initialement prévu.

Refuser (Partie 4) : Annule l'action en attente et transmet un motif de rejet à l'agent.

Modifier (Partie 5) : Intercepte les arguments de l'outil et injecte un nouveau corps de message manuellement corrigé avant l'envoi final.

⚙️ Concepts Clés du TP
HumanInTheLoopMiddleware : Composant intermédiaire qui intercepte l'exécution de l'agent selon une configuration prédéfinie (ici, interrupt_on={"send_email": True}).

InMemorySaver (Checkpointer) : Permet de sauvegarder l'état de l'agent en mémoire vive à l'aide d'un thread_id unique, rendant possible la mise en pause et la reprise transparente du flux.

Command(resume=...) : Objet permettant d'envoyer la décision humaine à l'agent mis en pause pour relancer sa logique.