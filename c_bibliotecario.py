from f_connection_select import recSelect
from f_controlloCredenziali import controllo
from f_cancellaAccount import cancella
from f_insert import insert


class Bibliotecario:
    def __init__(self, ID, pwd):
        self.ID = ID
        self.pwd = pwd

    def getID(self):
        return self.ID

    def setID(self, ID):
        self.ID = ID

    def getpwd(self):
        return self.pwd

    def setwpd(self, pwd):
        self.pwd = pwd

    def logIn(self):
        ID = str(input("Inserisci la ID: "))
        pwdMaybe = str(input("Inserisci la password: "))
        dati = controllo(
            recSelect("bibliotecario", {"ID_bibliotecario": ID}, "*"), pwdMaybe)
        self.setID(dati["ID_bibliotecario"])

    def register(self):
        ID = str(input("Inserisci il tuo ID: "))
        pwd = str(input("Inserisci la tua password: "))
        insert("bibliotecario", {"ID_bibliotecario": ID, "password": pwd})
        print("Registrazione avvenuta con successo!")
