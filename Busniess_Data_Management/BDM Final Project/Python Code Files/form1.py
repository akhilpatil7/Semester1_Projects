#!C:/Users/Ayush Jain/AppData/Local/Programs/Python/Python37-32/python.exe -u
print("Content-Type: text/html")    
print()

import cgi,cgitb
import urllib.request
#import os
#import webbrowser

cgitb.enable() #for debugging
form = cgi.FieldStorage()

customer_type = form.getvalue('customer_type')
customer_name = form.getvalue('customer_name')
customer_age = form.getvalue('customer_age')
id_type = form.getvalue('id_type')
id_number = form.getvalue('id_number')
payment_mode = form.getvalue('payment_mode')

dependent = form.getvalue('dependent')

import pymysql;

# Open connection to the database.
db = pymysql.connect("localhost","root","ayushjain03","HOTEL" )

# Start a cursor object using cursor() method
cursor = db.cursor()

#cursor.execute("select room_number from room where ROOM_TYPE =  (%s) and isAvailable=1",(room_type));
#room_num = cursor.fetchall()
#froom_num = room_num[0]
cursor.execute(" update reservation set ID_NUMBER = (%s) ",(id_number));



# Execute a SQL query using execute() method. This should return all the columns of heroes that use swords.
cursor.execute("INSERT INTO CUSTOMER (CUSTOMER_TYPE,CUSTOMER_NAME,CUSTOMER_AGE,ID_TYPE,ID_NUMBER,PAYMENT_MODE) VALUES (%s,%s,%s,%s,%s,%s)",( customer_type,customer_name,customer_age,id_type,id_number,payment_mode));
db.commit()
db.close()

import urllib.request

#if(dependent = "yes"): 
#	fp = urllib.request.urlopen("file:///C:/Apache24/cgi-bin/ADD_DEPENDENT.html")
#	mybytes = fp.read()
 #	mystr = mybytes.decode("utf8")
# 	fp.close()
#else(dependent = "no"): 
#	fp = urllib.request.urlopen("file:///C:/Apache24/cgi-bin/ADD_ROOM.html")
#	mybytes = fp.read()
#	mystr = mybytes.decode("utf8")
#	fp.close()




fp = urllib.request.urlopen("file:///C:/Apache24/cgi-bin/ADD_DEPENDENT.html")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)