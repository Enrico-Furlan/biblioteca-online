#creazione data base, tabelle e insert
import mysql.connector
from mysql.connector import Error
from f_connection_select import dbConnection, hostConnection, fastConnect

def dbCreate(db_name):
    connection = fastConnect()
    cursor = connection.cursor()
    query = "CREATE DATABASE " + db_name
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def tbCreate(tb_name, col_attr):
    connection = fastConnect()
    cursor = connection.cursor()
    query = "CREATE TABLE IF NOT EXISTS " + tb_name + " ( "
    for i in range(len(col_attr)):

      query += col_attr[i][0] + " "

      if col_attr[i][1] == "str":
        query += "VARCHAR(255) "
      elif col_attr[i][1] == "int":
        query += "INT "
      elif col_attr[i][1] == "dec":
        query += "DECIMAL(6,2) "
      elif col_attr[i][1] == "date":
         query += "DATE "

      if col_attr[i][2]:
        query += "AUTO_INCREMENT "
      if col_attr[i][3]:
        query += "NOT NULL "

      query += ","

      if col_attr[i][5] != "":
        query += " FOREIGN KEY (" + col_attr[i][0] + ") REFERENCES " + col_attr[i][5] + "(" + col_attr[i][6] + "),"
    
    query += " PRIMARY KEY ("
    for i in range(len(col_attr)):
      if col_attr[i][4]:
        query += col_attr[i][0] + ","

    query = query[:-1]
    query += ")) ENGINE = InnoDB"
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

#           (nome, tipo, auto_inc, not_null, pk, fk_table, fk_ref)
tb_libro = [("ID_libro", "int", True, True, True, "", ""),
            ("titolo", "str", False, True, False, "", ""),
            ("autore", "str", False, False, False, "", ""),
            ("ISBN", "str", False, False, False, "", ""),
            ("prezzo", "dec", False, True, False, "", ""),
            ("copie_magazzino", "int", False, True, False, "", ""),
            ("riserva_noleggio", "int", False, True, False, "", "")]

tb_cliente = [("ID_cliente", "int", True, True, True, "", ""), 
              ("nome", "str", False, True, False, "", ""),
              ("cognome", "str", False, True, False, "", ""),
              ("indirizzo", "str", False, True, False, "", ""),
              ("email", "str", False, True, False, "", ""),
              ("password", "str", False, True, False, "", "")]

tb_noleggio = [("ID_noleggio", "int", True, True, True, "", ""),
               ("data_fine", "date", False, True, False, "", ""),
               ("ID_cliente", "int", False, True, False, "cliente", "ID_cliente"),
               ("ID_libro", "int", False, True, False, "libro", "ID_libro")]

tb_bibliotecario = [("ID_bibliotecario", "int", True, True, True, "", ""),
                    ("password", "str", False, True, False, "", "")]

tb_carrello_cliente = [("ID_cliente", "int", False, True, True, "cliente", "ID_cliente"),
                       ("ID_libro", "int", False, True, True, "libro", "ID_libro"),
                       ("quantita", "int", False, True, False, "", "")]

tb_carrello_bibliotecario = [("ID_libro", "int", False, True, True, "libro", "ID_libro"),
                             ("quantita", "int", False, True, False, "", "")]

tb_prenotazione = [("ID_cliente", "int", False, True, True, "cliente", "ID_cliente"),
                   ("ID_libro", "int", False, True, True, "libro", "ID_libro"),
                   ("data_richiesta", "date", False, True, False, "", "")]

if __name__ == "__main__":
  #dbCreate("Libreria")
  tbCreate("libro", tb_libro)
  tbCreate("cliente", tb_cliente)
  tbCreate("noleggio", tb_noleggio)
  tbCreate("bibliotecario", tb_bibliotecario)
  tbCreate("carrello_cliente", tb_carrello_cliente)
  tbCreate("carrello_bibliotecario", tb_carrello_bibliotecario)
  tbCreate("prenotazione", tb_prenotazione)