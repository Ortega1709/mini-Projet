#***********************************************#
#       FONCTION PRINCIPALE GESTION D'AUTOCARS  #
#***********************************************#

from os import system
from time import sleep
from horaires import Horaires
from places import Places
from choix import Choix
from reservation import Reservation
import sys

#*****************************start*********************************#
def start():

    system("clear")
    sleep(1)
    print("                                                                         :0%")
    sleep(1)
    system("clear")
    print("#                                                                        :1%")
    sleep(2)
    system("clear")
    print("##########                                                              :10%")
    sleep(1)
    system("clear")
    print("#######################################                                 :50%")
    sleep(1)
    system("clear")
    print("#######################################################                 :75%")
    sleep(2)
    system("clear")
    print("###################################################################### :100%")
    sleep(1)
    system("clear")
    print("      [Starting] ...")
    sleep(2)
    

#*****************************Acceuil*******************************#
def acceuil():
    system("clear")
    sleep(1)
    print("""    ____           _   _                  _         _         ____                """) 
    print("""   / ___| ___  ___| |_(_) ___  _ __      / \  _   _| |_ ___  / ___|__ _ _ __ ___  """) 
    print("""  | |  _ / _ \/ __| __| |/ _ \| '_ \    / _ \| | | | __/ _ \| |   / _` | '__/ __| """)
    print("""  | |_| |  __/\__ \ |_| | (_) | | | |  / ___ \ |_| | || (_) | |__| (_| | |  \__ \ """)
    print("""   \____|\___||___/\__|_|\___/|_| |_| /_/   \_\__,_|\__\___/ \____\__,_|_|  |___/ """)
    print("                                                                                      ")
    print("        [1]       Faire une réservation chez nous                                     ")
    print("        [2]       Informations sur nous                                               ")
    print("        [3]       Voir les reservations                                               ")
    print("        [4]       Quitter                                                             ")
    print("                                                                                      ")
    try:
        CHOIX = int(input("        [Acceuil]: "))
        return CHOIX
    except:
        print("         Veuillez entrer un entier")

#****************************Réservations***************************#
def reservation():
    system("clear")
    sleep(1)
    print("""   ____                                _   _                                     """) 
    print("""  |  _ \ ___  ___  ___ _ ____   ____ _| |_(_) ___  _ __  ___                     """) 
    print("""  | |_) / _ \/ __|/ _ \ '__\ \ / / _` | __| |/ _ \| '_ \/ __|                    """)
    print("""  |  _ <  __/\__ \  __/ |   \ V / (_| | |_| | (_) | | | \__ \                    """)
    print("""  |_| \_\___||___/\___|_|    \_/ \__,_|\__|_|\___/|_| |_|___/                    """)
    print("                                                                                     ")
    print("         [1]     Faire une réservation pour singleton                                ")
    print("         [2]     Faire une réservation pour couple                                   ")
    print("         [Ctrl+C]     Retour à l'acceuil                                             ")
    print("                                                                                     ")
    try:
        CHOIX = int(input("        [Réservation]: "))
        return CHOIX
    except:
        print("         Veuillez entrer un entier")

#***************************Informations****************************#
def informations():
    system("clear")
    sleep(1)
    print("""    ___        __                            _   _                             """)
    print("""   |_ _|_ __  / _| ___  _ __ _ __ ___   __ _| |_(_) ___  _ __  ___             """)
    print("""    | || '_ \| |_ / _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \/ __|            """)
    print("""    | || | | |  _| (_) | |  | | | | | | (_| | |_| | (_) | | | \__ \            """)
    print("""   |___|_| |_|_|  \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|___/            """)
    print("                                                                                   ")
    print("""       Informations sur l'entreprise de transport quelconque                   """)
    print("""          Crée le 17 septembre par Mr Ortega Kabwe Mulunda                     """)
    print("                                                                                   ")
    print("         [Ctrl+C]     Retour à l'acceuil                                           ")
    try:
        CHOIX = int(input("         [Informations]: "))
        return CHOIX
    except:
        print("         Veuillez entrer un entier")
        

#***********************Formulaire singleton************************#
def formulaire_singleton():
    system("clear")
    sleep(1)
    print("""    _____                          _       _                                  """)
    print("""   |  ___|__  _ __ _ __ ___  _   _| | __ _(_)_ __ ___                         """)
    print("""   | |_ / _ \| '__| '_ ` _ \| | | | |/ _` | | '__/ _ \                        """)
    print("""   |  _| (_) | |  | | | | | | |_| | | (_| | | | |  __/                        """)
    print("""   |_|  \___/|_|  |_| |_| |_|\__,_|_|\__,_|_|_|  \___|              singleton """)
    print("                                                                                  ")
    nom = str(input("Nom:"))

#***********************Formulaire couple**************************#
def formulaire_couple():
    system("clear")
    sleep(1)
    print("""    _____                          _       _                                  """)
    print("""   |  ___|__  _ __ _ __ ___  _   _| | __ _(_)_ __ ___                         """)
    print("""   | |_ / _ \| '__| '_ ` _ \| | | | |/ _` | | '__/ _ \                        """)
    print("""   |  _| (_) | |  | | | | | | |_| | | (_| | | | |  __/                        """)
    print("""   |_|  \___/|_|  |_| |_| |_|\__,_|_|\__,_|_|_|  \___|              couple    """)
    print("                                                                                  ")
    nom = str(input("Nom:"))

#********************Voir réservations******************************#
def voir_reservations():
    system("clear")
    sleep(1)
    voir = Reservation()
    print(voir.reservations())
    print("                                                                                  ")
    print("         [Ctrl+C]     Retour à l'acceuil                                          ")
    try:
        CHOIX = int(input("         [Réservations]: "))
        return CHOIX
    except:
        print("         Veuillez entrer un entier")


#********************Exec*******************************************#
def executable():

    start()
    vouloir = str(input("      Commencer(O/N) ? "))
    c = Choix(vouloir,4)
    while c.validation_choix() == False:
        vouloir = str(input("      Insérer entre(O/N) ? "))
        c = Choix(vouloir,4)
    
    while vouloir != "N":
        vouloir1 = acceuil()
        cc = Choix(vouloir1,1)
        if vouloir1 == 1:
            vouloir1 = reservation()
            cc = Choix(vouloir1,2)
        if vouloir1 == 2:
            vouloir1 = informations()
            cc = Choix(vouloir1,3)
        if vouloir1 == 3:
            vouloir1 = voir_reservations()
            cc = Choix(vouloir1,5)
        if vouloir1 == 4:
            vouloir = "N"
    
    print(vouloir)
    
    # pas encore finis #
    


    








