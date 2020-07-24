'''
开放平台开通小额自动支付服务
'''

import readConfig
import json,time
import unittest
from common import common,Log
import paramunittest
from common import configHttp

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

setPayConfig_xls = common.get_xls('OpenApiCase.xlsx','set_pay_config')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*setPayConfig_xls)
class set_pay_config(unittest.TestCase):

    def setParameters(self,case_name,method,app_id,redirect_uri):

        self.case_name = str(case_name)
        self.method = str(method)
        self.app_id = str(app_id)
        self.redirect_uri =str(redirect_uri)


    def setUp(self):
        # 设置无界面
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.dr = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',chrome_options= chrome_options)

    def testSetPayConfig(self):

        self.url = common.get_url_from_xml('set_pay_config')
        self.url = configHttp.set_url(self.url)
        new_url = self.url + '?app_id=' + self.app_id + '&redirect_uri=' + self.redirect_uri
        print(new_url)
        self.dr.get(new_url)

        time.sleep(5)

        # 输入账号
        self.dr.find_element_by_xpath('//*[@id="username"]').send_keys('13882618810@163.com')

        # 输入密码
        self.dr.find_element_by_xpath('//*[@id="password"]').send_keys('zhang20.')

        # 点击确定
        self.dr.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/form/div[4]/div/div/div/button').click()
        time.sleep(5)

        text = self.dr.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div[2]/button[1]/span').text

        self.assertIn('同意授权',text)





if __name__ == '__main__':
    unittest.main()