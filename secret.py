import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="adi01334",
 database="IPL"
)

mycursor = mydb.cursor()

#mycursor.execute("SHOW DATABASES ")
#for x in mycursor:
 # print(x)
mycursor.close()