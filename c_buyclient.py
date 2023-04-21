from multiprocessing import connection
from c_book import *
from c_client import *
from f_connection_select import fastConnect, recSelect
from main import login
class buyclient:
    def __init__(self, id_client, id_book, quantity):
        self.id_client = id_client
        self.id_book = id_book
        self.quantity = quantity
    
    def get_id_client(self):
        return self.id_client
    
    def get_id_book(self):
        return self.id_book

    def get_quantity(self):
        return self.quantity
    
    def set_id_client(self, id_client):
        self.id_client = id_client
    
    def set_id_book(self, id_book):
        self.id_book = id_book

    def set_quantity(self, quantity):
        self.quantity = quantity

    def getTotalCost(self, prezzo, ID_libro):
        fastConnect()
        cursor = connection.cursor()
        result = cursor.execute("SELECT libro.ID_libro,carrello_cliente.ID_libro, SUM(prezzo) FROM libro,carrello_cliente WHERE libro.ID_libro=carrello_cliente.ID_libro")
        print(result)
    
    def getBookQuantity(self, quantita):
        fastConnect()
        cursor = connection.cursor()
        result = cursor.execute("SELECT SUM(quantita) FROM carrello_cliente")
        print(result)
    
    def getBookCost(self, prezzo, ID_libro):
        fastConnect()
        result=recSelect("SELECT libro.prezzo,libro.ID_libro, carrello_cliente.ID_libro FROM libro,carrello_cliente WHERE libro.ID_libro=carrello_cliente.ID_libro")
   
    def getBookList(self, titolo, ID_libro):
        fastConnect()
        result=recSelect("SELECT libro.titolo,libro.ID_libro, carrello_cliente.ID_libro FROM libro,carrello_cliente WHERE libro.ID_libro=carrello_cliente.ID_libro")