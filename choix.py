# classe qui gère les choix de l'utilisateur

class Choix:
    # chx
    # la categorie du choix 1 pour acceuil, 2 pour réservation, 3 pour informations, 4 pour les (O/N)
    def __init__(self,chx,categorie) -> None:
        self.chx = chx
        self.categorie = categorie
        self.L = [1,2,3] # liste des assertions dans chaque rubrique du programme
        self.Q = ["O","N"] # pour les questions du type (O/N)
        self.LL = [1,2,3,4]
    
    def verification_acceuil(self) -> bool:
        for i in range(len(self.LL)):
            if self.chx == self.LL[i]:
                return True
        return False
    
    def verification_reservation(self) -> bool:
        for i in range(len(self.L)):
            if self.chx == self.L[i]:
                return True
        return False
    
    def verification_information(self) -> bool:
        if self.chx == 3:
            return True
        return False
    
    def verification_voir(self) -> bool:
        if self.chx == 3:
            return True
        return False
    
    def verification_o_n(self) -> bool:
        for i in range(len(self.Q)):
            if self.chx == self.Q[i]:
                return True
        return False
    
    
    def validation_choix(self) -> bool: # retourne une verification selon la catégorie choisie
        if self.categorie == 1:
            return self.verification_acceuil()
        if self.categorie == 2:
            return self.verification_reservation()
        if self.categorie == 3:
            return self.verification_information()
        if self.categorie == 4:
            return self.verification_o_n()
        if self.categorie == 5:
            return self.verification_reservation()

