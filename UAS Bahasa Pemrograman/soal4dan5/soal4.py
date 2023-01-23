import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port=23306,
  user="root",
  password="p455w0rd",
  database="basis_data"
)

print(mydb)