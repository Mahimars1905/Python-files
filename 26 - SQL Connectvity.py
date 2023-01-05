# # pip install mysql-connector
# # pip install mysql-connector-python

import mysql.connector

# #  open database connectivity
mydb = mysql.connector.connect(host="localhost", 
             user= "root", password='7354062672',
             database="customer")

# # cursor method to create a cursor object
mycursor = mydb.cursor() 
mycursor.execute("select * from customer")
mycursor.execute(" create database dbtutorial")

# # for fething all records
result = mycursor.fetchall()
for i in result:
    print(i)
    
mydb.close()
