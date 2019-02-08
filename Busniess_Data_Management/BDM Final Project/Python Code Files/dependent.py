#!C:/Users/Ayush Jain/AppData/Local/Programs/Python/Python37-32/python.exe -u

print("Content-Type: text/html")    
print()


import cgi,cgitb
cgitb.enable() #for debugging

form = cgi.FieldStorage()
dependent_name = form.getvalue('dependent_name')
dependent_age = form.getvalue('dependent_age')
deptid_type = form.getvalue('deptid_type')
deptid_number = form.getvalue('deptid_number')


import pymysql;
# Open connection to the database
db = pymysql.connect("localhost","root","ayushjain03","HOTEL" )

# Start a cursor object using cursor() method
cursor = db.cursor()

cursor.execute(" INSERT INTO DEPENDENT (DEPENDENT_NAME,DEPENDENT_AGE,DEPTID_TYPE,DEPTID_NUMBER) VALUES (%s,%s,%s,%s)",( dependent_name,dependent_age,deptid_type,deptid_number));



db.commit()

db.close()



import urllib.request

fp = urllib.request.urlopen("file:///C:/Apache24/cgi-bin/ADD_ROOM.HTML")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)