#Function: update a record in a table

from f_connection_select import *

def recUpdate(tb_name, nameInput, newInput, IDname, IDvalue):
    mydb = fastConnect()
    cursor = mydb.cursor()
    cursor.execute("UPDATE %s SET %s = %s WHERE %s = %s" % (tb_name, nameInput, newInput, IDname, IDvalue))

if __name__ == "__main__":
    recUpdate("libro", "titolo", "mandi", "ID_libro", "1")
