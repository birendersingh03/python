import boto3
import sys
from datetime import datetime, timedelta

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
    StartTime=datetime(2020, 6, 01) - timedelta(seconds=600),
    EndTime=datetime(2020, 6, 30),
    Period=86400,
    Statistics=[
                'Average',
            ],
    Unit='Percent'
        )

#print( type(response['Datapoints']) )
for cpu in response['Datapoints']:
  if 'Average' in cpu:
       print( cpu['Average'] )
