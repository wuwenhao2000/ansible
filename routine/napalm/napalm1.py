import pprint
import napalm
import sys
driver = napalm.get_network_driver("ios")
with driver(sys.argv[1],'cisco','cisco') as device:
     print(device.get_facts())
     device.load_replace_candidate(filename='r1.cfg') 
     # print(device.compare_config())