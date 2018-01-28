#!/usr/bin/env python
from __future__ import print_function
import sys
import json
import logging
from argparse import ArgumentParser, REMAINDER
from util import get_url, post_and_wait, delete_and_wait

def show_tags():
    response = get_url("tag")
    print('{0:50}:{1:12}'.format('TagName','TagId'))
    for tag in response['response']:
        print ('{0:50}:{1:12}'.format(tag['tag'], tag['id']))

def tag_mapping(tag):
    '''

    :param tag: tag to look for
    :return: all device ID matching that tag
    '''
    if tag is None:
        return []
    response = get_url('tag/association?tag={0}&resourceType=network-device'.format(tag))

    return [association['resourceId'] for association in response['response']]

def device2id(device):
    response = get_url('network-device/ip-address/{0}'.format(device))
    return response['response']['id']

def id2device(deviceId):
    response = get_url('network-device/{0}'.format(deviceId))
    return response['response']['managementIpAddress']

def tag2id(tagName):
    response = get_url('tag')
    print (response)
    return[tag['id'] for tag in response['response'] if tag['tag'].encode('UTF-8') == tagName or tag['tag'] == tagName][0]

def assign_tag(tag, device):
    deviceId = device2id(device)
    payload={
        "resourceId": deviceId,
        "resourceType" : "network-device",
        "tag": tag
    }
    response = post_and_wait('tag/association', payload)
    print(response, '\n')

def remove_tag(tagId,device):
    deviceId = device2id(device)
    response = delete_and_wait('tag/association/{0}?resourceType=network-device&resourceId={1}'.format(tagId, deviceId))
    print (response)

def delete_tag(tag, devices):
    #tag/association/{{tagId}}?resourceType=network-device&resourceId={{deviceId}}
    print("\nDeleting tag:{0}".format(tag))
    tagId = tag2id(tag)

    for device in devices:
        remove_tag(tagId, device)

def create_tag(tag):
    print ("Creating tag: {0}".format(tag))
    payload = { "tag" : tag }
    response = post_and_wait('tag', payload)
    print (response)

def add_tag(tag, devices):
    print("\nAdding tag:{0}".format(tag))

    try:
        tagId = tag2id(tag)
    except IndexError as e:
        create_tag(tag)
    for device in devices:
        assign_tag(tag, device)

if __name__ == "__main__":
    parser = ArgumentParser(description='Select options.')
    parser.add_argument('--tag', type=str, required=False,
                        help="show devices with a tag")

    parser.add_argument('--addtag', type=str, required=False,
                        help="add tag to devices")
    parser.add_argument('--deletetag', type=str, required=False,
                        help="delete tag from devices")
    parser.add_argument('-v', action='store_true',
                        help="verbose")
    parser.add_argument('rest', nargs=REMAINDER)
    args = parser.parse_args()
    if args.v:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    if args.tag:
        ids = tag_mapping(args.tag)
        ips = map(id2device, ids)
        print( list(zip(ids,ips)))

    elif args.addtag:
        add_tag(args.addtag, args.rest)
    elif args.deletetag:
        delete_tag(args.deletetag, args.rest)
    else:
        show_tags()
