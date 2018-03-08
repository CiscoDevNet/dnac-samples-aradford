#!/usr/bin/env python
from __future__ import print_function
import jtextfsm as textfsm


sample="""
CAM Utilization for ASIC# 0                      Max            Used
                                             Masks/Values    Masks/values

 Unicast mac addresses:                      16604/16604        22/22
 IPv4 IGMP groups + multicast routes:         1072/1072          2/2
 IPv4 unicast directly-connected routes:      2048/2048          0/0
 IPv4 unicast indirectly-connected routes:    1024/1024         34/34
 IPv6 Multicast groups:                       1072/1072         11/11
 IPv6 unicast directly-connected routes:      2048/2048          0/0
 IPv6 unicast indirectly-connected routes:    1024/1024          3/3
 IPv4 policy based routing aces:               504/504          13/13
 IPv4 qos aces:                                504/504          54/54
 IPv4 security aces:                           600/600          78/78
 IPv6 policy based routing aces:                20/20            8/8
 IPv6 qos aces:                                500/500          45/45
 IPv6 security aces:                           600/600          17/17

Note: Allocation of TCAM entries per feature uses
a complex algorithm. The above information is meant
to provide an abstract view of the current TCAM utilization
"""
template = open("show_platform_tcam_utilization.textfsm")
re_table = textfsm.TextFSM(template)
print (re_table)
fsm_results = re_table.ParseText(sample)
print (fsm_results)
