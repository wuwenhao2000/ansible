import pprint
import napalm
import sys
driver = napalm.get_network_driver("ios")
device = driver(hostname=sys.argv[1],username="cisco",password="cisco")
device.open()
print(device.get_config())