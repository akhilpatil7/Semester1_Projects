#!C:/Users/Ayush Jain/AppData/Local/Programs/Python/Python37-32/python.exe -u

print("Content-Type: text/html")    
print()


import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
event_name = form.getvalue('event_name')
event_location = form.getvalue('event_location')
num_of_participants = form.getvalue('num_of_participants')
event_notes = form.getvalue('event_notes')
event_date = form.getvalue('myDate')
event_type = form.getvalue('event_type')


import pymysql;
# Open connection to the database
db = pymysql.connect("localhost","root","ayushjain03","HOTEL" )

# Start a cursor object using cursor() method
cursor = db.cursor()

cursor.execute(" INSERT INTO EVENT (EVENT_NAME,EVENT_LOCATION,NUM_OF_PARTICIPANTS,EVENT_DATE,EVENT_NOTES,EVENT_TYPE) VALUES (%s,%s,%s,%s,%s,%s)",( event_name,event_location,num_of_participants,event_date,event_notes,event_type));

db.commit()
db.close()


import urllib.request

fp = urllib.request.urlopen("file:///C:/Apache24/cgi-bin/reservation.html")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)