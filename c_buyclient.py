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

    #getTotalCost
    #getBookList
    #getBookQuantity
    #getBookCost
    #getLogin
    #getBankApproval
    #getBookAvailability
    
