import json
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()

class ChefAgent:
    def __init__(self, memory_path="data/memory_store.json"):
        self.memory_path = memory_path
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
        self.search_tool = DuckDuckGoSearchRun()
        self.system_message = (
            "Tu es un Chef cuisinier personnel étoilé et expert anti-gaspillage. "
            "Règles strictes :\n"
            "1. Utilise PRIORITAIREMENT les ingrédients du frigo.\n"
            "2. Respecte TOUJOURS le profil, les allergies et régimes de l'utilisateur.\n"
            "3. Propose des recettes claires, structurées et rapides."
        )
        self.init_memory()

    def init_memory(self):
        """Initialise ou charge la mémoire/profil utilisateur."""
        if not os.path.exists(self.memory_path) or os.stat(self.memory_path).st_size == 0:
            default_profile = {"preferences": "Aucune", "allergies": "Aucune", "regime": "Omnivore"}
            with open(self.memory_path, 'w') as f:
                json.dump(default_profile, f)
        
    def get_profile(self):
        with open(self.memory_path, 'r') as f:
            return json.load(f)

    def update_profile(self, key, value):
        profile = self.get_profile()
        profile[key] = value
        with open(self.memory_path, 'w') as f:
            json.dump(profile, f, indent=4)

    def simuler_rag(self, ingredients):
        """Simule un RAG rapide sans configurer ChromaDB pour gagner du temps."""
        # Si besoin d'un vrai appel web pour compléter
        try:
            return self.search_tool.run(f"recette simple avec {ingredients}")
        except:
            return "Pas de connexion web, utilisation des connaissances internes."

    def cuisiner(self, ingredients):
        profile = self.get_profile()
        
        # Recherche de connaissances complémentaires (RAG / Web)
        connaissances = self.simuler_rag(ingredients)
        
        prompt_construction = f"""
        PROFIL UTILISATEUR: {json.dumps(profile)}
        INGRÉDIENTS DISPONIBLES: {ingredients}
        INSPIRATION TECHNIQUE: {connaissances}
        
        Propose 1 à 2 recettes adaptées.
        """
        
        messages = [
            SystemMessage(content=self.system_message),
            HumanMessage(content=prompt_construction)
        ]
        
        response = self.llm.invoke(messages)
        return response.content