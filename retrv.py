import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="kiranjp",
  password="root",
  database="employee3"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)