'''
开放平台查询托管余额
'''
import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp

getHostedBalance_xls = common.get_xls('OpenApiCase.xlsx','get_hosted_account_balance')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*getHostedBalance_xls)
class getHostedAccount(unittest.TestCase):

    def setParameters(self,case_name,method,headers,data,code,msg):

        self.case_name = str(case_name)
        self.method = str(method)
        self.headers = json.loads(headers)
        self.data = json.loads(data)
        self.code = str(code)
        self.msg = str(msg)



    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testGetHostedAccount(self):

        self.url = common.get_url_from_xml('get_hosted_account_balance')
        # set url
        configHttp.set_url(self.url)

        # set headers

        configHttp.set_headers(self.headers)

        # set data
        configHttp.set_data(self.data)

        # test interface
        self.return_json = configHttp.requests_by_method(self.method)

        print(self.return_json.text)
        self.checkResult()

    def checkResult(self):
        '''
        check test result
        :return:
        '''
        try:
            self.assertEqual(self.return_json.status_code, 200, '状态码不等于200，用例失败')
            self.info = json.loads(self.return_json.text)
            self.assertEqual(self.info['code'], self.code)
            self.assertIn(self.msg, self.info['msg'])
            self.logger.info(self.info)
        except Exception as Ex:
            self.logger.exception(Ex)


if __name__ == '__main__':
    unittest.main()