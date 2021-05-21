import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="kiranjp",
  password="root",
  database="employee3"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("kiran", "vennala")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")