'''
开放平台 支付功能 订单支付
成功获取 order_sn 后，客户端跳转到打点钱包进行支付
'''
import readConfig
import json,uuid,time
import unittest
from common import common,Log
import paramunittest
from common import configHttp,configDing,configSign,configUI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

Order_xls = common.get_xls('OpenApiCase.xlsx','order')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*Order_xls)
class Order(unittest.TestCase):

    def setParameters(self,case_name,method,code,msg):

        self.case_name = str(case_name)
        self.method = str(method)
        self.code = str(code)
        self.msg = str(msg)



    def setUp(self):
        self.dr = configUI.get_driver()
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()
        self.url_01 = 'https://www.ddpurse.com/platform/openapi/create_order'

    def testCreateOrder(self):

        self.url = common.get_url_from_xml('order')
        # set url
        url = configHttp.set_url(self.url)
        sign = configSign.get_order_sign(self.url_01)
        url = url + '?order_sn=' + sign
        print(url)

        # 打开网页
        self.dr.get(url)

        # 显式等待账户输入框出现
        locate = (By.XPATH, '//*[@id="username"]')
        WebDriverWait(self.dr, 10).until(EC.presence_of_element_located(locate))

        # 输入账号
        self.dr.find_element_by_xpath('//*[@id="username"]').send_keys('13882618810@163.com')
        time.sleep(1)

        # 输入密码
        self.dr.find_element_by_xpath('//*[@id="password"]').send_keys('zhang20.')
        time.sleep(1)

        # 点击确定
        self.dr.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[2]/div/div/div/form/div[4]/div/div/div/button').click()
        time.sleep(3)

        # 点击同意支付
        self.dr.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/button[1]').click()

        locate = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[1]/div/div[1]')
        WebDriverWait(self.dr, 10).until(EC.presence_of_element_located(locate))
        text = self.dr.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[1]/div/div[1]').text
        print(text)

        self.cheackresult(text)
    def cheackresult(self,text):
        re = []
        re.append(self.url)
        try:
            self.assertIn('成功',text,'用例失败')
            self.logger.info('客户端跳转到打点钱包进行支付,用例通过')
        except Exception as Ex:
            re.append(Ex)
            self.logger.exception(re)


if __name__ == '__main__':
    unittest.main()