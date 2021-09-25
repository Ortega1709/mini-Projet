# classe qui gère les horaires selon les villes

class Horaires:
    def __init__(self,ville) -> None:
        self.ville = ville.lower()

    def horaire_1(self) -> str:
        return ""
    
    def horaire_2(self) -> str:
        return ""
    
    def horaire_3(self) -> str:
        return ""
    
    def horaire_4(self) -> str:
        return ""
    
    def horaire_5(self) -> str:
        return ""

    def horaires(self) -> str:
        if self.ville == "lubumbashi":
            return self.horaire_1()
        if self.ville == "likasi":
            return self.horaire_2()
        if self.ville == "kolwezi":
            return self.horaire_3()
        if self.ville == "kasumbalesa":
            return self.horaire_4()
        if self.ville == "fungurume":
            return self.horaire_5()
