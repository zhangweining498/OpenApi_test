'''
开放平台刷新access_token
'''
import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp,configDing

refreshToken_xls = common.get_xls('OpenApiCase.xlsx','refresh_access_token')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*refreshToken_xls)
class refresh_access_token(unittest.TestCase):

    def setParameters(self,case_name,method,app_id,refresh_token,code,msg):
        self.case_name = str(case_name)
        self.method = str(method)
        self.app_id = str(app_id)
        self.refresh_token = str(refresh_token)
        self.code= int(code)
        self.msg = (msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testRefreshToken(self):
        # 获取refresh_token
        content = configHttp.access_token()
        if self.refresh_token == '':
            self.refresh_token = content['data']['refresh_token']
            print(self.refresh_token)

        self.url = common.get_url_from_xml('refresh_access_token')

        # set url
        url = configHttp.set_url(self.url)
        print(url)

        # set params
        data = {'app_id':self.app_id,
                  'refresh_token':self.refresh_token}
        configHttp.set_data(data)

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
