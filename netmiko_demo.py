
from netmiko import ConnectHandler
import getpass


ipaddr = raw_input("IP Address: ")
user = raw_input("Username: ")
# Prompt the user for a password without echoing
pswd = getpass.getpass("Password: ")

my_device = {
    'host': ipaddr,
    'username': user,
    'password': pswd,
    'device_type': 'juniper',
}

net_connect = ConnectHandler(**my_device)
output = net_connect.send_command("show system users ")
net_connect.disconnect()
print output

