#!C:/Users/Ayush Jain/AppData/Local/Programs/Python/Python37-32/python.exe -u

print("Content-Type: text/html")    
print()


import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
unique_id = form.getvalue('unique_id')
print(unique_id)

import pymysql;
# Open connection to the database
db = pymysql.connect("localhost","root","ayushjain03","HOTEL" )

# Start a cursor object using cursor() method
cursor = db.cursor()


cursor.execute(" SELECT * FROM RESERVATION WHERE ID_NUMBER  = (%s)",( unique_id));
data = cursor.fetchall()
#attribute_names = [i[0] for i in cursor.description]

print("<table border = '1'>")
print("<tr>")

print("<th>EVENT_ID</th>")
print("<th>TRANSACTION_ID</th>")
print("<th>TOTAL_AMOUNT</th>")
print("<th>BOOKING_DATE</th>")
print("<th>ID_NUMBER</th>")
print("<th>ROOM_NUMBER</th>")

print("</tr>")
for each in data:
	print("<tr>")
	print("<td>{0}</td>".format(each[0]))
	print("<td>{0}</td>".format(each[1]))
	print("<td>{0}</td>".format(each[2]))
	print("<td>{0}</td>".format(each[3]))
	print("<td>{0}</td>".format(each[4]))
	print("<td>{0}</td>".format(each[5]))
	print("</tr>")
print("</table>")



#db.commit()

db.close()
