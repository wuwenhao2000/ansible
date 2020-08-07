import pprint
import napalm
import sys
optional_args = {}
optional_args['global_delay_factor'] = 4
driver = napalm.get_network_driver("ios")
with driver(sys.argv[1],'cisco','cisco',optional_args=optional_args) as device:
     print(device.get_facts())
     device.load_replace_candidate(filename='r1.cfg') 
     # print(device.compare_config())