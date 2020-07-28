'''
开放平台区块链信息查询查询token剩余次数
'''

import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp,configDing


count_xls = common.get_xls('OpenApiCase.xlsx','count')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*count_xls)
class count(unittest.TestCase):

    def setParameters(self,case_name,method,header,code,msg):

        self.case_name = str(case_name)
        self.method = str(method)
        self.header = json.loads(header)
        self.code = int(code)
        self.msg = str(msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testCount(self):

        self.url = common.get_url_from_xml('count')
        # set url
        url = configHttp.set_url(self.url)
        print(url)

        # set headers
        configHttp.set_headers(self.header)
        print(self.header)

        # test interface
        self.return_json = configHttp.requests_by_method(self.method)
        print(self.return_json)

        status_code = self.return_json.status_code
        print(self.return_json.text)

        self.checkResult(url, status_code)

    def checkResult(self, url, status_code):
        '''
        check test result
        :return:
        '''
        re = []
        re.append(self.url)
        try:
            self.assertEqual(self.return_json.status_code, 200, '状态码不等于200，用例失败')
            self.info = json.loads(self.return_json.text)
            self.assertEqual(self.info['code'], self.code)
            re.append(self.info)
            self.logger.info(re)
        except Exception as Ex:
            re.append(Ex)
            self.logger.exception(re)
            configDing.dingmsg(url, status_code, Ex)

if __name__ == '__main__':
    unittest.main()