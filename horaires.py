# classe qui gère les horaires selon les villes


class Horaires:
    def __init__(self,ville) -> None:
        self.ville = ville.lower()

    def horaires_read(self,file) -> str:
        with open("files_txt/"+file,"r") as file_read:
            return file_read.read()

    def horaire(self) -> str:
        if self.ville == "lubumbashi":
            return self.horaires_read("lubumbashi.txt")
        if self.ville == "likasi":
            return self.horaires_read("likasi.txt")
        if self.ville == "kolwezi":
            return self.horaires_read("kolwezi.txt")
        if self.ville == "kasumbalesa":
            return self.horaires_read("kasumbalesa.txt")
        if self.ville == "fungurume":
            return self.horaires_read("fungurume.txt")



