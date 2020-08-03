import requests,json
import readConfig
from xlrd import open_workbook
from xlutils.copy import copy
import os,requests
import xml.etree.ElementTree as ET
import unittest
# from common import Log,configDing
localReadConfig = readConfig.ReadConfig()

proDir = readConfig.proDir
session = requests.session()



def get_headers():
    url = 'https://www.ddpurse.com/openapi/v1/signin'
    headers = {'device-id': localReadConfig.get_headers('device-id'),
               'fingerprint': localReadConfig.get_headers('fingerprint'),
               'user-agent': localReadConfig.get_headers('user-agent')}
    data = {'account':str(localReadConfig.get_user('username')),
            'client_id':'ce7ac9b5c4d54c7f9e71ed3e9a732c12',
            'form':'web',
            'mobile_prefix':'+86',
            'password':str(localReadConfig.get_user('password')),
            'provider':'local'}
    res = session.post(url,headers = headers,json=data)
    access_token = json.loads(res.text)['data']['access_token']
    headers['authorization'] = 'Bearer %s' % access_token
    # print(headers)
    return headers


def show_return_msg(response):
    '''
    show msg detail
    :param respomse:
    :return:
    '''
    url = response.url
    msg = response.text
    print('\n请求地址：'+url)
    print('\n请求返回值：'+'\n'+msg)

# ****************************** read testCase excel ********************************

def get_xls(xls_name, sheet_name):
    cls = []

    # get xls file’s path
    xlsPath = os.path.join(proDir,'test_file','case',xls_name)

    # open xls file
    file = open_workbook(xlsPath)

    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)

    # get one sheet's rows
    nrows = sheet.nrows

    # make case_name join in cls
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    # print(cls)
    return cls



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

# ****************************** check Result********************************
from common import Log,configDing

log = Log.MyLog.get_log()
logger = log.get_logger()


def checkResult(url,return_json,code):
    re = []
    re.append(url)
    status_code = return_json.status_code
    info = json.loads(return_json.text)

    try:
        if status_code == 200:
            re.append(info)
            if info['code'] == code:
                re.append(info)
                logger.info(re)

            else:
                logger.error(re)
                configDing.dingmsg(url,return_json,code)

        else:
            pass
    except Exception as Ex:
        re.append(Ex)
        logger.exception(re)





if __name__ == '__main__':
    url = 'https://www.ddpurse.com/platform/openapi/svdb/token'
    headers = {'appid': '0d158bc3605fffe30f7046f0c9c7e4bf', 'appsecret': 'e9943b6b167554fe555e39c1428c1d86'}
    return_json = requests.get(url,headers = headers)
    checkResult(url,return_json,'-132561')


