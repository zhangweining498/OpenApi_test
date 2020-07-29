'''
开放平台区块链信息查询免费获取token
'''
import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp,configDing

token_xls = common.get_xls('OpenApiCase.xlsx','token')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*token_xls)
class Token(unittest.TestCase):

    def setParameters(self,case_name,method,headers,code,msg):

        self.case_name = str(case_name)
        self.method = str(method)
        self.headers = json.loads(headers)
        self.code = int(code)
        self.msg = str(msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testToken(self):
        self.url = common.get_url_from_xml('token')

        # set url
        url = configHttp.set_url(self.url)
        print(url)


        # set headers
        configHttp.set_headers(self.headers)
        print(self.headers)

        # test interface
        self.return_json = configHttp.requests_by_method(self.method)

        status_code = self.return_json.status_code
        print(self.return_json.text)

        self.checkResult(url,status_code)

    def checkResult(self,url,status_code):
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
            # configDing.dingmsg(url,status_code,Ex)




if __name__ == '__main__':
    unittest.main()
