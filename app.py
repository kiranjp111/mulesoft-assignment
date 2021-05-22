import flask
from flask import request, jsonify,make_response
import sqlite3
import mysql.connector
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Customer Details</h1>
<p>A prototype API for displaying customer details</p>'''

@app.route('/retrieve', methods=['GET'])
def retrieve():

    mydb = mysql.connector.connect(
        host="localhost",
        user="kiranjp",
        password="root",
        database="employee3"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()
    output=""

    for x in myresult:
        output=str(x)+"\n"+output

    response = make_response( output, 200)
    response.mimetype = "text/plain"
    return response

@app.route('/insert', methods=['POST'])
def insert():
    mydb = mysql.connector.connect(
        host="localhost",
        user="kiranjp",
        password="root",
        database="employee3"
    )
    name=request.form.get('name')
    address= request.form.get('address')
    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (name, address)
    mycursor.execute(sql, val)

    mydb.commit()

    output=str(mycursor.rowcount)+  " record inserted"
    response = make_response(output, 200)
    response.mimetype = "text/plain"
    return response

app.run()