# Ansible_self-learning project

python programming

Dear everyone,

There is the simple project based on Ansible to automate the network setup and operation

The network topology is in the pic of "lab_pic.jpg", the f1/0 of each device is OOB network 10.0.0.0/24 connecting to the master server which is a Centos7 server

The 10.0.1.0/24 is used in production network, in this case we use ISIS, BGP, MPLS. All these config is configed by Ansible 

There are 2 branches master and second, they have different variable provisioning functions, master is based on variable file function, second is based on subdirectory function

For both ones, if the big project the subdirectory function is better cause different config portions can be managed correspondingly. Otherwise, file function can bring the integrated config

If you also are interested in or have other good suggestions, please kindly let me know

routine/netmiko/netmiko1 is based on standard netmiko

routine/netmiko/netmiko1a is based on netmiko with template_fsm

routine/netmiko/template_fsm is based on template_fsm parsing for string

########
In the first step I define all the functions in integrated playbook which is 
high efficient, however the sharing is not good enough

In the second step I define the role and to split the partition configs into
the corresponding roles, which makes the whole structure more sharing and clear 

pb_push_if.yml, is used to config interface specially
pb_push_bgp.yml, is used to config BGP specially
pb_push_isis.yml, is used to config ISIS specially
pb_push_all.yml, is used to summary above ones together
