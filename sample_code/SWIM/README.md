## Introduction
SWIM (SoftWare Image Management) API allow for the distribution and activation of software 
images on Cisco network devices.

This service is hosted on DNA Center.  Images are stored locally on DNAC and https is used to distribute them.
The only exception is WLAN controllers, that require and external SFTP server.

## list_images.py
provides a list of all of the images on DNAC

## Distribute.py
takes a tag and an imagename.
Any devices with the tag associated with them will have the image distributed to them

## delete.py
used to delete an image from a device.  

## Notes:
I have not created an activate script, but that is almost identical to distribution
