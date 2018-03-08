This directory contains utilities for using the "CommandRunner"
API on DNAC.

It requires python3 for the uniq library. 
.

I also recommend using virtualenv.  Use the following commands as examples

```buildoutcfg
virtualenv -p python3 env
source env/bin/activate
```

To install:

```buildoutcfg
pip install -r requirements.txt
```

You will need to edit the dnac_config.py file to change your credentials.
NOTE:  You can also use environment variables for these parameters too.
   DNAC, DNAC_USER, DNAC_PASSWORD will be looked at first.
   export DNAC_PASSWORD="mysecrete" for example

To run:

There are some examples in the Examples file.
Note your IP address and tags will likely be different to those in the example.

```buildoutcfg
$ ./cmd_runner.py --ip 10.10.22.70 --command "show clock"
tag: None
['show clock']
[
  {
    "commandResponses": {
      "FAILURE": {},
      "BLACKLISTED": {},
      "SUCCESS": {
        "show clock": "20:44:40.509 UTC Sat Feb 25 2017"
      }
    },
    "deviceUuid": "5abffd04-f981-46be-8640-789af2e910d6"
  }
]

```

or for human friendly output (along with device selection using a tag)

```buildoutcfg

$ ./cmd_runner.py --tag switch --commands 'show power inline' --table --fsm
tag: switch
['show power inline']
IP,Name,Command,Module,available,used,remaining
10.10.22.70,cat_9k_2.abc.inc,show power inline,1,560.0,0.0,560.0
10.10.22.66,cat_9k_1.abc.inc,show power inline,1,560.0,0.0,560.0

```