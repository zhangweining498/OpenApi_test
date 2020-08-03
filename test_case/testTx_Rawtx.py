'''
开放平台
Merchant API 发送交易 Rawtx
'''
import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp,configDing

TxRawtx_xls = common.get_xls('OpenApiCase.xlsx','tx_Rawtx')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*TxRawtx_xls)
class TXRawtx(unittest.TestCase):

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

    def testTxRawtx(self):

        self.url = common.get_url_from_xml('tx_Rawtx')
        # set url
        url = configHttp.set_url(self.url)
        print(url)

        # set headers
        headers = configHttp.set_headers(self.headers)
        print(headers)

        # test interface
        try:
            self.return_json = configHttp.requests_by_method(self.method)
        except Exception as Ex:
            self.logger.exception(Ex)
            return

        common.checkResult(url,self.return_json,self.code)
    #     self.return_json = configHttp.requests_by_method(self.method)
    #     status_code = self.return_json.status_code
    #     print(self.return_json.status_code)
    #     print(self.return_json.text)
    #     self.cheackresult(url,status_code)
    # def cheackresult(self,url, status_code):
    #     re = []
    #     re.append(self.url)
    #     try:
    #         self.assertEqual(self.return_json.status_code, 200, '状态码不等于200，用例失败')
    #         self.info = json.loads(self.return_json.text)
    #         re.append(self.info)
    #         self.logger.info(re)
    #     except Exception as Ex:
    #         re.append(Ex)
    #         self.logger.exception(re)
    #         configDing.dingmsg(url, status_code, Ex)


if __name__ == '__main__':
    unittest.main()