#!C:/Users/Ayush Jain/AppData/Local/Programs/Python/Python37-32/python.exe -u

print("Content-Type: text/html")    
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
room_id = form.getvalue('room_id')
event_id = form.getvalue('event_id')
transaction_id = form.getvalue('transaction_id')
total_amount = form.getvalue('total_amount')
booking_date = form.getvalue('booking_date')
id_number = form.getvalue('id_number')
#print("Name of the user is:",name)

import pymysql;
# Open connection to the database
db = pymysql.connect("localhost","root","ayushjain03","HOTEL" )

# Start a cursor object using cursor() method
cursor = db.cursor()

# Execute a SQL query using execute() method. This should return all the columns of heroes that use swords.
cursor.execute("INSERT INTO RESERVATION (ID_NUMBER,EVENT_ID,TRANSACTION_ID,TOTAL_AMOUNT,BOOKING_DATE,ID_NUMBER) VALUES (%s,%s,%s,%s,%s,%s)",( room_id,event_id,transaction_id,total_amount,booking_date,id_number));

#print("<p> Customer Added Sucessfully</p>")


# Fetch all the rows using fetchall() method.

#cursor.execute("select CUSTOMER_TYPE,CUSTOMER_NAME,CUSTOMER_AGE from customer")
#data = cursor.fetchall()


db.commit()
db.close()

import urllib.request

fp = urllib.request.urlopen("file:///C:/Apache24/cgi-bin/RESERVATION_SERACH.HTML")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)




