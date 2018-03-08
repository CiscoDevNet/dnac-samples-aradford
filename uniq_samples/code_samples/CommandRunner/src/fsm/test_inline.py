#!/usr/bin/env python
from __future__ import print_function
import jtextfsm as textfsm

sample='''
Module   Available     Used     Remaining
          (Watts)     (Watts)    (Watts)
------   ---------   --------   ---------
1           390.0        0.0       390.0
Interface Admin  Oper       Power   Device              Class Max
                            (Watts)
--------- ------ ---------- ------- ------------------- ----- ----
Gi1/0/1   auto   off        0.0     n/a                 n/a   30.0
Gi1/0/2   auto   off        0.0     n/a                 n/a   30.0
Gi1/0/3   auto   off        0.0     n/a                 n/a   30.0
Gi1/0/4   auto   off        0.0     n/a                 n/a   30.0
Gi1/0/5   auto   off        0.0     n/a                 n/a   30.0
Gi1/0/47  auto   off        0.0     n/a                 n/a   30.0
Gi1/0/48  auto   off        0.0     n/a                 n/a   30.0

Module   Available     Used     Remaining
          (Watts)     (Watts)    (Watts)
------   ---------   --------   ---------
2           390.0        0.0       390.0
Interface Admin  Oper       Power   Device              Class Max
                            (Watts)
--------- ------ ---------- ------- ------------------- ----- ----
Gi2/0/1   auto   off        0.0     n/a                 n/a   30.0
Gi2/0/2   auto   off        0.0     n/a                 n/a   30.0
Gi2/0/3   auto   off        0.0     n/a                 n/a   30.0
Gi2/0/4   auto   off        0.0     n/a                 n/a   30.0
Gi2/0/5   auto   off        0.0     n/a                 n/a   30.0
Gi2/0/6   auto   off        0.0     n/a                 n/a   30.0
Interface Admin  Oper       Power   Device              Class Max
                            (Watts)
--------- ------ ---------- ------- ------------------- ----- ----
Gi2/0/7   auto   off        0.0     n/a                 n/a   30.0
Gi2/0/8   auto   off        0.0     n/a                 n/a   30.0
'''


template = open("show_power_inline.textfsm")
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(sample)
print (fsm_results)

