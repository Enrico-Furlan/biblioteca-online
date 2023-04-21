#Classe tobook
#Attributi id_client, id_book, booking_end_date
#Metodi get_id_client, get_id_book, get_booking_date, set_id_client, set_id_book, set_booking_date, booking, restitution

from f_connection_select import recSelect
from f_deletion import recDelete
from f_alter import recUpdate
from f_insert import insertData

class tobook:
    def __init__(self, id_client, id_book, booking_end_date):
        self.id_client = id_client
        self.id_book = id_book
        self.booking_end_date = booking_end_date

    def get_id_client(self):
        return self.id_client
    
    def get_id_book(self):
        return self.id_book
    
    def get_booking_date(self):
        return self.booking_end_date

    def set_id_client(self, id_client):
        self.id_client = id_client

    def set_id_book(self, id_book):
        self.id_book = id_book

    def set_booking_date(self, booking_date):
        self.booking_end_date = booking_date

    def booking(self):
        insertData([{"ID_libro" : str(self.id_book), "ID_cliente" : str(self.id_client), "data_fine" : str(self.booking_end_date)}], "noleggio")
        recUpdate("libro", {"ID_libro" : str(self.id_book)}, "copie_magazzino", "copie_noleggiate + 1")
        recUpdate("libro", {"ID_libro" : str(self.id_book)}, "riserva_noleggio", "riserva_noleggio - 1")

    def restitution(self):
        recDelete("noleggio", "ID_cliente", self.id_client)
        recUpdate("libro", {"ID_libro" : str(self.id_book)}, "copie_noleggiate", "copie_noleggiate - 1")
        recUpdate("libro", {"ID_libro" : str(self.id_book)}, "riserva_noleggio", "riserva_noleggio + 1")

if __name__ == "__main__":
    book = tobook(2, 1, "2023-03-31")
    book.booking()
    book.restitution()