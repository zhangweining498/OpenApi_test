#!/usr/bin/python
# coding=utf-8

import readConfig
import unittest,json,requests,time
from common import common
import paramunittest

localReadConfig = readConfig.ReadConfig()

class dotwallet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        scheme = localReadConfig.get_http('scheme')
        host = localReadConfig.get_http('baseurl')
        cls.server = scheme + '://' + host
        route = common.get_url_from_xml('signin')
        url = cls.server + route
        print(url)
        data = {
                "account":"zwn@boquaninc.com",
                "password":"zhang20.",
                "client_id":"ce7ac9b5c4d54c7f9e71ed3e9a732c12",
                "mobile_prefix":"+86",
                "provider":"local"
        }
        res = requests.post(url,json = data)
        access_token = json.loads(res.text)['data']['access_token']
        cls.headers = {
                "Authorization":"Bearer " + access_token
        }


        url = 'http://192.168.1.141:19002'
        headers = {
            "Authorization": "Basic cmVndGVzdDoxMjM="
        }
        data = {
            "jsonrpc": "1.0",
            "id": "0",
            "method": "generate",
            "params": [1]
        }
        requests.post(url, json=data, headers=headers)


    def flow(self):
        url = 'http://192.168.1.13:3000/dev/api/v1/flow?page=1&page_size=3'
        params = {
            'page':1,
            'page_size':3
        }
        res = requests.get(url,params=params,headers=self.headers)
        tx_id = json.loads(res.text)['data'][0]['tx_id']
        return tx_id



    # def testPayAddressBsv(self):
    #     '''
    #     BSV转账
    #     :return:
    #     '''
    #     route = common.get_url_from_xml('payAddress')
    #     url = self.server + route
    #     data = {
    #             "amount":100000,
    #             "info":"",
    #             "coin_type":"BSV",
    #             "address":"mtzsW2TSLT2juoHcBQ67xHT8U9A5bqihWr",
    #             "need_sign":True,
    #             "use_fee":""
    #     }
    #     res = requests.post(url,json=data,headers=self.headers).text
    #     res = json.loads(res)
    #     code = res['code']
    #     self.assertEqual(0,code)
    #     tx_id = res['data']['rawMsg']['txid']
    #     flow_tx_id = self.flow()
    #     self.assertEqual(tx_id,flow_tx_id)
    #
    # def testPayAddressBTC(self):
    #     '''
    #     BTC转账
    #     :return:
    #     '''
    #     route = common.get_url_from_xml('payAddress')
    #     url = self.server + route
    #     data = {
    #             "amount":10000,
    #             "info":"",
    #             "coin_type":"BTC",
    #             "address":"mpdkxp7fYa78snCAq6wmQiqhAhGC5PyTF9",
    #             "need_sign":True,
    #             "use_fee":""
    #     }
    #     res = requests.post(url,json=data,headers=self.headers).text
    #     res = json.loads(res)
    #     code = res['code']
    #     self.assertEqual(0, code)
    #     tx_id = res['data']['txID']
    #     flow_tx_id = self.flow()
    #     self.assertEqual(tx_id, flow_tx_id)
    #
    # def testPayAddressETH(self):
    #     '''
    #     ETH转账
    #     :return:
    #     '''
    #     route = common.get_url_from_xml('payAddress')
    #     url = self.server + route
    #     data = {
    #         "amount": 2000000,
    #         "info": "",
    #         "coin_type": "ETH",
    #         "address": "0xB101Bf34c3c9f6c8801470f388Fdf18faAf54383",
    #         "need_sign": True,
    #         "use_fee": ""
    #     }
    #     res = requests.post(url, json=data, headers=self.headers).text
    #     res = json.loads(res)
    #     code = res['code']
    #     self.assertEqual(0, code)
    #     tx_id = res['data']['txID']
    #     flow_tx_id = self.flow()
    #     self.assertEqual(tx_id, flow_tx_id)

    # def testTransferBSV(self):
    #     '''
    #     BSV 打点转账 指定接收人
    #     :return:
    #     '''
    #     time.sleep(1)
    #     route = common.get_url_from_xml('transfer')
    #     url = self.server + route
    #     data = {
    #             "amount":2000,
    #             "need_sign":True,
    #             "info":"",
    #             "coin_type":"BSV",
    #             "recvGid":"b940725f2fb97534122613a9683015c6"
    #     }
    #     res = requests.post(url,json=data,headers=self.headers).text
    #     res = json.loads(res)
    #     code = res['code']
    #     self.assertEqual(0, code)
    #     tx_id = res['data']['rawMsg']['txid']
    #     flow_tx_id = self.flow()
    #     self.assertEqual(tx_id, flow_tx_id)
    #
    # def testTransferBTC(self):
    #     '''
    #     BTC 打点转账 指定接收人
    #     :return:
    #     '''
    #     time.sleep(1)
    #     route = common.get_url_from_xml('transfer')
    #     url = self.server + route
    #     data = {
    #             "amount":10000,
    #             "need_sign":True,
    #             "info":"",
    #             "coin_type":"BTC",
    #             "recvGid":"b940725f2fb97534122613a9683015c6"
    #     }
    #     res = requests.post(url, json=data, headers=self.headers).text
    #     res = json.loads(res)
    #     code = res['code']
    #     self.assertEqual(0, code)
    #     tx_id = res['data']['txID']
    #     flow_tx_id = self.flow()
    #     self.assertEqual(tx_id, flow_tx_id)
    #
    # def testTransferETH(self):
    #     '''
    #     ETH 打点转账 指定接收人
    #     :return:
    #     '''
    #     time.sleep(1)
    #     route = common.get_url_from_xml('transfer')
    #     url = self.server + route
    #     data = {
    #             "amount":2000000,
    #             "need_sign":True,
    #             "info":"",
    #             "coin_type":"ETH",
    #             "recvGid":"b940725f2fb97534122613a9683015c6"
    #     }
    #     res = requests.post(url, json=data, headers=self.headers).text
    #     res = json.loads(res)
    #     code = res['code']
    #     self.assertEqual(0, code)
    #     tx_id = res['data']['txID']
    #     flow_tx_id = self.flow()
    #     self.assertEqual(tx_id, flow_tx_id)

    def testSendRedBagBSV(self):
        '''
        发送BSV红包
        :return:
        '''
        time.sleep(1)
        route = common.get_url_from_xml('redbag')
        url = self.server + route
        data = {
                "amount":10000,
                "coin_type":"BSV",
                "info":"BSV 网络非常安全，可以放心使用",
                "type":"random",
                "count":"1",
                "need_sign":True
        }
        res = requests.post(url, json=data, headers=self.headers).text
        res = json.loads(res)
        code = res['code']
        self.assertEqual(0, code)
        tx_id = res['data']['txID']
        flow_tx_id = self.flow()
        self.assertEqual(tx_id, flow_tx_id)

    def testSendRedBagBTC(self):
        '''
        发送BTC红包
        :return:
        '''
        route = common.get_url_from_xml('redbag')
        url = self.server + route
        data = {
                "amount":10000,
                "coin_type":"BTC",
                "info":"BTC 交易，就用打点钱包.",
                "type":"random",
                "count":"1",
                "need_sign":True
        }
        res = requests.post(url, json=data, headers=self.headers).text
        res = json.loads(res)
        code = res['code']
        self.assertEqual(0, code)
        tx_id = res['data']['txID']
        flow_tx_id = self.flow()
        self.assertEqual(tx_id, flow_tx_id)

    def testSendRedBagETH(self):
        '''
        发送ETH红包
        :return:
        '''
        route = common.get_url_from_xml('redbag')
        url = self.server + route
        data = {
            "amount": 2000000,
            "coin_type": "ETH",
            "info": "网络非常安全，可以放心使用",
            "type": "random",
            "count": "1",
            "need_sign": True
        }
        res = requests.post(url, json=data, headers=self.headers).text
        res = json.loads(res)
        code = res['code']
        self.assertEqual(0, code)
        tx_id = res['data']['txID']
        flow_tx_id = self.flow()
        self.assertEqual(tx_id, flow_tx_id)







if __name__ == '__main__':
    unittest.main()

