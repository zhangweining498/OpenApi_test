

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
getcode_xls = common.get_xls('OpenApiCase.xlsx','get_code')
localReadConfig = readConfig.ReadConfig()
configHttp = configHttp.ConfigHttp()
info = {}

@paramunittest.parametrized(*getcode_xls)
class get_code(unittest.TestCase):

    def setParameters(self,case_name,method,app_id,redirect_uri):

        self.case_name = str(case_name)
        self.method = str(method)
        self.app_id = str(app_id)
        self.redirect_uri = str(redirect_uri)


    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.dr = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',\
                                   chrome_options=chrome_options)

        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_logger()

    def testgetCode(self):

        self.url = common.get_url_from_xml('get_code')
        self.url = configHttp.set_url(self.url)
        new_url = self.url + '?app_id=' + self.app_id + '&redirect_uri=' + self.redirect_uri
        print(new_url)
        self.dr.get(new_url)

        #显式等待账户输入框出现
        locate = (By.XPATH, '//*[@id="username"]')
        WebDriverWait(self.dr, 20).until(EC.presence_of_element_located(locate))

        # 输入账号
        self.dr.find_element_by_xpath('//*[@id="username"]').send_keys('13882618810@163.com')

        # 输入密码
        self.dr.find_element_by_xpath('//*[@id="password"]').send_keys('zhang20.')

        # 点击确定
        self.dr.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/form/div[4]/div/div/div/button').click()
        time.sleep(10)
        try:
            # 显式等待同意授权按钮出现
            receive_authorization_attribute = '//*[@id="root"]/div/div/div[2]/div/div[2]/button[1]'
            # 同意授权
            self.dr.find_element_by_xpath(receive_authorization_attribute).click()
        except:
            print('近期已授权，自动授权')
        time.sleep(5)
        # locator = (By.XPATH, '//*[@id="root"]/div/div[3]/img')
        # WebDriverWait(self.dr, 30).until(EC.presence_of_element_located(locator))
        url = self.dr.current_url
        code = url.split('=', 1)[1]
        print(code)
        self.dr.quit()

        try:
            self.assertIsNotNone(code)
            self.logger.info(self.info)
        except Exception as Ex:
            self.logger.exception(Ex)




if __name__ == '__main__':
    unittest.main()