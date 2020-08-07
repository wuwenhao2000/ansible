#this object is used to parse the string into structured#
from ntc_templates.parse import parse_output

str1 = '''abc'''
ver = parse_output(platform="cisco_ios", command="show ver", data=str1)
print(ver)