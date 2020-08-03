# this file is used to illustrate how to read yaml file into Python
import yaml
import json
from jinja2 import Environment , FileSystemLoader




######################################################################

# with open('interface.yml') as f:
#      result = yaml.load(f,Loader=yaml.FullLoader) # read yaml file into python environment as dict format
#      # print(result) 
'''
{'hostname': 'leaf1', 'domain_name': 'wenhao.com', 
'vlans': [{'name': 'web', 'id': 10}, {'name': 'app', 'id': 20}, {'name': 'db', 'id': 30}]}
'''
######################################################################

with open('test1.json') as f:
     result = json.load(f) # read json file into python environment as dict format
     # print(result) 
'''
{'vendor': 'cisco', 'model': 'nxos', 'country': 'Singapore'}
'''
######################################################################

ENV = Environment(loader=FileSystemLoader('.'))
# template = ENV.get_template('interface_set.j2') # J2 dragon bone
# template = ENV.get_template('interface_set2.j2') # J2 dragon bone
# template = ENV.get_template('interface_set3.j2') # J2 dragon bone
# template = ENV.get_template('interface_set4.j2') # J2 dragon bone
# template = ENV.get_template('interface_set5.j2') # J2 dragon bone
template = ENV.get_template('interface_set6.j2') # J2 dragon bone


# the variable template is the file interface_set.j2
# the variable will be used in the upper variable template

# interface_parameter = {"name": "f1/0","vlan": 10,"description": "link_to_device","uplink": False}
# interface_parameter = ['f0/1','f0/2','f0/3']
# interface_parameter = {'f0/1':'des1','f0/2':'des2','f0/3':'des3'}

# interface_parameter = [
# {"name": "f1/0","vlan": 10,"description": "link_to_device","uplink": False},
# {"name": "f1/1","vlan": 11,"description": "link_to_server","uplink": False},
# {"name": "f1/2","vlan": 12,"description": "link_to_lb","uplink": True}]

# the variable mapping from template to interface_parameter
# the mapping parent is abc, which is like hook

######################################################################

with open('interface.yml') as f:
     #read yaml file into python environment as dict format
     interface_parameter = yaml.load(f,Loader=yaml.FullLoader) 
#the dragon bone is jinja2 file, the variable is yaml file
print(template.render(abc=interface_parameter))
