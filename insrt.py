import  mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="kiranjp",
  password="root",
  database="employee3"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

