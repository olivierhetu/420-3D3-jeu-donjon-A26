# models/ennemi_aleatoire.py
import random
from models.ennemie import Ennemi


class EnnemiAleatoire(Ennemi):
    """Choisit aléatoirement entre attaquer et défendre."""

    def agir(self) -> str:
        if self.change_comportement():
            return "defend"
        else:
            return random.choice(["attaque", "defend"])