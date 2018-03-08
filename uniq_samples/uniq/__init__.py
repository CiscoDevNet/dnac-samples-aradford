# -*- coding: utf-8 -*-

"""
uniq is a Python API client library for Cisco's Application Policy Infrastructure Controller
Enterprise Module (APIC-EM) Northbound APIs.

*** Description ***

The APIC-EM Northbound Interface is the only API that you will need to control your network
programmatically. The API is function rich and provides you with an easy-to-use, programmatic
control of your network elements, interfaces, and hosts.

The APIC-EM API provides you with the ability to think about your network at a higher policy
level rather than how to implement that policy. When you use the APIC-EM API, your applications
will make network policy decisions, which will then be implemented by the APIC-EM Controller
through its Southbound Interfaces. Thus you tell the network what you want (i.e., the policy)
and the controller figures out how to implement that policy for you.

The APIC-EM API is REST based and thus you will discover and control your network using HTTP
protocol with HTTP verbs (i.e., GET, POST, PUT, and DELETE) with JSON syntax.

This package provides a handle to this rich API library in an easy to consume fashion.

*** Usage ***

Import the package and make an API call.

    >>> from uniq.apis.nb.client_manager import NbClientManager

    >>> client = NbClientManager(
    ...     server="1.1.1.1",
    ...     username="username",
    ...     password="password",
    ...     connect=True)

    >>> # NorthBound API call to get all users
    >>> user_list_result = client.user.getUsers()

    >>> # Serialize the model object to a python dictionary
    >>> users = client.serialize(user_list_result)

    >>> print(users)

:copyright: (c) 2016 by Cisco Systems, see Copyright for more details.
:license: Apache 2.0, see LICENSE for more details.
"""


__title__ = 'uniq'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2016 Cisco Systems'

__version__ = '2.0.10'
__first_release_date__ = '2016.1.16'
