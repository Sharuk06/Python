#Prgram to implement DB Connectivity
import mysql.connector

con=mysql.connector.connect(user='root',password='', database='python',host='localhost')
com=con.cursor()

query=("insert into details (name,age) VALUES('Aravinth',15)")

com.execute(query)

query = "Select * from details"

com.execute(query)

print com.fetchall()

com.close()
con.close()
