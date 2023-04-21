import mysql.connector
from mysql.connector import Error

hostname = "localhost"
user = "root"
pw = ""
database = "libreria"


def hostConnection(hostName, userName, userPassword):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostName,
            user=userName,
            passwd=userPassword
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def dbConnection(hostName, userName, userPassword, dbName):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostName,
            user=userName,
            passwd=userPassword,
            database=dbName
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def recSelect(tbName, requirementsDict, fieldName):
    result = None
    try:
        connection = dbConnection(hostname, user, pw, database)
        if connection:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT " + fieldName + " FROM "+ tbName + " WHERE "
            for key in sorted(requirementsDict):
                query += key + " = " 
                if isinstance(requirementsDict.get(key),str):
                    query +=" '"+ requirementsDict.get(key) + "' AND "
                else:
                   query += str(requirementsDict.get(key)) + " AND "                    
            query = query[:-4] #rimozione degli ultimi 4 caratteri in quanto è presente un AND di troppo nella query
            print(query)
            cursor.execute(query)
            result = cursor.fetchall()
            diz = []
            #cast del risultato in un dizionario
            for row in result:
                diz.append(dict((k, v) for k, v in row.items() if v is not None))
        return diz
    except Error as e:
        print(f"The error '{e}'occurred")

def fastConnect():
    conn = dbConnection(hostname, user, pw, database)
    return conn
