#!/usr/bin/python
# coding=utf-8

import json,os
import requests
import xml.etree.ElementTree as ET
import readConfig

proDir = readConfig.proDir

# ****************************** read interfaceURL xml ********************************
def get_url_from_xml(name):
    """
    By name get url from interfaceURL.xml
    :param name: interface's url name
    :return: url
    """
    url_list = []
    url_path = os.path.join(proDir, 'test_file', 'interfaceURL.xml')
    tree = ET.ElementTree(file=url_path)
    root = tree.getroot()
    for u in root.iter('url'):
        if u.get('name')== name:
            for c in u.iter():
                url_list.append(c.text)
    url = '/' + '/'.join(url_list[1:])
    # print(url)
    return url


























