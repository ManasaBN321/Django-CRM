import mysql.connector

dataBase = mysql.connector.connect(
    host ='localhost',
    user ='root',
    passwd = 'Maan'
)

#cursor object
cursorObject = dataBase.cursor()

#create database

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")


