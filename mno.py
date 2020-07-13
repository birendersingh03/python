import boto3

ec2 = boto3.resource('ec2') 
ec3 = ec2.instances.all()
#for each in ec3:
#  print(each)
for each in ec3:
   print(each.each)
