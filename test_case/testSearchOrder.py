'''
开放平台 支付功能  订单支付
查询订单状态
'''


import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp,configDing

searchOrder_xls = common.get_xls('OpenApiCase.xlsx','search_order')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*searchOrder_xls)
class hash(unittest.TestCase):

    def setParameters(self,case_name,method,data,code,msg):
        self.case_name = str(case_name)
        self.method =str(method)
        self.data = json.loads(data)
        self.code = int(code)
        self.msg = str(msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testSearchOrder(self):
        # set url
        self.url = common.get_url_from_xml('search_order')
        url = configHttp.set_url(self.url)

        # set params
        configHttp.set_data(self.data)
        print(self.data)

        # test interface
        self.return_json = configHttp.requests_by_method(self.method)
        print(self.return_json.text)
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