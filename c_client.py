from f_connection_select import fastConnect, recSelect

class Client:
    def __init__(self, name = "Guest", surname = None, email = None, address = None):
        self.name = name
        self.surname = surname
        self.email = email
        self.address = address    

    # get set name
    def getName(self):
        return self.name
        
    def setName(self, name):
        self.name = name

    # get set surname
    def getSurname(self):
        return self.surname
        
    def setSurname(self, surname):
        self.surname = surname
    
    # get set email
    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email
    
    # get set address
    def getAddress(self):
        return self.address
    
    def setAddress(self, address):
        self.address = address

    def isLoggedIn(self):
        if self.name != "Guest":
            return True
    
    def logIn(self):
        mail = str(input("Inserisci la mail: "))
        ID = recSelect("cliente", {"email" : mail}, "ID_cliente")
        if ID:
            dati = recSelect("cliente", {"ID_cliente" : ID}, "*")
            password = str(input("Inserisci la password: "))
            if dati["password"] == password:
                print("Login effettuato con successo")
                self.setEmail(mail)
                self.setName(dati["nome"])
                self.setSurname(dati["cognome"])
                self.setAddress(dati["indirizzo"])
                print("Benvenuto", self.getName(), self.getSurname())
            else:
                print("Password errata")
                
client = Client()
client.logIn()