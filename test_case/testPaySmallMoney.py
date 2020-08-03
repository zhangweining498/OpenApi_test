'''
开放平台发起小额支付
'''
import readConfig
import json,uuid
import unittest
from common import common,Log
import paramunittest
from common import configHttp,configDing

paySmallMoney_xls = common.get_xls('OpenApiCase.xlsx','pay_small_money')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*paySmallMoney_xls)
class pay_small_money(unittest.TestCase):

    def setParameters(self,case_name,method,data,merchant_order_sn,receive_address,code,msg):

        self.case_name = str(case_name)
        self.method = str(method)
        self.data = json.loads(data)
        self.merchant_order_sn = str(merchant_order_sn)
        if self.merchant_order_sn == '':
            self.merchant_order_sn = str(uuid.uuid1())
        self.receive_address = str(receive_address)
        self.data['merchant_order_sn'] = self.merchant_order_sn
        self.data['receive_address'] = self.receive_address
        self.code= int(code)
        self.msg = str(msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testPaySmallMoney(self):
        '''
        发起小额支付
        :return:
        '''
        self.url = common.get_url_from_xml('pay_small_money')

        # set url
        url = configHttp.set_url(self.url)

        configHttp.set_data(self.data)
        print(self.data)
        print(type(self.data))

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
    #         re.append(self.info)
    #         self.logger.info(re)
    #     except Exception as Ex:
    #         re.append(Ex)
    #         self.logger.exception(re)
    #         configDing.dingmsg(url, status_code, Ex)

if __name__ == '__main__':
    unittest.main()