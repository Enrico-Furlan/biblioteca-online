# Definition of the libraries

from f_connection_select import *

# Definition of the function


def recUpdate(tb_name, nameInput, newInput, IDname, IDvalue):
    mydb = fastConnect()
    cursor = mydb.cursor()
    cursor.execute("UPDATE %s SET %s = %s WHERE %s = %s" %
                   (tb_name, nameInput, newInput, IDname, IDvalue))

# Test


if __name__ == "__main__":
    recUpdate("libro", "titolo", "mandi", "ID_libro", "1")
