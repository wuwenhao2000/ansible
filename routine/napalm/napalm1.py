import pprint
import napalm
import sys
# optional_args = {}
# optional_args['global_delay_factor'] = 4
driver = napalm.get_network_driver("ios")
# with driver(sys.argv[1],'cisco','cisco',optional_args=optional_args) as device:
with driver(sys.argv[1],'cisco','cisco') as device:
     # print(device.get_facts())
     # print(device.get_interfaces_ip())
     # print(device.get_arp_table())
     print(device.get_bgp_neighbors())
     # device.load_replace_candidate(filename='r1.txt') 
     # # print(device.compare_config())