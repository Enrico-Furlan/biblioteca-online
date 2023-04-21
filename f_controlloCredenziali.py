from f_connection_select import recSelect


def controllo(dati, pwd):
    if dati[0]["password"] == pwd:
        print("Login effettuato con successo")
        return dati[0]
    else:
        print("Password errata")
