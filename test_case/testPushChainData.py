'''
开放平台托管账户进行数据上链
'''
import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp,configDing

pushChainData_xls = common.get_xls('OpenApiCase.xlsx','push_chain_data')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*pushChainData_xls)
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

    def testPushChainData(self):

        self.url = common.get_url_from_xml('push_chain_data')
        # set url
        url = configHttp.set_url(self.url)
        print(url)

        # set headers
        configHttp.set_headers(self.headers)
        print(self.headers)

        # set data
        configHttp.set_data(self.data)
        print(self.data)

        # test interface
        try:
            self.return_json = configHttp.requests_by_method(self.method)
        except Exception as Ex:
            self.logger.exception(Ex)
            return

        common.checkResult(url,self.return_json,self.code)
    #     self.return_json = configHttp.requests_by_method(self.method)
    #     status_code = self.return_json.status_code
    #
    #     print(self.return_json.text)
    #     self.checkResult(url,status_code)
    #
    # def checkResult(self,url,status_code):
    #     '''
    #     check test result
    #     :return:
    #     '''
    #     re = []
    #     re.append(self.url)
    #     try:
    #         self.assertEqual(self.return_json.status_code, 200, '状态码不等于200，用例失败')
    #         self.info = json.loads(self.return_json.text)
    #         self.assertEqual(self.info['code'], self.code)
    #         re.append(self.info)
    #         self.logger.info(re)
    #     except Exception as Ex:
    #         re.append(Ex)
    #         self.logger.exception(re)
    #         configDing.dingmsg(url, status_code, Ex)

if __name__ == '__main__':
    unittest.main()