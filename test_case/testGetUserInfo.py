'''
开放平台获取用户信息接口
'''
import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp,configDing


get_user_info_xls = common.get_xls('OpenApiCase.xlsx','get_user_info')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*get_user_info_xls)
class get_user_info(unittest.TestCase):

    def setParameters(self,case_name,method,access_token,code,msg):
        self.case_name = str(case_name)
        self.method = str(method)
        self.access_token = str(access_token)
        self.code = int(code)
        self.msg = str(msg)

    def setUp(self):

        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testGetUserInfo(self):

        self.url = common.get_url_from_xml('get_user_info')

        # 获取access_token
        content = configHttp.access_token()
        self.access_token = content['data']['access_token']
        print(self.access_token)

        # set url
        url = configHttp.set_url(self.url)
        print(url)

        # set data
        data = {'access_token':self.access_token}
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
    #     print(self.return_json.text)
    #
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
    #         self.assertIn(self.msg, self.info['msg'])
    #         re.append(self.info)
    #         self.logger.info(re)
    #     except Exception as Ex:
    #         re.append(Ex)
    #         self.logger.exception(re)
    #         configDing.dingmsg(url, status_code, Ex)



if __name__ == '__main__':
    unittest.main()
