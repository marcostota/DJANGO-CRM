import mysql.connector

dataBase = mysql.connector.connect(host="localhost", user="root", passwd="2248333")

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmdjango")

print("All done!")
