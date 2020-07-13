



cat <<'EOF' >/tmp/xyz.sh
#!/bin/bash
##### Find out hostname and take decision based on that
os_release=`cat /etc/os-release | grep -i "Name" | head -1 | awk -F'=' '{print $2}'`

if [[ ${os_release}  =~ "Amazon"  ]]
then
  os_name="Amazon"
elif [[ ${os_release}  =~ "Ubuntu" ]]
then
  os_name="Ubuntu"
elif [[ ${os_release}  =~ "redhat" || ${os_release}  =~ "Centos" ]]
then
  os_name="Common"
else
  os_name="Unknown"
fi

# use case statement to make decision for rental
case $os_name in
   "Amazon") 
            echo "installing required packages" 
            sudo yum install -y perl-Switch perl-DateTime perl-Sys-Syslog perl-LWP-Protocol-https perl-Digest-SHA.x86_64 wget
            sudo mkdir /opt/cloud-watch
            sudo wget https://aws-cloudwatch.s3.amazonaws.com/downloads/CloudWatchMonitoringScripts-1.2.2.zip -P /opt/cloud-watch 
            sudo unzip /opt/cloud-watch/CloudWatchMonitoringScripts-1.2.2.zip -d /opt/cloud-watch 
            sudo rm /opt/cloud-watch/CloudWatchMonitoringScripts-1.2.2.zip 
            cd /opt/cloud-watch/aws-scripts-mon
            sudo  echo "*/5 * * * * /opt/cloud-watch/aws-scripts-mon/mon-put-instance-data.pl --mem-used-incl-cache-buff --mem-util --disk-space-util --disk-path=/ --from-cron" >>   /var/spool/cron/root
            sudo /opt/cloud-watch/aws-scripts-mon/mon-put-instance-data.pl --mem-used-incl-cache-buff --mem-util --mem-used --mem-avail --disk-space-util --disk-space-avail --disk-path=/
            ;;
            echo "sent logs to cloudwatch"

   "Ubuntu")
            echo "installing required packages"
            sudo apt-get update
            sudo apt-get install unzip
            sudo apt-get install libwww-perl libdatetime-perl wget
            sudo mkdir /opt/cloud-watch
            sudo wget https://aws-cloudwatch.s3.amazonaws.com/downloads/CloudWatchMonitoringScripts-1.2.2.zip -P /opt/cloud-watch 
            sudo unzip /opt/cloud-watch/CloudWatchMonitoringScripts-1.2.2.zip -d /opt/cloud-watch 
            sudo rm /opt/cloud-watch/CloudWatchMonitoringScripts-1.2.2.zip 
            cd /opt/cloud-watch/aws-scripts-mon
            sudo  echo "*/5 * * * * /opt/cloud-watch/aws-scripts-mon/mon-put-instance-data.pl --mem-used-incl-cache-buff --mem-util --disk-space-util --disk-path=/ --from-cron" >>   /var/spool/cron/root
            sudo /opt/cloud-watch/aws-scripts-mon/mon-put-instance-data.pl --mem-used-incl-cache-buff --mem-util --mem-used --mem-avail --disk-space-util --disk-space-avail --disk-path=/
            ;;
            echo "sent logs to cloudwatch"

   "Common") 

            echo "installing required packages"

            sudo yum install perl-DateTime perl-CPAN perl-Net-SSLeay perl-IO-Socket-SSL perl-Digest-SHA gcc wget -y
            sudo yum install zip unzip
            sudo mkdir /opt/cloud-watch
            sudo wget https://aws-cloudwatch.s3.amazonaws.com/downloads/CloudWatchMonitoringScripts-1.2.2.zip -P /opt/cloud-watch 
            sudo unzip /opt/cloud-watch/CloudWatchMonitoringScripts-1.2.2.zip -d /opt/cloud-watch 
            sudo rm /opt/cloud-watch/CloudWatchMonitoringScripts-1.2.2.zip 
            cd /opt/cloud-watch/aws-scripts-mon
            sudo  echo "*/5 * * * * /opt/cloud-watch/aws-scripts-mon/mon-put-instance-data.pl --mem-used-incl-cache-buff --mem-util --disk-space-util --disk-path=/ --from-cron" >>   /var/spool/cron/root
            sudo /opt/cloud-watch/aws-scripts-mon/mon-put-instance-data.pl --mem-used-incl-cache-buff --mem-util --mem-used --mem-avail --disk-space-util --disk-space-avail --disk-path=/
            ;;

            echo "sent logs to cloudwatch"
   "Unknown") echo "For $os_name";;


   *) echo "Sorry, I can not get a $os_name  for you!";;


esac

EOF


su root  -c 'chmod +x /tmp/xyz.sh'
su root -c 'sh /tmp/xyz.sh'


