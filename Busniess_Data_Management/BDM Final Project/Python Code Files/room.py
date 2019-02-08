#!C:/Users/Ayush Jain/AppData/Local/Programs/Python/Python37-32/python.exe -u

print("Content-Type: text/html")    
print()


import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
room_type = form.getvalue('room_type')
booking_date = form.getvalue('myDate')

#print (room_type)
#print (booking_date)

import pymysql;
# Open connection to the database
db = pymysql.connect("localhost","root","ayushjain03","HOTEL" )

# Start a cursor object using cursor() method
cursor = db.cursor()

#cursor.execute("SELECT * FROM ROOM WHERE isAvailable = 1");
#data = cursor.fetchall()

#query_room_num = "select room_number from room where room_type (%s) and isAvailable=1"

cursor.execute("select room_number from room where ROOM_TYPE =  (%s) and isAvailable=1",(room_type));
room_num = cursor.fetchall()
froom_num = room_num[0]
cursor.execute(" update room set isAvailable = 0 where room_number = (%s)",(froom_num[0]));

#print(froom_num[0])

# Execute a SQL query using execute() method. This should return all the columns of heroes that use swords.

#cursor.execute("INSERT INTO RESERVATION (TOTAL_AMOUNT,BOOKING_DATE) VALUES (%s,%s)",(100,booking_date ))

if(room_type == "single"): cursor.execute(" INSERT INTO RESERVATION (TOTAL_AMOUNT,BOOKING_DATE,ROOM_NUMBER) VALUES (%s,%s,%s)",(100,booking_date, froom_num[0]));
elif(room_type == "double") : cursor.execute(" INSERT INTO RESERVATION (TOTAL_AMOUNT,BOOKING_DATE,ROOM_NUMBER) VALUES (%s,%s,%s)",(250,booking_date, froom_num[0] ));
elif room_type == "deluxe": cursor.execute(" INSERT INTO RESERVATION (TOTAL_AMOUNT,BOOKING_DATE,ROOM_NUMBER) VALUES (%s,%s,%s)",(400,booking_date , froom_num[0]));
elif room_type == "event": cursor.execute(" INSERT INTO RESERVATION (TOTAL_AMOUNT,BOOKING_DATE,ROOM_NUMBER) VALUES (%s,%s,%s)",(200,booking_date , froom_num[0]));


#cursor.execute(" INSERT INTO RESERVATION (BOOKING_DATE) VALUES (%s)",(booking_date ))
db.commit()

query = "select TRANSACTION_ID,TOTAL_AMOUNT,BOOKING_DATE from reservation;"
cursor.execute(query)
data = cursor.fetchall()

#print("<table border = '1'>")
#print("<tr>")
#print("<th>TOTAL_AMOUNT</th>")
#print("<th>BOOKING_DATE</th>")
#print("<th>ROOM_NUMBER</th>")
#print("</tr>")
#for each in data:
#	print("<tr>")
#	print("<td>{0}</td>".format(each[0]))
#	print("<td>{0}</td>".format(each[1]))
#	print("<td>{0}</td>".format(each[2]))
#	print("</tr>")
# print("</table>")


# Fetch all the rows using fetchall() method.
#data = cursor.fetchall()

# disconnect from server
db.close()



import urllib.request

fp = urllib.request.urlopen("file:///C:/Apache24/cgi-bin/EVENT_DETAILS.HTML")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)

