import boto3
import sys
from datetime import datetime, timedelta, date
import MySQLdb


"""
DB Connection and Instance IDs
"""
db = MySQLdb.connect("localhost","root","abc123","ec2" )
cursor = db.cursor()
sql = "SELECT * FROM instance1"
cursor.execute(sql)
results = cursor.fetchall()
list_instance = []
for row in results:
    list_instance.append(row[0])
db.close()

"""
DB Part Ends Here
"""




def numberOfDays(y, m):
    leap = 0
    if y% 400 == 0:
         leap = 1
    elif y % 100 == 0:
         leap = 0
    elif y% 4 == 0:
         leap = 1
    if m==2:
         return 28 + leap
    list = [1,3,5,7,8,10,12]
    if m in list:
         return 31
    return 30


Request_Date = "7 2020"
Req_Mon, Req_Yrs = Request_Date.split()
Current_Date = datetime.now()

if int(Req_Mon) == int(Current_Date.month):
   starttime = datetime(int(Req_Yrs), int(Req_Mon), 01)
   endtime = datetime.now()
else:
   starttime = datetime(int(Req_Yrs), int(Req_Mon), 1)
   endtime = datetime(int(Req_Yrs), int(Req_Mon), numberOfDays(int(Req_Yrs), int(Req_Mon)))


print(starttime)
print(endtime)

today = date.today()
yesterday = today - timedelta(days = 1)
print(yesterday)


def rds_cpu(dbinstancename, ):
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

#print(rds_cpu()) 

def rds_class():
    db_class = {'db.r5.large': 16, 
                'db.r5.xlarge': 32,
                'db.r5.2xlarge': 64,
                'db.r5.4xlarge': 128,
                'db.r5.12xlarge': 384,
                'db.r5.24xlarge': 768,
                'db.r4.large': 15,
                'db.r4.xlarge': 30,
                'db.r4.2xlarge': 61,
                'db.r4.4xlarge': 122,
                'db.r4.8xlarge': 244,
                'db.r4.16xlarge': 488
               }
    rds = boto3.client('rds')
    response = rds.describe_db_instances(
    DBInstanceIdentifier='database-1-instance-1'
       )
    DB_Class = [totl['DBInstanceClass'] for totl in response['DBInstances']]

    for key,value in db_class.items():
        if DB_Class[0] == key:
          DB_Mem = value
          break
    return DB_Mem

print(rds_class())






def rds_mem():
    client = boto3.client('cloudwatch')
    response = client.get_metric_statistics(
      Namespace='AWS/RDS',
      MetricName='FreeableMemory',
      Dimensions=[
                {
                'Name': 'DBInstanceIdentifier',
                'Value': 'cloudapphrms-instance-1'
                },
            ],
      StartTime=datetime(2020, 7, 01) - timedelta(seconds=600),
      EndTime=datetime(2020, 7, 30),
      Period=86400,
      Statistics=[
                'Average',
            ],
      Unit='Bytes'
      )
    Total_Mem = rds_class()
    Mem_All = [mem['Average'] for mem in response['Datapoints'] if 'Average' in mem]
    Mem_GB = [i/(1024*1024*1024) for i in Mem_All]
    Mem_Percent = [(( Total_Mem - i )/Total_Mem)*100 for i in Mem_GB]

    Avg_Mem =sum (Mem_Percent) / len(Mem_Percent) 
    return Avg_Mem

print(rds_mem())

