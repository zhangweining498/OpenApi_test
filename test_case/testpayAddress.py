"""
打点钱包转账自动化测试
"""
import readConfig
import json
import unittest
from common import common,Log
import paramunittest
from common import configHttp


payAddress_xls = common.get_xls('userCase.xlsx','payAddress')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*payAddress_xls)
class transfer_accounts(unittest.TestCase):

    def setParameters(self,case_name,method,address,amount,coin_type,info,need_sign,code,msg):
        '''
        set params
        :param case_name:
        :param method:
        :param address:
        :param amount:
        :param coin_type:
        :param info:
        :param need_sign:
        :param code:
        :param msg:
        :return:
        '''
        self.case_name = str(case_name)
        self.method = str(method)
        self.address = str(address)
        self.amount = int(amount)
        self.coin_type = str(coin_type)
        self.info = str(info)
        self.need_sign = bool(need_sign)
        self.code = int(code)
        self.msg = str(msg)

    # def description(self):
    #     """
    #
    #     :return:
    #     """
    #     self.case_name

    def setUp(self):

        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        # print(self.case_name+'测试开始前准备')


    def testpayAddress(self):
        '''
        地址付款
        :return:
        '''
        self.url = common.get_url_from_xml('payAddress')

        # set url
        configHttp.set_url(self.url)

        # set headers
        configHttp.set_headers()

        # set data
        data = {'address':self.address,
                'amount':self.amount,
                'coin_type':self.coin_type,
                'info':self.info,
                'need_sign':self.need_sign}
        configHttp.set_data(data)

        # test interface
        self.return_json = configHttp.request_json_post()

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



















    # def test_01(self):
    #     '''
    #     BSV转账(免密支付)
    #     '''
    #     url = 'https://www.ddpurse.com/api/v1/payAddress'
    #     data = {'address':'1MjUodGyHSFXcmaBmsMnTLtgyrBtTEHxd4',
    #             'amount':1000,
    #             'coin_type':'BSV',
    #             'info':'',
    #             'need_sign':True}
    #     res = self.session.post(url,headers = self.headers,json=data)
    #     code = json.loads(res.text)['code']
    #     self.assertEqual(0,code)
    #
    #
    # def test_02(self):
    #     '''
    #     ETH转账(免密支付)
    #     :return:
    #     '''
    #     url = 'https://www.ddpurse.com/api/v1/payAddress'
    #     data = {'address': '0xC6804E894218214ae3B7F679Ee2AF35c2d307539',
    #             'amount': 2000000,
    #             'coin_type': 'ETH',
    #             'info': '',
    #             'need_sign': True}
    #     res = self.session.post(url, headers=self.headers, json=data)
    #     code = json.loads(res.text)['code']
    #     self.assertEqual(0, code)







