import boto3
ec2 = boto3.resource('ec2')
  
for instance in ec2.instances.all():
     print(
         #"Id: {0}\nRegion: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\nLaunchTime: {6}\nBlock_Devices: {7}\n".format(
         #instance.id, instance.placement, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state, instance.launch_time, instance.block_device_mapping
       #  dir(instance)
       instance.load


     )
