import mysql.connector
import utils

mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="projet_rdv_medical"
)

mycursor = mydb.cursor()

mycursor.execute(utils.specialite)
