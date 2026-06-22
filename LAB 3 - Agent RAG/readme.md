# LAB 3 : Agents Intelligents - RAG & SQL Expert

Ce projet contient deux applications d'agents IA autonomes développées pour le Master BDCC.

##  Étape 1 : Préparer les fichiers
Mettez tous ces fichiers dans le même dossier :
* Vos scripts `rag.py` et `sql_agent.py`
* Le fichier PDF : `acmecorp-employee-handbook.pdf`
* La base de données : `Chinook.db`

##  Étape 2 : Installer les outils
Ouvrez votre terminal et lancez cette unique commande :

pip install pypdf langchainhub langchain-community langchain-ollama

##  Étape 3 : Lancer Ollama
Ouvrez l'application Ollama sur votre ordinateur.

Téléchargez et lancez le modèle en tapant ceci dans le terminal :

ollama run llama3.2:3b

##  Étape 4 : Exécuter les scripts
Ouvrez un autre terminal dans votre dossier et lancez les agents :

Pour tester l'Agent RAG (PDF) :

python rag.py

Pour tester l'Agent SQL (Base de données) :

python sql_agent.py