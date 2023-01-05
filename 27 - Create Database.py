import mysql.connector

# #  open database connectivity
mydb = mysql.connector.connect(host="localhost", 
             user= "root", password='7354062672')

# # cursor method to create a cursor object
mycursor = mydb.cursor() 

# # sql ="ceeate database dbtutorial"
# # mycursor.execute(sql)
mycursor.execute("create database dbtutorial")
mydp.commit()