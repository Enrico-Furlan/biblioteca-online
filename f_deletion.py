from f_connection_select import fastConnect

def dbDelete(db_name):
    cursor = fastConnect().cursor()
    cursor.execute("DROP DATABASE ", db_name)

def tbDelete(tb_name):
    cursor = fastConnect().cursor()
    cursor.execute("DROP TABLE", tb_name, " ")
    
def recDelete(tb_name, nameInput, Input):
    cursor = fastConnect().cursor()
    cursor.execute("DELETE FROM", tb_name, "WHERE", nameInput, "=", Input)
    