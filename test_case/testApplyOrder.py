'''
用户发起订单请求
'''

import readConfig
import readConfig
import json
import uuid,time
import unittest
from common import common,Log
import paramunittest
from common import configHttp

applyOrder_xls = common.get_xls('OpenApiCase.xlsx','apply_order')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}


@paramunittest.parametrized(*applyOrder_xls)
class apply_order(unittest.TestCase):

    def setParameters(self,case_name,method,app_id,merchant_order_sn,item_name,order_amount,nonce_str,
                      sign,notice_uri ,redirect_uri,opreturn,receive_address,code,msg):

        self.case_name = str(case_name)
        self.method = str(method)
        self.app_id = int(app_id)
        self.merchant_order_sn = str(merchant_order_sn)
        self.item_name = str(item_name)
        self.order_amount = int(order_amount)
        self.nonce_str = str(nonce_str)
        self.sign = str(sign)
        self.notice_uri = str(notice_uri)
        self.redirect_uri = str(redirect_uri)
        self.opreturn = str(opreturn)
        self.receive_address = str(receive_address)
        self.code = int(code)
        self.msg = str(msg)

    def setUp(self):
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testApplyOrder(self):

        self.url = common.get_url_from_xml('apply_order')

        # set url
        configHttp.set_url(self.url)

        # set data
        data = {'app_id':self.app_id,
                'merchant_order_sn':uuid.uuid1(),
                'item_name':self.item_name,
                'order_amount':self.order_amount,
                'nonce_str':str(time.time()),
                'sign':''}





if __name__ == '__main__':
    unittest.main()