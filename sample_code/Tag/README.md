## A tool to manuiplate device tags
This tool allows manipulation of device tags.  A device can have many tags.  Tags are useful for grouping devices for 
* software distribution
* software activation
* command_runner
* template execution

Tags can also be applied to interfaces.

## Examples

### List of tags
just run tag.py by itself.  It will show you the tags and their ID

```buildoutcfg
$ ./tag.py 
https://sandboxdnac.cisco.com:8080/api/v1/tag
TagName                                           :TagId       
SydneyDevice                                      :7dd451c2-65ce-4bef-9b1c-bb521e68d688
InterestingDevice                                 :d1bce9c7-39c2-4db8-9227-b96891aaaca5
```

### Add a tag to a device
The --addtag option will add a tag to a device.  The tag will be created if it does not exist.

```buildoutcfg
$ ./tag.py --addtag switch 10.10.22.70 10.10.22.66

Adding tag:switch
https://sandboxdnac.cisco.com:8080/api/v1/tag
{'response': [{'id': '7dd451c2-65ce-4bef-9b1c-bb521e68d688', 'tag': 'SydneyDevice'}], 'version': '1.0'}
Creating tag: switch
Waiting for Task 036f8aa5-a95d-4d3a-8fd8-87a0e34ac846
{'version': 1516757537943, 'startTime': 1516757537943, 'serviceType': 'Inventory service', 'id': '036f8aa5-a95d-4d3a-8fd8-87a0e34ac846', 'endTime': 1516757537998, 'rootId': '036f8aa5-a95d-4d3a-8fd8-87a0e34ac846', 'isError': False, 'progress': '9f996415-10f3-4b34-8d33-c800702984ef'}
https://sandboxdnac.cisco.com:8080/api/v1/network-device/ip-address/10.10.22.70
Waiting for Task 22fa48af-6359-4425-9496-35bd5e240312
{'version': 1516757546609, 'startTime': 1516757546609, 'serviceType': 'Inventory service', 'id': '22fa48af-6359-4425-9496-35bd5e240312', 'endTime': 1516757546624, 'rootId': '22fa48af-6359-4425-9496-35bd5e240312', 'isError': False, 'progress': 'Tag switch on resource 74b69532-5dc3-45a1-a0dd-6d1d10051f27 of resource type network-device added successfully'} 

https://sandboxdnac.cisco.com:8080/api/v1/network-device/ip-address/10.10.22.66
Waiting for Task 156c460e-cce8-4ac6-b369-f327143331fe
{'version': 1516757555487, 'startTime': 1516757555487, 'serviceType': 'Inventory service', 'id': '156c460e-cce8-4ac6-b369-f327143331fe', 'endTime': 1516757555600, 'rootId': '156c460e-cce8-4ac6-b369-f327143331fe', 'isError': False, 'progress': 'Tag switch on resource 6d3eaa5d-bb39-4cc4-8881-4a2b2668d2dc of resource type network-device added successfully'} 


```

### List devices with a certain tag
Just use the --tag <tag> option

Shows a list of the deviceId and the IP address of the device with the tag "switch"
```buildoutcfg
$ ./tag.py --tag switch 
https://sandboxdnac.cisco.com:8080/api/v1/tag/association?tag=switch&resourceType=network-device
https://sandboxdnac.cisco.com:8080/api/v1/network-device/74b69532-5dc3-45a1-a0dd-6d1d10051f27
https://sandboxdnac.cisco.com:8080/api/v1/network-device/6d3eaa5d-bb39-4cc4-8881-4a2b2668d2dc
[('74b69532-5dc3-45a1-a0dd-6d1d10051f27', '10.10.22.70'), ('6d3eaa5d-bb39-4cc4-8881-4a2b2668d2dc', '10.10.22.66')]
```
