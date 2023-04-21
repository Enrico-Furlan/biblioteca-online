# Classe book
# Attributi title, author, price, isbn, copies, reserved, rented
# Metodi get_title, get_author, get_isbn, get_price, get_copies, get_reserved, get_rented, set_copies, set_reserved, set_price, set_rented, is_rentable, is_low

from f_connection_select import recSelect
from f_insert import insertData
from f_deletion import recDelete


class Book:

    # Costruttore

    def __init__(self, title, author, price, isbn, copies, reserved, rented):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.copies = copies
        self.reserved = reserved
        self.rented = rented

    # Getters e setters

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_isbn(self):
        return self.isbn

    def get_price(self):
        return self.price

    def get_copies(self):
        return self.copies

    def get_reserved(self):
        return self.reserved

    def get_rented(self):
        return self.rented

    def set_copies(self, copies):
        self.copies = copies

    def set_reserved(self, reserved):
        self.reserved = reserved

    def set_price(self, price):
        self.price = price

    def set_rented(self, rented):
        self.rented = rented

    # Metodi

    def insert(self):
        insertData([{"titolo": str(self.title), "autore": str(self.author), "prezzo": str(self.price), "ISBN": str(
            self.isbn), "copie_magazzino": str(self.copies), "riserva_noleggio": str(self.reserved), "copie_noleggiate": str(self.rented)}], "libro")

    def delete(self):
        recDelete("libro", {"ISBN": str(self.isbn)})

    def is_rentable(self):
        result = recSelect(
            "libro", {"ISBN": str(self.isbn)}, "copie_magazzino")
        if result:
            return True
        else:
            return False

    def is_low(self):
        copie_magazzino = recSelect("libro", {"ISBN": str(self.isbn)}, "copie_magazzino")[
            0].get("copie_magazzino")
        riserva_noleggio = recSelect("libro", {"ISBN": str(self.isbn)}, "riserva_noleggio")[
            0].get("riserva_noleggio")
        copie_noleggiate = recSelect("libro", {"ISBN": str(self.isbn)}, "copie_noleggiate")[
            0].get("copie_noleggiate")
        if copie_noleggiate + copie_magazzino < riserva_noleggio:
            return True
        else:
            return False


# Main

if __name__ == "__main__":
    libro = Book("ciao", "Verga", 20, 112312321, 7, 1, 1)
    print(libro.is_rentable())
    print(libro.is_low())
