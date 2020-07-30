import sys
import json
from netmiko import ConnectHandler
# def print1(s):
#      print ("I am back {}".format(s))

device = ConnectHandler(device_type="cisco_ios",ip=sys.argv[1],
username=sys.argv[3],password=sys.argv[4])

output = device.send_command(sys.argv[2])

print (output)


# if __name__=="__main__":
#      print1(sys.argv[1])