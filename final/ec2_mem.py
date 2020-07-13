import boto3
import sys
from datetime import datetime, timedelta, date

client = boto3.client('cloudwatch')
response = client.get_metric_statistics(
    Namespace='System/Linux',
    MetricName='MemoryUtilization',
    Dimensions=[
                {
                'Name': 'InstanceId',
                'Value': 'i-0e183772f29854fc9'
                },
            ],
    StartTime=datetime(2020, 6, 30) - timedelta(seconds=600),
    EndTime=datetime.utcnow(), 
    Period=86400,
    Statistics=[
                'Average',
            ],
    Unit='Percent'
        )
Mem_All = [mem['Average'] for mem in response['Datapoints'] if 'Average' in mem]
Avg_Mem =sum (Mem_All) / len(Mem_All)
print(Avg_Mem)

#print( type(response['Datapoints']) )
for cpu in response['Datapoints']:
  if 'Average' in cpu:
       print( cpu['Average'] )
