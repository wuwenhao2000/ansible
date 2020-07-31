# this file is used to illustrate how to read yaml file into Python
import yaml
import json
from jinja2 import Environment , FileSystemLoader

######################################################################

with open('test1.yml') as f:
     result = yaml.load(f) # read yaml file into python environment as dict format
     print(result) 
     # print(type(result))

'''
{'hostname': 'leaf1', 'domain_name': 'wenhao.com', 
'vlans': [{'name': 'web', 'id': 10}, {'name': 'app', 'id': 20}, {'name': 'db', 'id': 30}]}
'''
######################################################################

with open('test1.json') as f:
     result = json.load(f) # read json file into python environment as dict format
     print(result) 
     # print(type(result))
'''
{'vendor': 'cisco', 'model': 'nxos', 'country': 'Singapore'}
'''
######################################################################

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template('interface_set.j2') # J2 dragon bone
# the variable template is the file interface_set.j2

# the variable will be used in the upper variable template
interface_parameter = {
     "name": "f1/0",
     "vlan": 10,
     "description": "link_to_device",
     "uplink": False}

# the variable mapping from template to interface_parameter
# the mapping parent is abc
print(template.render(abc=interface_parameter))