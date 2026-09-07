import mysql.connector

connection=mysql.connector.connect(  
      host="mysql",
      username="admin",
      password="rdscnt1231",
      database="databases3"
)
cursor=connection.cursor()

cursor.execute("SELECT * FROM Employees")

for row in cursor.fetchall():
  print(row)

cursor.close()
connection.close()
