import readConfig
from common.Log import MyLog as MyLog
from common import configUI
from common.common import get_headers
# from common import common
import requests,json,time
from common.common import get_url_from_xml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
localReadConfig = readConfig.ReadConfig()


class ConfigHttp:
    def __init__(self):
        global scheme, host, port, timeout

        scheme = localReadConfig.get_http('scheme')
        host = localReadConfig.get_http('baseurl')
        port = localReadConfig.get_http('port')
        # timeout = localReadConfig.get_http('timeout')
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data= {}
        self.url = None
        self.files = {}
        self.state = 0


    def set_headers(self, headers):
        '''
        set headers
        :return:
        '''

        # self.headers = get_headers()
        # print(self.headers)
        self.headers = headers


    def set_url(self,url):
        '''
        set url
        :param url:
        :return:
        '''
        self.url = scheme + '://' + host + url
        return self.url


    def set_data(self, data):
        """
        set data
        :param data:
        :return:
        """
        self.data = data

    def set_params(self,params):
        '''
        set params
        :param params:
        :return:
        '''
        self.params = params

    def request_get(self):
        '''
        defind get method
        :return:
        '''

        try:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            return response
        except Exception as Ex:
            self.logger.exception(Ex)


    def request_get_no_params(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            return response
        except Exception as ex:
            self.logger.exception(ex)
            return None

    def request_json_post(self):
        '''
        defind post method,make json
        :return:
        '''
        try:
            response = requests.post(self.url, headers = self.headers, json = self.data)
            return response
        except Exception as ex:
            self.logger.exception(ex)
            return None


    def request_post_no_data(self):
        '''
        defind post method,make json
        :return:
        '''
        try:
            response = requests.post(self.url, headers = self.headers)
            return response
        except Exception as ex:
            self.logger.exception(ex)
            return None

    def request_post_not_headers(self):
        '''
        defind post method,make json
        :return:
        '''
        try:
            response = requests.post(self.url, json = self.data)
            return response
        except Exception as ex:
            self.logger.error(ex)
            return None

    def requests_by_method(self,method):
        method = method.upper()
        if method == 'GET':

            # 请求头和请求参数都存在
            if self.headers and self.data:
                response = requests.get(self.url, headers=self.headers, params=self.data)
                return response

            # 只有请求头
            elif self.headers:
                print(1)
                response = requests.get(self.url,headers = self.headers)
                return response

            # 只有请求参数
            else:
                response = requests.get(self.url,params=self.data)
                return response
        elif method == 'POST':

            # 请求头和请求参数都存在
            if self.headers and self.data:
                response = requests.post(self.url, headers=self.headers, json=self.data)
                return response

            # 只有请求头
            elif self.headers:
                response = requests.post(self.url, headers=self.headers)
                return response

            # 只有请求参数
            else:
                response = requests.post(self.url, json=self.data)
                return response






    def code(self):
        '''
        获取code
        :return:
        '''
        url = get_url_from_xml('get_code')
        new_url = self.url = scheme + '://' + host + url

        # 设置无界面
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        #
        # dr = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',\
        #                       chrome_options=chrome_options)
        dr = configUI.get_driver()
        dr.get(new_url + '?app_id=0d158bc3605fffe30f7046f0c9c7e4bf\
                               &redirect_uri=https://www.ddpurse.com/platform/testapp/hello')
        locate = (By.XPATH, '//*[@id="username"]')
        WebDriverWait(dr, 20).until(EC.presence_of_element_located(locate))

        # 输入账号
        dr.find_element_by_xpath('//*[@id="username"]').send_keys('13882618810@163.com')

        # 输入密码
        dr.find_element_by_xpath('//*[@id="password"]').send_keys('zhang20.')

        # 点击确定
        dr.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div/form/div[4]/div/div/div/button').click()

        time.sleep(10)

        receive_authorization_attribute = '//*[@id="root"]/div/div/div[2]/div/div[2]/button[1]'

        try:
            # 显式等待同意授权按钮出现
            receive_authorization_attribute = '//*[@id="root"]/div/div/div[2]/div/div[2]/button[1]'
            # 同意授权
            dr.find_element_by_xpath(receive_authorization_attribute).click()
        except:
            print('近期已授权，自动授权')
        # try:
        #     locator = (By.XPATH, '//*[@id="root"]/div/div[3]/img')
        #     WebDriverWait(dr, 30).until(EC.presence_of_element_located(locator))
        time.sleep(10)
        url = dr.current_url
        code = url.split('=', 1)[1]
        dr.quit()
        return code

    def access_token(self):
        code = ConfigHttp.code(self)
        url = 'https://www.ddpurse.com/openapi/access_token'
        data = {'app_id':'0d158bc3605fffe30f7046f0c9c7e4bf',
                'secret':'e9943b6b167554fe555e39c1428c1d86',
                'code':code}
        res = requests.post(url,json=data)
        content = json.loads(res.text)
        return content





















if __name__ == '__main__':
    c = ConfigHttp()
    url = '/api/v1/payAddress'
    data  = {'address':'1MjUodGyHSFXcmaBmsMnTLtgyrBtTEHxd4',
                'amount':1000,
                'coin_type':'BSV',
                'info':'',
                'need_sign':True}
    c.set_url(url)
    c.set_data(data)
    res = c.request_json_post()
    print(res.text)
    # print(res.text)

