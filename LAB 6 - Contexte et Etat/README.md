🛠️ Guide d'Exécution
1. Installation de l'environnement
Ce projet utilise le gestionnaire moderne de paquets uv. Pour synchroniser l'environnement et installer les dépendances nécessaires (langchain, langchain-ollama, langgraph), exécutez :

> uv sync

2. Exécution de la partie Contexte (Parties 1 à 4)
Le fichier agent_context.py valide la transmission d'informations statiques relatives aux préférences de l'utilisateur (couleurs favorites et détestées).

> uv run python agent_context.py
Attendu : * Partie 2 : L'agent sans outils échoue à connaître votre couleur.

Partie 3 : L'agent avec outils récupère la couleur par défaut (blue).

Partie 4 : L'agent s'adapte immédiatement au changement dynamique (green).

3. Exécution de la partie État persistant (Parties 5 & 6)
Le fichier agent_state.py met en évidence la mémoire de l'agent capable de retenir une couleur apprise au cours de la discussion au sein d'un même thread_id.

> uv run python agent_state.py
Attendu :

L'agent reçoit l'information, met à jour son état via l'outil update_favourite_colour (renvoyant un objet Command).

Au message suivant, l'agent utilise read_favourite_colour pour restituer avec succès la couleur précédemment apprise.
