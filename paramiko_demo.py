
import paramiko
import getpass

ipaddr = raw_input("IP Address: ")
user = raw_input("Username: ")
pswd = getpass.getpass("Password: ")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ipaddr,
            port=22,
            username=user,
            password=pswd)
stdin, stdout, sterr = ssh.exec_command('show system users ')
output = stdout.readlines()
type(output)
print ''.join(output)


