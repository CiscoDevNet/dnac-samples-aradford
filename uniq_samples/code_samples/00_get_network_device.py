from login import login
import logging
#logging.basicConfig(level=logging.DEBUG)
# connect to DNAC using the login module

dnac = login()

# networkdevice -> NetworkdeviceAPI class.  getAllNetworkDeices is a method in this class
network_devices  = dnac.networkdevice.getAllNetworkDevice()

# print a heading
print('{ip:<16s} {name:<16s}'.format(ip="IP Address", name="Device Name"))

# print each of the nework devices.  network_devices is a list of objects with attributes, not a python dict
for network_device in network_devices.response:
    print('{ip:<16s} {name:<16s}'.format(ip=network_device.managementIpAddress, name=network_device.hostname))
