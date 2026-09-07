import mysql.connector
#Connection = connection to database
#Cursor = performs database operations through that connection
connection=mysql.connector.connect(  
      host="databases3.crosuwuk8vh3.ap-south-1.rds.amazonaws.com",
      username="admin",
      password="rdscnt1231",
      database="databases3"
)
cursor=connection.cursor() #A cursor is an object that lets your Python program send SQL commands to the database and read the results. Think of it like a messenger between Python and MySQL.

cursor.execute("SELECT * FROM Employees")

for row in cursor.fetchall():
  print(row)

cursor.close()
connection.close()
