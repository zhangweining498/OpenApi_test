"""
开放平台非托管账户（打点钱包用户）数据上链
"""
import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp

pushChainDataDotWallet_xls = common.get_xls('OpenApiCase.xlsx','push_chain_data_dotwallet')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*pushChainDataDotWallet_xls)
class pushChainDataDotWallet(unittest.TestCase):

    def setParameters(self,case_name,method,coin_type,email,data,data_type,sign_callback,code,msg):

        self.case_name = str(case_name)
        self.method = str(method)
        self.coin_type = str(coin_type)
        self.email = str(email)
        self.data = str(data)
        self.data_type = int(data_type)
        self.sign_callback = str(sign_callback)
        self.code = str(code)
        self.msg = str(msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testPushChainDataDotWallet(self):

        self.url = common.get_url_from_xml('push_chain_data_dotwallet')
        # set url
        configHttp.set_url(self.url)


        # set data
        data = {'coin_type': self.coin_type,
                'email':self.email,
                'data': self.data,
                'data_type': self.data_type,
                'sign_callback':self.sign_callback}
        configHttp.set_data(data)

        # test interface
        self.return_json = configHttp.request_post_not_headers()

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