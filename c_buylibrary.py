from multiprocessing import connection  
from c_book import *
from c_client import *
from f_connection_select import fastConnect, recSelect
from c_book import is_low
class buylibrary:
    def __init__(self, id_book,id_client,title, quantity):
        self.id_book = id_book
        self.quantity = quantity
        self.id_client = id_client
        self.title =title
    
    def get_id_book(self):
        return self.id_book

    def get_quantity(self):
        return self.quantity

    def get_id_client(self):
        return self.id_client
    
    def get_title(self):
        return self.title
    
    def set_id_book(self, id_book):
        self.id_book = id_book
    
    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_id_client(self, id_client):
        self.id_clietn = id_client
        
    def set_title(self, title):
        self.title = title
        
    def getBookCost(self, ID_libro, copie_magazzino):
        fastConnect()
        result= recSelect("SELECT libro.copie_magazzino,libro.ID_libro, carrello_bibliotecario.ID_libro FROM libro,carrello_bibliotecario WHERE libro.ID_libro=carrello_bibliotecario.ID_libro")
        print(result)
        
    def book_available(self, cliente, libro):
        fastConnect()
        if is_low(self):
            print("Il libro è da acquistare")
        else:
            print("Il libro non è disponibile.")
