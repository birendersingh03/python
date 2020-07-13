import boto3
import sys
from datetime import datetime, timedelta

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
 #   Unit='Percent'
        )

#print( type(response['Datapoints']) )
for mem in response['Datapoints']:
  if 'Average' in mem:
       print( mem['Average'] )



