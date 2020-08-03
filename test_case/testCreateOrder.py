'''
开放平台 支付功能  订单支付
商家发起订单请求
'''
import readConfig
import json,uuid
import unittest
from common import common,Log
import paramunittest
from common import configHttp,configDing,configSign

CreateOreder_xls = common.get_xls('OpenApiCase.xlsx','create_order')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*CreateOreder_xls)
class TXRawtx(unittest.TestCase):

    def setParameters(self,case_name,method,data,appsecret,code,msg):

        self.case_name = str(case_name)
        self.method = str(method)
        self.data = json.loads(data)
        self.appsecret = str(appsecret)
        self.code = int(code)
        self.msg = str(msg)



    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testCreateOrder(self):

        self.url = common.get_url_from_xml('create_order')
        # set url
        url = configHttp.set_url(self.url)
        print(url)

        # set headers
        # headers = configHttp.set_headers(self.headers)
        # print(headers)

        # set data
        self.data['merchant_order_sn'] = str(uuid.uuid1())
        sign = configSign.getSignature(self.data,self.appsecret)
        self.data['sign'] = sign
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
    #     print(self.return_json.status_code)
    #     print(self.return_json.text)
    #     self.cheackresult(url,status_code)
    # def cheackresult(self,url, status_code):
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