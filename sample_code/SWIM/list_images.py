#!/usr/bin/env python
from __future__ import print_function
import sys
import json
import logging
from argparse import ArgumentParser

from util import get_url, post_and_wait

def get_images(imageName=None):
    if imageName:
        url='image/importation?imageName={0}'.format(imageName)
    else:
        url='image/importation'
    response = get_url(url)
    print('{0:45}{1:15}{2:18}{3:15}{4}'.format('Name','Version','FileSize','Family','importSourceType'))
    for image in response['response']:
        print('{0:45}{1:15}{2:18}{3:15}{4}'.format(image['name'], image['version'], image['fileSize'],
                                                   image['family'], image['importSourceType']))

if __name__ ==  "__main__":
    parser = ArgumentParser(description='Select options.')
    parser.add_argument('--pattern', type=str, required=False,
                        help="show devices that match pattern")

    args = parser.parse_args()
    get_images(args.pattern)
