# 👨‍🍳 Agent Intelligent - Chef Cuisinier Personnel

Ce projet présente un agent intelligent jouant le rôle d'un Chef cuisinier personnel. L'agent analyse les ingrédients disponibles dans le réfrigérateur, consulte le profil de l'utilisateur (mémoire) pour respecter ses allergies et préférences, et utilise un LLM pour générer des recettes sur-mesure adaptées.

---

## 🛠️ Prérequis & Installation

1. **Python** (version 3.x)
2. **Dépendances** : Installez les bibliothèques requises avec la commande suivante :
  
  > pip install groq python-dotenv

Clé API : Créez un fichier .env à la racine du projet et ajoutez votre clé Groq : (utilisé dans ce TP car il est gratuit)

Plaintext
GROQ_API_KEY=gsk_VotreCleGroqIci...

🚀 Mode de Fonctionnement
L'agent repose sur une architecture à 4 piliers :

System Message (Identité) : Définit le rôle de Chef étoilé expert en anti-gaspillage et impose le respect strict des contraintes.

Gestion de la Mémoire (data/memory_store.json) : Sauvegarde et charge dynamiquement le profil utilisateur (ex: Allergie au Gluten, Préférence pour le Piquant).

Moteur d'Inférence (LLM via Groq) : Utilise le modèle ultra-rapide llama-3.3-70b-versatile.

Context Injection (RAG / Web virtuel) : Combine le profil de la mémoire et la liste des ingrédients du frigo pour enrichir le prompt final envoyé à l'IA.

💻 Exécution
Pour lancer l'agent et générer une recette personnalisée, exécutez le script principal :

> python main.py
Le script va mettre à jour la mémoire utilisateur, analyser le frigo ("Poulet, courgettes, crème fraîche, riz") et afficher la recette exclusive du Chef dans la console.