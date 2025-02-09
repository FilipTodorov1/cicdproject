import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Fitz1234",

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE djangoappdb")

print ("All Done!")