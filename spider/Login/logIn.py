from selenium import webdriver
from commonBusiness.Exception import businessException
import time
from lackey import *
from bs4 import BeautifulSoup

class LogIn:

    def __init__(self, driverType, url):
        print("### Set browser type")
        self.browser = driverType
        if self.browser == "chrome":
            print("### Chrome ")
            # chrome 다운로드 받은 크롬 드라이버의 경로를 지정한다.
            self.driver = webdriver.Chrome('C:/Users/Namkil kim/PycharmProjects/chromedriver')
        elif self.browser == "phantomJS":
            print("### PhantomJS ")
            # phantomjs 렌더링을 하지 않는 브라우저
            self.driver = webdriver.PhantomJS('C:/Users/Namkil kim/PycharmProjects/phantomjs-2.1.1-windows/bin/phantomjs')
        else:
            raise businessException.businessException("Unsupported browser => " + self.browser)

        print("### Set log-in page")
        self.company = url
        if self.company == "hyundaicard":
            print("### Open HyundaiCard log-in page ")
            # 현대카드 로그인 페이지 오픈
            self.driver.get('https://www.hyundaicard.com/cpa/ma/CPAMA0101_01.hc')
            # 이미지폴더 셋팅
            self.imageFolder = 'HCKeyPadImage'


        elif self.company == "wooribank":
            print("### Open WooriBank log-in page ")
            # 현대카드 로그인 페이지 오픈
            self.driver.get('https://spib.wooribank.com/pib/Dream?withyou=CMLGN0001')
            # 이미지폴더 셋팅
            self.imageFolder = 'WBKeyPadImage'

        else:
            raise businessException.businessException("Unsupported company website => " + self.company)



    def typeAccount(self, account):
        if self.company == "hyundaicard":
            self.driver.maximize_window()
            self.driver.find_element_by_name('webMbrId').send_keys(account)

        elif self.company == "wooribank":
            time.sleep(3)
            self.driver.find_element_by_name('webMbrId').send_keys(account)

        print("### typed " + self.company + " account")

    def typePasswordByVK(self, pwd):
        r = Screen(0)
        # addImagePath(os.path.dirname(__file__) + self.imageFolder)
        addImagePath('C:/Users/Namkil kim/PycharmProjects/sojinProject/' + self.imageFolder)
        r.click("mouseInput.png")
        for a in pwd:
            r.click(a + ".png")

        print("### typed " + self.company + " Password")
        r.click("loginBtn.png")
        print("### clicked " + self.company + " Log-in Button")

    def getPageSource(self):
        return self.driver.page_source

    def close(self):
        self.close()
        print("### WebDriver Close")

try :
    hcLogin = LogIn("chrome", "hyundaicard")
    hcLogin.typeAccount('ngkim51')
    hcLogin.typePasswordByVK('rlaskarlf83')
    pageSource = hcLogin.getPageSource()
    print(pageSource)
    hcLogin.close()
    print("test githup!!")

except businessException.businessException as be:
    hcLogin.close()
    print(be)

