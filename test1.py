import sys
import json
from netmiko import ConnectHandler
# def print1(s):
#      print ("I am back {}".format(s))

device = ConnectHandler(device_type="cisco_ios",ip=sys.argv[1],
username=sys.argv[2],password=sys.argv[3])

output = device.send_command('show version')

print (output)


# if __name__=="__main__":
#      print1(sys.argv[1])