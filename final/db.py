import boto3
import sys
import datetime
import MySQLdb

db = MySQLdb.connect("localhost","root","abc123","ec2" )

cursor = db.cursor()
sql_select_query = """select * from db1"""
cursor.execute(sql_select_query)
record = cursor.fetchall()
print(record)

sql_update_query = """UPDATE db1 SET mem = '50' WHERE instance_name = 'database-1-instance-1'"""
cursor.execute("""UPDATE db1 SET mem = '60' WHERE instance_name = 'database-1-instance-1'""")
db.commit()
print("Record Updated successfully ")
print("After updating record ")
cursor.execute(sql_select_query)
record = cursor.fetchall()
print(record)
