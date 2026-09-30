# models/ennemi_agressif.py
from models.ennemie import Ennemi


class EnnemiAgressif(Ennemi):
    """Attaque à chaque tour, sans exception."""

    def agir(self) -> str:
        if self.change_comportement():
            pass
        else:
            return "attaque"
    