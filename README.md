# DNA Center API Samples
Digital Network Architecture Center (DNAC) is Cisco's controller for campus and WAN environments.

It provides automation and assurance capabilities for routers, switches and wireless LAN.

DNAC exposes a set of northbound API which are used by this collection of scripts and tools.

## Getting Started
Clone this repository.
`git clone https://github.com/CiscoDevNet/dnac-samples-aradford.git`

## sample_code
has examples of python requests code for the following API:
- PnP (Plug and Play) : shows how to create, upload, delete files, projects and rules
- SWIM Software Image Mananagement tools
- Tag  tools for managing device tags.  Required for SWIM
- Top5 : examples of utilities for:
    - network-device: list all of the devices on the controller and their attributes
    - interface: show the interface utilization of a switch (number of interfaces in use, and the hosts/vlan attached)
    - license: shows license information for a device
    - host: find_my_host.  shows where a host is connected in the network
    - path_trace: shows the path between two hosts on the network

## tools
contains a postman collection for interacting with an always on sandbox.  You can change the variables to point to your
own DNAC server.

## uniq_samples
uniq is a client library for DNAC.  It abstracts the REST API endpoints and allows you to interact with python objects.

I have modified the uniq library from APIC-EM to work with DNAC.  This is not the officially supported version.

- uniq contains the client library code.  You will need to install this to use the examples.
- code_samples contains examples for PnP and other simple use cases


