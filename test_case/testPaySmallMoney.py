'''
开放平台发起小额支付
'''
import readConfig
import json,uuid
import unittest
from common import common,Log
import paramunittest
from common import configHttp

paySmallMoney_xls = common.get_xls('OpenApiCase.xlsx','pay_small_money')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*paySmallMoney_xls)
class pay_small_money(unittest.TestCase):

    def setParameters(self,case_name,method,app_id,secret,merchant_order_sn,
                      pre_amount,user_open_id,item_name,receive_address,code,msg):

        self.case_name = str(case_name)
        self.method = str(method)
        self.app_id = str(app_id)
        self.secret = str(secret)
        self.merchant_order_sn = str(merchant_order_sn)
        if self.merchant_order_sn == '':
            self.merchant_order_sn = str(uuid.uuid1())
        self.pre_amount = int(pre_amount)
        self.user_open_id = str(user_open_id)
        self.item_name = str(item_name)
        self.receive_address = str(receive_address)
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
        configHttp.set_url(self.url)

        # set data
        data = {'app_id':self.app_id,
                'secret':self.secret,
                'merchant_order_sn':self.merchant_order_sn,
                'pre_amount':self.pre_amount,
                'user_open_id':self.user_open_id,
                'item_name':self.item_name,
                'receive_address':self.receive_address}
        configHttp.set_data(data)
        print(data)

        # test interface
        self.return_json = configHttp.request_post_not_headers()
        print(self.return_json.text)

        self.checkResult()

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