# import time
#
# # import pytest
# from selenium import webdriver
# from Data import reading_objects
# path = r"C:\Users\Administrator\Downloads\chromedriver_win32 (2)\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
#
# driver.get(r"https://www.redbus.in/bus-tickets/")
# driver.maximize_window()
#
# red = reading_objects.read_locators()
#
#
# # print(red)
#
# class Printhelp:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def clickbusticket(self):
#         self.driver.find_element(*red['busticket']).click()
#         time.sleep(3)
#
#     def printticket(self):
#         self.driver.find_element(*red['printticket']).click()
#         time.sleep(3)
#
#     def tickettb(self):
#         self.driver.find_element(*red['ticketnumbertb']).send_keys("TR9R32228404")
#         time.sleep(3)
#
#     def phnotb(self):
#         self.driver.find_element(*red['phonenumtb']).send_keys("9886055217")
#         time.sleep(3)
#
#     def submitbtn(self):
#         self.driver.find_element(*red['submitbtn']).click()
#         time.sleep(3)
#
#     def helplink(self):
#         self.driver.find_element(*red['help']).click()
#         time.sleep(3)
#         handles = self.driver.window_handles
#         # print(handles)
#         self.driver.switch_to.window(handles[1])
#
#     def loginiframe(self):
#         ele = self.driver.find_element(*red['loginiframe'])
#         time.sleep(3)
#         self.driver.switch_to.frame(ele)
#         time.sleep(3)
#
#     def loginphno(self):
#         self.driver.find_element(*red['logphoneno']).send_keys("9108688668")
#         time.sleep(10)
#
#     def recptch(self):
#         self.driver.find_element(*red['reCaptcha']).click()
#         time.sleep(20)
#
#     def generate(self):
#         self.driver.find_element(*red['generateoptbtn']).click()
#         time.sleep(30)
#
#     def verifyotp(self):
#         self.driver.find_element(*red['verifybtn']).click()   ###verify button(otp)
#         time.sleep(5)
#
#     def helpiframe(self):
#         ele_ = self.driver.find_element(*red['helpiframe'])  ##helpiframe
#         self.driver.switch_to.frame(ele_)
#         time.sleep(3)
#
#     def preferlanguage(self):
#         self.driver.find_element(*red['preferlanguage']).click()
#         time.sleep(3)
#     def checkbox(self):
#         self.driver.find_element(*red['languagecb']).click()
#         time.sleep(3)
#
#     def set(self):
#         self.driver.find_element(*red['setlanguage']).click()
#         time.sleep(3)
#
#     def viewallbooking(self):
#         self.driver.find_element(*red['viewallbookings']).click()
#         time.sleep(3)
#
#     def redbus(self):
#         self.driver.find_element(*red['rebbusicon']).click()
#         time.sleep(3)
#
#     def redrail(self):
#         self.driver.find_element(*red['redrailicon']).click()
#         time.sleep(3)
#
#     def ryde(self):
#         self.driver.find_element(*red['rydeicon']).click()
#         time.sleep(3)
#
#     def confirmed(self):
#         self.driver.find_element(*red['confirmed']).click()
#         time.sleep(3)
#
#     def cncelled(self):
#         self.driver.find_element(*red['cancelled']).click()
#         time.sleep(3)
#
#     def failed(self):
#         self.driver.find_element(*red['failed']).click()
#         time.sleep(3)
#
#     def backarrow(self):
#         self.driver.find_element(*red['backarrow']).click()
#         time.sleep(3)
#
#     def newbooking(self):
#         self.driver.find_element(*red['newbusbookinghelp']).click()
#         time.sleep(3)
#     def available(self):
#         self.driver.find_element(*red['availablebus']).click()
#         time.sleep(3)
#     def technical(self):
#         self.driver.find_element(*red['technicalissue']).click()
#         time.sleep(4)
#     def nobus(self):
#         self.driver.find_element(*red['nobusfound']).click()
#         time.sleep(5)
#     def redBusReferralHelp(self):
#         self.driver.find_element(*red['redbusrefferalhelp']).click()
#         time.sleep(3)
#     def nothanks(self):
#         self.driver.find_element(*red['nothanks']).click()
#         time.sleep(3)
#     def offers(self):
#         self.driver.find_element(*red['offers']).click()
#         time.sleep(3)
#
#     def redBusWalletHelp(self):
#         self.driver.find_element(*red['redbuswallethelp']).click()
#         time.sleep(3)
#     def wallethelp(self):
#         self.driver.find_element(*red['walletamt']).click()
#
# m = Printhelp(driver)
# m.clickbusticket()
# m.printticket()
# m.tickettb()
# m.phnotb()
# m.submitbtn()
# m.helplink()
# m.loginiframe()
# m.loginphno()
# m.recptch()
# m.generate()
# m.verifyotp()
# m.helpiframe()
# # m.language()
# m.preferlanguage()
# m.checkbox()
# m.set()
# m.viewallbooking()
# m.redbus()
# m.confirmed()
# m.cncelled()
# m.failed()
# m.redrail()
# m.confirmed()
# m.cncelled()
# m.failed()
# m.ryde()
# m.backarrow()
# m.newbooking()
# m.available()
# m.backarrow()
# m.technical()
# m.nobus()
# m.backarrow()
# m.redBusReferralHelp()
# m.nothanks()
# m.backarrow()
# m.offers()
# m.nothanks()
# m.backarrow()
# m.redBusWalletHelp()
# m.wallethelp()
# m.backarrow()
#
#
#
#
#
