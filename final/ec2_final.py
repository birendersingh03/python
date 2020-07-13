import boto3
import sys
import datetime 
import MySQLdb

"""
Start Function for CPU

"""

def ec2_cpu(instancename, start_date, end_date ):
    client = boto3.client('cloudwatch')
    response = client.get_metric_statistics(
      Namespace='AWS/EC2',
      MetricName='CPUUtilization',
      Dimensions=[
                {
                'Name': 'InstanceId',
                'Value': instancename
                },
            ],
      StartTime=start_date - datetime.timedelta(seconds=600),
      EndTime=end_date,
      Period=86400,
      Statistics=[
                'Average',
            ],
      Unit='Percent'
        )


    CPU_All = [cpu['Average'] for cpu in response['Datapoints'] if 'Average' in cpu]
    Avg_CPU = sum(CPU_All) / len(CPU_All)
    return Avg_CPU
"""
End Function for CPU

"""



"""
Memory Utilization
"""

def ec2_mem(instancename, start_date, end_date):
    client = boto3.client('cloudwatch')
    response = client.get_metric_statistics(
      Namespace='System/Linux',
      MetricName='MemoryUtilization',
      Dimensions=[
                {
                'Name': 'InstanceId',
                'Value': instancename
                },
            ],
      StartTime=start_date - datetime.timedelta(seconds=600),
      EndTime=end_date,
      Period=86400,
     # Period=43200,
      Statistics=[
                'Average',
            ],
      Unit='Percent'
      )
    
    Mem_All = [mem['Average'] for mem in response['Datapoints'] if 'Average' in mem]
    Avg_Mem = sum (Mem_All) / len(Mem_All) 
    return Avg_Mem

"""
Memory Utilization Ends
"""


"""
Variabls
"""

Current_Date = datetime.datetime.today()   #end date
Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1) #start date
NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)


"""
DB Connection and Instance IDs
"""
ec = MySQLdb.connect("localhost","root","abc123","ec2" )
cursor = ec.cursor()
sql = """SELECT * FROM instance1"""
cursor.execute(sql)
ec.commit()
results = cursor.fetchall()
list_instance = []
for row in results:
    list_instance.append(row[0])
print(list_instance)
for instances in list_instance:
     cpu_avg = ec2_cpu(instances,Previous_Date, Current_Date )
     mem_avg = ec2_mem(instances,Previous_Date, Current_Date ) 
     cursor.execute("UPDATE instance1 SET cpu = %s, mem = %s WHERE instance_id = '%s' " % (cpu_avg, mem_avg, instances))
     ec.commit()

ec.close()

#print(ec2_mem('i-0e183772f29854fc9',Previous_Date, Current_Date))
"""
DB Part Ends Here
"""
