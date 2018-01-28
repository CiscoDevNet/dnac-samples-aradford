Some examples for PnP (Plug and Play)
=====================================

Shows how to upload/list/delete config files.  Same approach applies to image files.  
You would just need to change the namespace from "config" to "image"


```
$ ./list_files.py 
Getting https://sandboxdnac.cisco.com:8080/api/v1/file/namespace/config
name                          :fileFormat      fileSize   id                              
ap.json                       :application/json 103        107c6310-c31b-4c50-875b-0e4483115177
config.txt                    :text/plain      17         38d2d4c0-1a48-49dc-a249-c83b3fdfc7b1
```


There is also an example of listing of projects

```
$ ./list_projects.py 
Getting https://sandboxdnac.cisco.com:8080/api/v1/pnp-project
siteName         state           deviceCount  id                              
Melbourne        PRE_PROVISIONED            1 e553a1a7-57c8-451a-8041-2832853c2ec9
```

# Config Template Automation
The scripts in this directory can be used to automate the deployment of PnP configurations.  Note this is sample code,
designed for educational purposes.  It exposes most of the mechanics under the covers and covers each of the four steps 
in isolation to aid the learning process.

A number of the resources (filename, projectname, serialnumber) need to be unique on APIC-EM.  To allow multiple people to
use this lab with the sandbox controller, a function called "name_wrap" is used to append a 4 digit number to filename and project names.
This suffix is stored in the suffix.py file.  NOTE: Serial numbers need to be 11 digits, so name_wrap just replaces the last 4 digits of the
serial number.

## Build Templates
First step it to build configuration templates.  There are two files used here:  
- [work_files/templates/config_template.jnj](work_files/templates/config_template.jnj) is a jinja2 template file.
- [work_files/inventory.csv](work_files/inventory.csv) is a csv file with an entry for each network device.

The template is very simple, and just illustrates the use of variables.  These variables correspond to the column names of the csv file. In
this case "hostname" and "ipAddress" are two variables that come from the inventory file.
```
hostname {{hostName|lower}}

enable password cisco123
!
username cisco password 0 cisco123
no aaa new-model

int vlan 1
ip address {{ipAddress}} 255.255.255.0

!
end
```

The inventory file just contains entries for each netork device along with the variables to be instanciated.  You need to provide
"serialNumber", "platformId" and "site" for PnP rules.
```
hostName,serialNumber,platformId,site,ipAddress
sw01,12345678901,WS-C2960X-48FPD-L,Sydney,10.10.10.101
sw02,22345678901,WS-C2960X-48FPD-L,Sydney,10.10.10.102
sw03,32345678901,WS-C2960X-48FPD-L,Melbourne,10.10.10.103
```

to create the configuration files, run the "build_templates.py" command.
``` bash
$ ./build_templates.py 
{'platformId': 'WS-C2960X-48FPD-L', 'hostName': 'sw01', 'ipAddress': '10.10.10.101', 'site': 'Sydney', 'serialNumber': '12345678901'}
wrote file: work_files/configs/sw01-config-6130
{'platformId': 'WS-C2960X-48FPD-L', 'hostName': 'sw02', 'ipAddress': '10.10.10.102', 'site': 'Sydney', 'serialNumber': '22345678901'}
wrote file: work_files/configs/sw02-config-6130
{'platformId': 'WS-C2960X-48FPD-L', 'hostName': 'sw03', 'ipAddress': '10.10.10.103', 'site': 'Melbourne', 'serialNumber': '32345678901'}
wrote file: work_files/configs/sw03-config-6130
```

The output of these files is in the [work_files/configs](work_files/configs) directory.  There will be three files created. 
"6130" is the suffix that was created for me.

## Upload File

Once the config files have been create, they need to be uploaded to the controller.  "upload_file.py -a" will do this.
``` bash
$ ./upload_file.py -a
POST https://sandboxdnac.cisco.com:8080/api/v1/file/config
{
  "downloadPath": "/file/211dbd99-45c3-4569-98fc-42a282e2e393", 
  "name": "sw01-config-6130", 
  "sha1Checksum": "5a3c2140da71480762d2ca4224494bd577fd68ad", 
  "nameSpace": "config", 
  "fileFormat": "text/plain", 
  "fileSize": "150", 
  "id": "211dbd99-45c3-4569-98fc-42a282e2e393", 
  "md5Checksum": "83ccf6fa8655c3c3e1009d4e4143625d"
}
POST https://sandboxdnac.cisco.com:8080/api/v1/file/config
{
  "downloadPath": "/file/3ae7f9eb-77a1-4da1-a1fe-3d83aa1d5477", 
  "name": "sw02-config-6130", 
  "sha1Checksum": "c3bec74b7a94bcd7cf2d06bdbd529ee28106a83e", 
  "nameSpace": "config", 
  "fileFormat": "text/plain", 
  "fileSize": "150", 
  "id": "3ae7f9eb-77a1-4da1-a1fe-3d83aa1d5477", 
  "md5Checksum": "4e48aa8337ef4042fc533da508fa5ebd"
}
POST https://sandboxdnac.cisco.com:8080/api/v1/file/config
{
  "downloadPath": "/file/cc39185a-623a-4f07-a18e-a79533cd5e90", 
  "name": "sw03-config-6130", 
  "sha1Checksum": "fdd42407fbbc1a1ca0b17c094faf791666d166f1", 
  "nameSpace": "config", 
  "fileFormat": "text/plain", 
  "fileSize": "150", 
  "id": "cc39185a-623a-4f07-a18e-a79533cd5e90", 
  "md5Checksum": "f3cf86ae93fe3527ad27cd4ac5f4e1c0"
}

```

Notice that file operations are synchronous, i.e. the operation returns straight away.  Each file has a 32character UUID associated with it.
All other POST commands will be asynchronous.

You can use "list_files.py" to take a look at the files created.

## Create Projects
The next step is to create projects for the rules.  The "create_project.py -a" command does this.
``` bash
$ ./create_project.py -a
POST URL https://sandboxdnac.cisco.com:8080/api/v1/pnp-project
Creating project Melbourne-6130
Waiting for Task 1251de55-9aae-4442-922a-def5b408a5c7
{
  "rootId": "1251de55-9aae-4442-922a-def5b408a5c7", 
  "serviceType": "Ztd Service", 
  "isError": false, 
  "version": 1516265436224, 
  "startTime": 1516265436224, 
  "progress": "{\"message\":\"Success creating new site\",\"siteId\":\"166c48c8-b116-49f1-8dc7-7253d36282fb\"}", 
  "endTime": 1516265436306, 
  "id": "1251de55-9aae-4442-922a-def5b408a5c7"
}
POST URL https://sandboxdnac.cisco.com:8080/api/v1/pnp-project
Creating project Sydney-6130
Waiting for Task 8ebd5b0c-05e8-42d0-8394-5ac8c9b91710
{
  "rootId": "8ebd5b0c-05e8-42d0-8394-5ac8c9b91710", 
  "serviceType": "Ztd Service", 
  "isError": false, 
  "version": 1516265449545, 
  "startTime": 1516265449545, 
  "progress": "{\"message\":\"Success creating new site\",\"siteId\":\"b346dca8-dd2f-46e0-b04c-3a83bcfb1fb1\"}", 
  "endTime": 1516265449579, 
  "id": "8ebd5b0c-05e8-42d0-8394-5ac8c9b91710"
}

```
The project creation calls are asynchronous, meaning that a task_id is returned and I need to poll the task_id to determine
if the creation was successful.

## Create Rules
I now create rules for the devices.  This will associate the configuration file created in step #1, uploaded in Step #2, in a rule
 defined in the project created in step #3.  "create_rule.py -a" will create the rules on APIC-EM.

``` bash
$ ./create_rule.py -a
Getting https://sandboxdnac.cisco.com:8080/api/v1/file/namespace/config
GET: https://sandboxdnac.cisco.com:8080/api/v1/pnp-project?siteName=Sydney-6130&offset=1&limit=10
POST URL https://sandboxdnac.cisco.com:8080/api/v1/pnp-project/b346dca8-dd2f-46e0-b04c-3a83bcfb1fb1/device
[
  {
    "platformId": "WS-C2960X-48FPD-L", 
    "hostName": "sw01", 
    "serialNumber": "12345676130", 
    "configId": "211dbd99-45c3-4569-98fc-42a282e2e393", 
    "pkiEnabled": true
  }
]
Waiting for Task 10a07cc2-b8a1-4673-bcad-7a6219975064
{
  "rootId": "10a07cc2-b8a1-4673-bcad-7a6219975064", 
  "serviceType": "Ztd Service", 
  "isError": false, 
  "version": 1516265502279, 
  "startTime": 1516265502279, 
  "progress": "{\"message\":\"Success creating new site device(rule)\",\"ruleId\":\"65360a72-70eb-4beb-8e3e-b60a13a5ed14\"}", 
  "endTime": 1516265502523, 
  "id": "10a07cc2-b8a1-4673-bcad-7a6219975064"
}
GET: https://sandboxdnac.cisco.com:8080/api/v1/pnp-project?siteName=Sydney-6130&offset=1&limit=10
POST URL https://sandboxdnac.cisco.com:8080/api/v1/pnp-project/b346dca8-dd2f-46e0-b04c-3a83bcfb1fb1/device
[
  {
    "platformId": "WS-C2960X-48FPD-L", 
    "hostName": "sw02", 
    "serialNumber": "22345676130", 
    "configId": "3ae7f9eb-77a1-4da1-a1fe-3d83aa1d5477", 
    "pkiEnabled": true
  }
]
Waiting for Task 2c8d970c-7ea0-461e-86f6-198c1bf54f13
{
  "rootId": "2c8d970c-7ea0-461e-86f6-198c1bf54f13", 
  "serviceType": "Ztd Service", 
  "isError": false, 
  "version": 1516265519091, 
  "startTime": 1516265519091, 
  "progress": "{\"message\":\"Success creating new site device(rule)\",\"ruleId\":\"8741fb5d-59b4-42c0-aeee-4cd8b9a2a337\"}", 
  "endTime": 1516265519252, 
  "id": "2c8d970c-7ea0-461e-86f6-198c1bf54f13"
}
GET: https://sandboxdnac.cisco.com:8080/api/v1/pnp-project?siteName=Melbourne-6130&offset=1&limit=10
POST URL https://sandboxdnac.cisco.com:8080/api/v1/pnp-project/166c48c8-b116-49f1-8dc7-7253d36282fb/device
[
  {
    "platformId": "WS-C2960X-48FPD-L", 
    "hostName": "sw03", 
    "serialNumber": "32345676130", 
    "configId": "cc39185a-623a-4f07-a18e-a79533cd5e90", 
    "pkiEnabled": true
  }
]
Waiting for Task 234290c5-1ca4-40b0-a6cf-0f4c56b0fa4d
{
  "rootId": "234290c5-1ca4-40b0-a6cf-0f4c56b0fa4d", 
  "serviceType": "Ztd Service", 
  "isError": false, 
  "version": 1516265535256, 
  "startTime": 1516265535256, 
  "progress": "{\"message\":\"Success creating new site device(rule)\",\"ruleId\":\"4a7b6a33-035c-4e8c-b822-27a9e83db84d\"}", 
  "endTime": 1516265535323, 
  "id": "234290c5-1ca4-40b0-a6cf-0f4c56b0fa4d"
}


```
This is slightly more complex as I need to do a REST API call to map the project_name to a project_id and the file_name to file_id.
Again the call is async, so i need to poll the task.

You can look at the controller to see the project and the rules that have been created.  This is using a hidden URL for the unsupported UI.
![uniq](pnp-screenshot.png?raw=true "uniq")
Similarly you can "list_project.py" to see the list of projects or "list_project.py Sydney-6130" to see the rules for a project.

## Clean up
Once you are done, you can run the "delete_file.py -a" and the "delete_project.py -a" to remove the files and the projects from the controller.
NOTE: you do not have to remove the rules as the arguments provided to the "delete_project" API call will remove all rules.

## Next Steps
This is an educational example where the steps have been broken out for clarity.  This does require some extra work in the code, as I have to lookup 
file and project names to resolve their UUID, where as an "all-in-one" version would keep the UUID of the resource that has been created.

 

