import time
from Library.config import Config
# import pytest
from selenium import webdriver
from Data import reading_objects
from Data.reading_objects import ReadExcel


read_xl = ReadExcel()
red = read_xl.read_locators(Config.Print_DATA_PATH_loc)
print(red)

class Printhelp:

    def __init__(self, driver):
        self.driver = driver

    def clickbusticket(self):
        self.driver.find_element(*red['busticket']).click()
        time.sleep(3)

    def printticket(self):
        self.driver.find_element(*red['printticket']).click()
        time.sleep(3)

    def tickettb(self, ticketnumbertb):
        self.driver.find_element(*red['ticketnumbertb']).send_keys(ticketnumbertb)
        time.sleep(3)

    def phnotb(self, phonenumtb):
        self.driver.find_element(*red['phonenumtb']).send_keys(phonenumtb)
        time.sleep(6)

    def submitbtn(self):
        self.driver.find_element(*red['submitbtn']).click()
        time.sleep(3)

    def helplink(self):
        self.driver.find_element(*red['help']).click()
        time.sleep(3)
        handles = self.driver.window_handles
        # print(handles)
        self.driver.switch_to.window(handles[1])
        time.sleep(3)

    def loginiframe(self):
        ele = self.driver.find_element(*red['loginiframe'])
        time.sleep(3)
        self.driver.switch_to.frame(ele)
        time.sleep(3)

    def loginphno(self, logphoneno):
        self.driver.find_element(*red['logphoneno']).send_keys(logphoneno)
        time.sleep(30)

    # def recptch(self):
    #     self.driver.find_element(*red['reCaptcha']).click()
    #     time.sleep(20)

    def generate(self):
        self.driver.find_element(*red['generateoptbtn']).click()
        time.sleep(30)

    def verifyotp(self):
        self.driver.find_element(*red['verifybtn']).click()   ###verify button(otp)
        time.sleep(5)

    def helpiframe(self):
        ele_ = self.driver.find_element(*red['helpiframe'])  ##helpiframe
        self.driver.switch_to.frame(ele_)
        time.sleep(3)

    def preferlanguage(self):
        self.driver.find_element(*red['preferlanguage']).click()
        time.sleep(3)

    def checkbox(self):
        self.driver.find_element(*red['languagecb']).click()
        time.sleep(3)

    def set(self):
        self.driver.find_element(*red['setlanguage']).click()
        time.sleep(3)

    def viewallbooking(self):
        self.driver.find_element(*red['viewallbookings']).click()
        time.sleep(3)

    def redbus(self):
        self.driver.find_element(*red['rebbusicon']).click()
        time.sleep(3)

    def redrail(self):
        self.driver.find_element(*red['redrailicon']).click()
        time.sleep(3)

    def ryde(self):
        self.driver.find_element(*red['rydeicon']).click()
        time.sleep(3)

    def confirmed(self):
        self.driver.find_element(*red['confirmed']).click()
        time.sleep(3)

    def cncelled(self):
        self.driver.find_element(*red['cancelled']).click()
        time.sleep(3)

    def failed(self):
        self.driver.find_element(*red['failed']).click()
        time.sleep(3)

    def backarrow(self):
        self.driver.find_element(*red['backarrow']).click()
        time.sleep(3)

    def newbooking(self):
        self.driver.find_element(*red['newbusbookinghelp']).click()
        time.sleep(3)

    def available(self):
        self.driver.find_element(*red['availablebus']).click()
        time.sleep(3)

    def technical(self):
        self.driver.find_element(*red['technicalissue']).click()
        time.sleep(4)

    def nobus(self):
        self.driver.find_element(*red['nobusfound']).click()
        time.sleep(5)

    def redBusReferralHelp(self):
        self.driver.find_element(*red['redbusrefferalhelp']).click()
        time.sleep(3)

    def nothanks(self):
        self.driver.find_element(*red['nothanks']).click()
        time.sleep(3)

    def offers(self):
        self.driver.find_element(*red['offers']).click()
        time.sleep(3)

    def redBusWalletHelp(self):
        self.driver.find_element(*red['redbuswallethelp']).click()
        time.sleep(3)
    def wallethelp(self):
        self.driver.find_element(*red['walletamt']).click()
        time.sleep(3)







