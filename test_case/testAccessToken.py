"""
开放平台获取access_token接口自动化测试
"""
import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp,configDing

access_token_xls = common.get_xls('OpenApiCase.xlsx','access_token')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*access_token_xls)
class access_token(unittest.TestCase):

    def setParameters(self,case_name,method,app_id,secret,code01,code,msg):
        self.case_name = str(case_name)
        self.method = str(method)
        self.app_id = str(app_id)
        self.secret = str(secret)
        self.code01 = str(code01)
        self.code = int(code)
        self.msg = str(msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testAccessToken(self):
        '''
        使用code获取token
        :return:
        '''
        # set code
        code = configHttp.code()

        self.url = common.get_url_from_xml('access_token')

        # set url
        url = configHttp.set_url(self.url)
        print(url)


        # set data
        data = {'app_id':self.app_id,
                'secret':self.secret,
                'code':code}
        configHttp.set_data(data)
        print(data)

        # test interface
        try:
            self.return_json = configHttp.requests_by_method(self.method)
        except Exception as Ex:
            self.logger.exception(Ex)
            return

        common.checkResult(url,self.return_json,self.code)
    #     self.return_json = configHttp.requests_by_method(self.method)
    #     status_code = self.return_json.status_code
    #     self.checkResult(url,status_code)
    #
    # def checkResult(self,url,status_code):
    #     '''
    #             check test result
    #             :return:
    #             '''
    #     re = []
    #     re.append(self.url)
    #     try:
    #         self.assertEqual(self.return_json.status_code, 200, '状态码不等于200，用例失败')
    #         self.info = json.loads(self.return_json.text)
    #         self.assertEqual(self.info['code'], self.code_res)
    #         self.assertIsNotNone(self.info['data']['access_token'])
    #         self.assertIsNotNone(self.info['data']['refresh_token'])
    #         self.assertIn(self.msg, self.info['msg'])
    #         re.append(self.info)
    #         self.logger.info(re)
    #     except Exception as Ex:
    #         re.append(Ex)
    #         self.logger.exception(re)
    #         configDing.dingmsg(url, status_code, Ex)



if __name__ == '__main__':
    unittest.main()
