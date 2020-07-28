
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Remote(
    command_executor='http://192.168.1.13:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

driver.get('https://www.baidu.com/')
time.sleep(3)
print(driver.title)

driver.close()