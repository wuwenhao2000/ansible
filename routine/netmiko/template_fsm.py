#this object is used to parse the string into structured#
from ntc_templates.parse import parse_output

str1 = '''Cisco IOS Software, 2600 Software (C2691-ADVENTERPRISEK9-M), Version 12.4(5a), RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2006 by Cisco Systems, Inc.
Compiled Sat 14-Jan-06 05:00 by alnguyen

ROM: ROMMON Emulation Microcode
ROM: 2600 Software (C2691-ADVENTERPRISEK9-M), Version 12.4(5a), RELEASE SOFTWARE (fc3)

R1 uptime is 1 day, 5 hours, 34 minutes
System returned to ROM by unknown reload cause - suspect boot_data[BOOT_COUNT] 0x0, BOOT_COUNT 0, BOOTDATA 19
System image file is "tftp://255.255.255.255/unknown"


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco 2691 (R7000) processor (revision 0.1) with 187392K/9216K bytes of memory.
Processor board ID XXXXXXXXXXX
R7000 CPU at 160MHz, Implementation 39, Rev 2.1, 256KB L2, 512KB L3 Cache
3 FastEthernet interfaces
DRAM configuration is 64 bits wide with parity enabled.
55K bytes of NVRAM.

Configuration register is 0x2102'''
ver = parse_output(platform="cisco_ios", command="show ver", data=str1)
print(ver)