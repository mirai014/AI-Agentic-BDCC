import sys
import os
import json
from dotenv import load_dotenv

# Force l'import de Groq
try:
    from groq import Groq
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "groq python-dotenv"])
    from groq import Groq

load_dotenv()

class ChefAgentAutonome:
    def __init__(self, memory_path="data/memory_store.json"):
        self.memory_path = memory_path
        
        # Récupère la clé depuis le .env OU mets-la directement entre les guillemets ci-dessous
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key or "gsk_" not in api_key:
            api_key = "METS_TA_CLE_GROQ_ICI_SI_BESOIN"
            
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile" 
        
        self.system_message = (
            "Tu es un Chef cuisinier personnel étoilé et expert anti-gaspillage. "
            "Règles strictes :\n"
            "1. Utilise PRIORITAIREMENT les ingrédients du frigo.\n"
            "2. Respecte TOUJOURS le profil, les allergies et régimes de l'utilisateur.\n"
            "3. Propose 1 à 2 recettes claires, structurées et rapides."
        )
        self.init_memory()

    def init_memory(self):
        os.makedirs(os.path.dirname(self.memory_path), exist_ok=True)
        if not os.path.exists(self.memory_path) or os.stat(self.memory_path).st_size == 0:
            default_profile = {"preferences": "Aucune", "allergies": "Aucune"}
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

    def cuisiner(self, ingredients):
        profile = self.get_profile()
        prompt_construction = f"""
        PROFIL UTILISATEUR (Mémoire): {json.dumps(profile)}
        INGRÉDIENTS DISPONIBLES DANS LE FRIGO: {ingredients}
        
        En te basant sur tes connaissances culinaires, propose une recette adaptée.
        """
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": prompt_construction}
            ],
            model=self.model,
            temperature=0.7
        )
        return chat_completion.choices[0].message.content

def main():
    # Instance locale autonome
    chef = ChefAgentAutonome()
    
    chef.update_profile("allergies", "Gluten")
    chef.update_profile("preferences", "Adore le piquant")
    
    mon_frigo = "Poulet, courgettes, crème fraîche, riz"
    print("👨‍🍳 Le Chef connecté à Groq réfléchit à votre repas...\n")
    
    reponse = chef.cuisiner(mon_frigo)
    
    print("--- PROPOSITION DU CHEF ---")
    print(reponse)

if __name__ == "__main__":
    main()