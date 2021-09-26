# classe qui gère des reservations

class Reservation:

    # initialise un tableau vide
    def __init__(self) -> None:
        self.tableauInfo = []

    # methodes
    def formulaire_singleton(self,nom,ville_o,ville_a,date_reservation,place) -> None:
        self.tableauInfo = [nom,ville_o,ville_a,date_reservation,place]
        with open("files_txt/reservation.txt","a") as file_write:
            file_write.write(f"\nRESERVATION SIGNLETON\n\nNom: {self.tableauInfo[0]}\nVille de depart: {self.tableauInfo[1]}\nVille d'arrivée: {self.tableauInfo[2]}\nPlace: {self.tableauInfo[3]}\nDate de reservation: {self.tableauInfo[4]}\n")
            

    def formulaire_couple(self,nom,ville_o,ville_a,date_reservation,nom1,ville_o1,ville_a1,date_reservation1,place):
        self.tableauInfo = [nom,ville_o,ville_a,date_reservation,nom1,ville_o1,ville_a1,date_reservation1,place]
        with open("files_txt/reservation.txt","a") as file_write:
            file_write.write(f"\nRESERVATION COUPLE\n\nNom: {self.tableauInfo[0]}\nVille de depart: {self.tableauInfo[1]}\nVille d'arrivée: {self.tableauInfo[2]}\nDate de reservation: {self.tableauInfo[3]}\nNom: {self.tableauInfo[4]}\nVille de depart: {self.tableauInfo[5]}\nVille d'arrivée: {self.tableauInfo[6]}\nDate de reservation: {self.tableauInfo[7]}\nPlaces: {self.tableauInfo[8]}\n")

    def reservations(self):
        with open("files_txt/reservation.txt","r") as file_read:
            return file_read.read()