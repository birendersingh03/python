import boto3
import sys
from datetime import datetime, timedelta

def cpuUtilization():
  client = boto3.client('cloudwatch')
  response = client.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='MemoryUtilization',
    Dimensions=[
                {
                'Name': 'InstanceId',
                'Value': 'i-073ee9bef5b894131'
                },
            ],
    StartTime=datetime(2020, 6, 01) - timedelta(seconds=600),
    EndTime=datetime(2020, 6, 30),
    Period=86400,
    Statistics=[
                'Average',
            ],
    Unit='Percent'
        )
  clist = []
  for cpu in response['Datapoints']:
    if 'Average' in cpu:
        clist.append( cpu['Average'] )
  print(clist)
#tt = []
#tt = cpuUtilization()
#for each in tt:
#    print(each)

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
print(numberOfDays(2019, 2))





