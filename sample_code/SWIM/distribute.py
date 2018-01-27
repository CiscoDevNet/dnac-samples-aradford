#!/usr/bin/env python
from __future__ import print_function
import sys
import json
import logging
from argparse import ArgumentParser

from util import get_url, post_and_wait, tagmapping

def imageName2id(imageName):
    #
    url='image/importation?name={0}'.format(imageName)
    response = get_url(url)
    return response['response'][0]['imageUuid']

def distribute(imageUuid, *deviceIdList):

    body = []
    for deviceId in deviceIdList:
        body.append({"deviceUuid": deviceId, "imageUuid": imageUuid})

    url = 'image/distribution'
    response = post_and_wait(url, body)
    print(response)
    taskId = response['id']
    detail = get_url('image/task?taskUuid={0}'.format(taskId))
    print (json.dumps(detail, indent=2))

def validate(imageUuid, *deviceIdList):
    '''
    quick check to make sure the image should be distributed to the device
    :param imageUuid:
    :param deviceIdList:
    :return:
    '''
    image = get_url('image/importation/{0}'.format(imageUuid))
    print(image['response']['family'])
    for deviceId in deviceIdList:
        device = get_url('network-device/{0}'.format(deviceId))
        print(device['response']['series'])

if __name__ ==  "__main__":
    parser = ArgumentParser(description='Select options.')
    parser.add_argument('--tag', type=str, required=False,
                        help="devices that match this tag")
    parser.add_argument('--image', type=str, required=False,
                        help="devices that match this tag")

    args = parser.parse_args()

    deviceIds = tagmapping(args.tag)
    imageId = imageName2id(args.image)
    validate(imageId, *deviceIds)
    distribute(imageId, *deviceIds)

