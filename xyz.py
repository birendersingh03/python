import boto3
import MySQLdb
import sys
from datetime import datetime, timedelta, date

db = MySQLdb.connect("localhost","root","abc123","ec2" )
cursor = db.cursor()
#cursor.execute("SELECT VERSION()")
#data = cursor.fetchone()
#print "Database version : %s " % data
sql = "SELECT * FROM instance1"
cursor.execute(sql)
results = cursor.fetchall()
print(type(results))

list_instance = []
#tup_instance = ( row[0]
for row in results:
    list_instance.append(row[0])
  #  print(row[0])

    #list_instance = list(row[0])

#print(tup_instance)
print(list_instance)

db.close()
sdate = datetime.now()
print(sdate)

today = date.today() 
yesterday = today - timedelta(days = 1) 
print(yesterday)


def rds_cpu( ):
    client = boto3.client('cloudwatch')
    response = client.get_metric_statistics(
      Namespace='AWS/RDS',
      MetricName='CPUUtilization',
      Dimensions=[
                {
                'Name': 'DBInstanceIdentifier',
                'Value': 'database-1-instance-1'
                },
            ],
      StartTime=starttime - timedelta(seconds=600),
      EndTime=endtime,
      Period=86400,
      Statistics=[
                'Average',
            ],
      Unit='Percent'
        )


    CPU_All = [cpu['Average'] for cpu in response['Datapoints'] if 'Average' in cpu]
    Avg_CPU = sum(CPU_All) / len(CPU_All)
    return Avg_CPU

