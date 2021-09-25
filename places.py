# classe qui gère les places

class Places:
    def __init__(self,L,bus) -> None:
        self.L = L
        self.bus = bus
        self.p = 0
        self.p1 = 0
        self.l = 0
        self.l1 = 0
        self.n = 0
        self.n1 = 0

    def verification_places_singletons(self) ->bool:
        if len(self.L) > 0:
            return True
        return False

    def verification_places_couples(self) -> bool:
        if len(self.L) > 2:
            return True
        return False

    def compatible_places_couples(self,p,p1) -> bool: #verifie si deux places placées en paramètre sont compatibles
        self.l = p[0]
        self.l1 = p1[0]
        self.n = int(p[1])
        self.n1 = int(p[1])
         
        if self.l == self.l1:
            if self.n + 1 == self.n1 and self.n + 1 != 3:
                return True
            return False
        return False
    
    def attribut_places_singletons(self) -> bool:
        if self.verification_places_singletons() == False:
            print("Plus de place dans le premier Bus",self.bus)
            return
        else:
            self.p = self.L[0]
            self.L.remove(self.p)
            return f"{self.p}"
    
    def attribut_places_couples(self) -> bool:
        if self.verification_places_couples() == False:
            print("Plus de place pour couple dans le bus",self.bus)
            return 
        else:
            for i in range(len(self.L) - 1):
                if self.compatible_places_couples(self.L[i],self.L[i+1]):
                    self.p = self.L[i]
                    self.p1 = self.L[i+1]
                    self.L.remove(self.p)
                    self.L.remove(self.p1)
                    return f"{self.p},{self.p1}"
            print("Pas de place pour couple dans le bus",self.bus)
            return 
    



