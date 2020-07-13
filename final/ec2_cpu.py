import boto3
import sys
from datetime import datetime, timedelta

"""
Value return from portal. For the month we want to show data.
  Value returned would be Month and year and I would be adding 01(start of each month)
"""

Request_Date = "7 2020"
Req_Mon, Req_Yrs = Request_Date.split()
Current_Date = datetime.now()


if int(Req_Mon) == int(Current_Date.month):
   print("months are same")
else:
   print("months are not same")


if int(Req_Mon) == int(Current_Date.month):
   starttime = datetime(int(Req_Yrs), int(Req_Mon), 01)
   endtime = datetime.now()
else:
   starttime = datetime(int(Req_Yrs), int(Req_Mon), 1)
   endtime = datetime(int(Req_Yrs), int(Req_Mon), 30)


#print(Req_Mon)
#print(Req_Yrs)
#print(Current_Date.month)
#print(Current_Date.year)
#print(Current_Date.day)
#print(starttime)
#print(endtime)






def cpuUtilization():
  client = boto3.client('cloudwatch')
  response = client.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[
                {
                'Name': 'InstanceId',
                'Value': 'i-073ee9bef5b894131'
                },
            ],
    StartTime=datetime(2020, 7, 01) - timedelta(seconds=600),
    EndTime=datetime(2020, 7, 07),
    Period=86400,
    Statistics=[
                'Average',
            ],
    Unit='Percent'
        )

  CPU_All = [cpu['Average'] for cpu in response['Datapoints'] if 'Average' in cpu]
  #Avg_CPU = sum(CPU_All) / len(CPU_All)
  return CPU_All
  #clist = []
  #for cpu in response['Datapoints']:
  #  if 'Average' in cpu:
  #      clist.append( cpu['Average'] )
  #print(clist)

print(cpuUtilization())
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
#print(numberOfDays(2019, 2))





