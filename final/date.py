import datetime


Current_Date = datetime.datetime.today()
print ('Current Date: ' + str(Current_Date))




Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
print ('Previous Date: ' + str(Previous_Date))

NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
print ('Next Date: ' + str(NextDay_Date))
