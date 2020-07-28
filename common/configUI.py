from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time



# def get_driver():
#     chrome_options = Options()
#     chrome_options.add_argument('--handless')
#
#     driver = webdriver.Remote(
#         command_executor='http://192.168.1.13:4444/wd/hub',
#         desired_capabilities=DesiredCapabilities.CHROME
#     )
#     return driver

def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    dr = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',chrome_options=chrome_options)
    return dr





if __name__ == '__main__':

    chrome_options = Options()
    chrome_options.add_argument('--headless')

    driver = webdriver.Remote(
        command_executor='http://192.168.1.13:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)

    driver.get('https://www.baidu.com/')
    time.sleep(3)
    print(driver.title)

    driver.close()
