from f_connection_select import fastConnect, recSelect
from c_book import is_rentable
from datetime import datetime

class reservation:
    def __init__(self, id_client, id_book, booking_date):
        self.id_client = id_client
        self.id_book = id_book
        self.booking_date = booking_date

    def get_id_client(self):
        return self.id_client
    
    def get_id_book(self):
        return self.id_book
    
    def get_booking_date(self):
        return self.booking_date
    
    def set_id_client(self, id_client):
        self.id_client = id_client

    def set_id_book(self, id_book):
        self.id_book = id_book

    def set_booking_date(self, booking_date):
        self.booking_date = booking_date
    
    def make_reservation(self, libro, cliente):
        fastConnect()
        if is_rentable(self):
            id_book=recSelect("libro", {"ISBN" : str(libro.get_isbn())}, "ID_libro")
            id_client=recSelect("cliente", {"email" : str(cliente.getEmail())}, "ID_cliente")
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            print("date and time =", dt_string)

            
#crea prenotazione
#aggiungi libro
#rimuovi libro
