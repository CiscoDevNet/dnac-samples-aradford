# Sample code for DNAC REST API

### PnP (Plug and Play)
Sample scripts showing how to 
- create a configuration file from a jinja template.
- upload/list/delete configuration files (can be extended to images)
- upload/list/delete projects
- create/delete rules

### Top5
5 scripts illustrating 5 basic API
- network-device
- interface
- license
- host
- path trace


### NOTE
Make sure you install the requirements.txt
`pip install -r requirements.txt`

in particular pyOpenSSL, ndg-httpsclient as DNAC is very specific about the ciphers that can be used to connect to it.
