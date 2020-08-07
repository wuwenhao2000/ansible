import pprint
import napalm
import sys
driver = napalm.get_network_driver("ios")
with driver(sys.argv[1],'cisco','cisco') as device:
     print(device.get_facts())
     # print(device.get_interfaces_counters())