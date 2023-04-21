from f_connection_select import fastConnect, recSelect

def menu():
    print("Libreria Sdrumo")
    print("1. Visualizza prodotti")
    print("2. Login") 
    print("3. Registrati")
    print("4. Esci")

def visualizzaProdotti():
    fastConnect()
    result = recSelect("libro", {}, "*")
    print(result)

def login():
    pass

def registrati():
    pass

if __name__ == "__main__":
    menu()