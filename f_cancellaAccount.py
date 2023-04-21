from f_deletion import recDelete
from f_controlloCredenziali import controllo


def cancella(dati, pwd):
    recDelete("cliente", controllo(dati, pwd))
