'''
开放平台区块链信息查询
根据高度查询区块信息
'''
import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp,configDing

height_xls = common.get_xls('OpenApiCase.xlsx','height')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*height_xls)
class height(unittest.TestCase):

    def setParameters(self,case_name,method,headers,data,code,msg):
        self.case_name = str(case_name)
        self.method =str(method)
        self.headers = json.loads(headers)
        self.data = json.loads(data)
        self.code = int(code)
        self.msg = str(msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testHeight(self):
        # set url
        self.url = common.get_url_from_xml('height')
        url = configHttp.set_url(self.url)

        # set headers
        configHttp.set_headers(self.headers)
        print(self.headers)

        # set params
        configHttp.set_data(self.data)
        print(self.data)

        # test interface
        self.return_json = configHttp.requests_by_method(self.method)

        status_code = self.return_json.status_code
        print(status_code)

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