import sys
import chilkat
import paramiko

def ppk_to_pem_convert():
  ssh_key = chilkat.CkSshKey()
  ssh_key_str = ssh_key.loadText("zimyo.ppk")
  success = ssh_key.FromPuttyPrivateKey(ssh_key_str)
  if (success != True):
    print(ssh_key.lastErrorText())
    sys.exit()

  bEncrypt = False
  unencryptedKeyStr = ssh_key.toOpenSshPrivateKey(bEncrypt)
  success = ssh_key.SaveText(unencryptedKeyStr,"unencrypted_zimyo.pem")
  if (success != True):
    print(ssh_key.lastErrorText())
    sys.exit()
  print("Done!")



def pmon_install():

  hostname = "13.232.123.248"
  username = "ec2-user"
  ssh_key_filename = "unencrypted_zimyo.pem"
  commands = [
    "pwd",
    "id",
    "uname -a",
    "df -h"
]
  ssh_client = paramiko.SSHClient()

  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  try:
    ssh_client.connect(hostname=hostname, username=username, key_filename=ssh_key_filename)
  except:
    print("[!] Cannot connect to the SSH Server")
    exit()
  for command in commands:
    print("="*50, command, "="*50)
    stdin, stdout, stderr = ssh_client.exec_command(command)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)

ppk_to_pem_convert
pmon_install
