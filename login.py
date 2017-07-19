from selenium import webdriver
from sikuli.sikuli import *

class LogIn:

    def __init__(self, driverType):
        print("### Diver type setting")
        if driverType == "chrome":
            print("### Chrome ")
            # chrome 다운로드 받은 크롬 드라이버의 경로를 지정한다.
            driver = webdriver.Chrome('C:/Users/Namkil kim/PycharmProjects/chromedriver')
        elif driverType == "phantomJS":
            print("### PhantomJS ")
            # phantomjs 렌더링을 하지 않는 브라우저
            driver = webdriver.PhantomJS('C:\Users\Namkil kim\PycharmProjects\phantomjs-2.1.1-windows\bin\phantomjs')
        else:
            print("### Unsupported browser. -> " + driverType)
            raise


driver.get('https://www.hyundaicard.com/cpa/ma/CPAMA0101_01.hc')
# driver.get('https://spib.wooribank.com/pib/Dream?withyou=CMLGN0001')

driver.find_element_by_name('webMbrId').send_keys('ngkim52')

type()
# driver.find_element_by_name('webPwd').send_keys("r")
# driver.find_element_by_id('loginBtn').click()


