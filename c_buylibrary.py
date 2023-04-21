class buylibrary:
    def __init__(self, id_book, quantity):
        self.id_book = id_book
        self.quantity = quantity
    
    def get_id_book(self):
        return self.id_book

    def get_quantity(self):
        return self.quantity
    
    def set_id_book(self, id_book):
        self.id_book = id_book
    
    def set_quantity(self, quantity):
        self.quantity = quantity
        