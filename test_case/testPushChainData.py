'''
开放平台托管账户进行数据上链
'''
import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp

pushChainData_xls = common.get_xls('OpenApiCase.xlsx','push_chain_data')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*pushChainData_xls)
class getHostedAccount(unittest.TestCase):

    def setParameters(self,case_name,method,app_id,app_secret,coin_type,data,data_type,code,msg):

        self.case_name = str(case_name)
        self.method = str(method)
        self.app_id = str(app_id)
        self.app_secret = str(app_secret)
        self.coin_type = str(coin_type)
        self.data =str(data)
        self.data_type = int(data_type)
        self.code = str(code)
        self.msg = str(msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testPushChainData(self):

        self.url = common.get_url_from_xml('push_chain_data')
        # set url
        configHttp.set_url(self.url)

        # set headers
        headers = {'appid': self.app_id,
                   'appsecret': self.app_secret}
        configHttp.set_headers(headers)

        # set data
        data = {'coin_type': self.coin_type,
                'data': self.data,
                'data_type': self.data_type}
        configHttp.set_data(data)

        # test interface
        self.return_json = configHttp.request_json_post()

        print(self.return_json.text)

    def checkResult(self):
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

if __name__ == '__main__':
    unittest.main()