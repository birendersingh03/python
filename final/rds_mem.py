import boto3
import sys
from datetime import datetime, timedelta
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
    print( DB_Mem)
    print("value found")    

rds_class()

