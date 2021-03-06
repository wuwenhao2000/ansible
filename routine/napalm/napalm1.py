import pprint
import napalm
import sys
import pprint
pp = pprint.PrettyPrinter(width=200)
# optional_args = {}
# optional_args['global_delay_factor'] = 4
driver = napalm.get_network_driver("ios")
pp.pprint(dir(driver))
# with driver(sys.argv[1],'cisco','cisco',optional_args=optional_args) as device:
with driver(sys.argv[1],'cisco','cisco') as device:
     # print(device.get_facts())
     # print(device.get_interfaces_ip())
     # print(device.get_arp_table())
     pp.pprint(device.get_bgp_neighbors())
     # device.load_replace_candidate(filename='r1.txt') 
     # # print(device.compare_config())
'''
output of pp.pprint(dir(driver))
['__class__',
 '__del__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__enter__',
 '__eq__',
 '__exit__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_canonical_int',
 '_check_file_exists',
 '_commit_handler',
 '_create_tmp_file',
 '_discard_config',
 '_discover_file_system',
 '_file_prompt_quiet',
 '_gen_full_path',
 '_gen_rollback_cfg',
 '_get_bgp_route_attr',
 '_get_vlan_all_ports',
 '_get_vlan_from_id',
 '_get_vrfs',
 '_inline_tcl_xfer',
 '_is_vss',
 '_load_candidate_wrapper',
 '_netmiko_close',
 '_netmiko_open',
 '_normalize_compare_config',
 '_normalize_merge_diff',
 '_normalize_merge_diff_incr',
 '_scp_file',
 '_send_command',
 '_send_command_postprocess',
 '_xfer_file',
 'bgp_time_conversion',
 'cli',
 'close',
 'commit_config',
 'compare_config',
 'compliance_report',
 'connection_tests',
 'dest_file_system',
 'discard_config',
 'get_arp_table',
 'get_bgp_config',
 'get_bgp_neighbors',
 'get_bgp_neighbors_detail',
 'get_config',
 'get_environment',
 'get_facts',
 'get_firewall_policies',
 'get_interfaces',
 'get_interfaces_counters',
 'get_interfaces_ip',
 'get_ipv6_neighbors_table',
 'get_lldp_neighbors',
 'get_lldp_neighbors_detail',
 'get_mac_address_table',
 'get_network_instances',
 'get_ntp_peers',
 'get_ntp_servers',
 'get_ntp_stats',
 'get_optics',
 'get_probes_config',
 'get_probes_results',
 'get_route_to',
 'get_snmp_information',
 'get_users',
 'get_vlans',
 'is_alive',
 'load_merge_candidate',
 'load_replace_candidate',
 'load_template',
 'open',
 'parse_uptime',
 'ping',
 'post_connection_tests',
 'pre_connection_tests',
 'rollback',
 'traceroute']


output of pp.pprint(device.get_bgp_neighbors())
{'global': {'peers': {'2.2.2.2': {'address_family': {'ipv4 unicast': {'accepted_prefixes': 1, 'received_prefixes': 1, 'sent_prefixes': 2}},
                                  'description': '',
                                  'is_enabled': True,
                                  'is_up': True,
                                  'local_as': 100,
                                  'remote_as': 100,
                                  'remote_id': '2.2.2.2',
                                  'uptime': 23659},
                      '3.3.3.3': {'address_family': {'ipv4 unicast': {'accepted_prefixes': 1, 'received_prefixes': 1, 'sent_prefixes': 2}},
                                  'description': '',
                                  'is_enabled': True,
                                  'is_up': True,
                                  'local_as': 100,
                                  'remote_as': 100,
                                  'remote_id': '3.3.3.3',
                                  'uptime': 23655}},
            'router_id': '192.168.1.1'}}
'''