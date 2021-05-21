import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="kiranjp",
  password="root"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE employee3")