from POM.redbus import Printhelp
import time
from Data.reading_objects import ReadExcel
from Library.config import Config
import pytest

class Test_Help:
    read_xl = ReadExcel()
    details = read_xl.read_test_data(Config.Print_DATA_PATH)
    @pytest.mark.parametrize('ticketnumbertb, phonenumtb, logphoneno', details)


    def test_print(self,ticketnumbertb, phonenumtb , logphoneno, _driver):
        _driver.implicitly_wait(30)
        m = Printhelp(_driver)
        m.clickbusticket()
        m.printticket()
        m.tickettb(ticketnumbertb)
        m.phnotb(phonenumtb)
        m.submitbtn()
        m.helplink()
        m.loginiframe()
        m.loginphno(logphoneno)
        # m.recptch()
        m.generate()
        m.verifyotp()
        m.helpiframe()
        # m.language()
        m.preferlanguage()
        m.checkbox()
        m.set()
        m.viewallbooking()
        m.redbus()
        m.confirmed()
        m.cncelled()
        m.failed()
        m.redrail()
        m.confirmed()
        m.cncelled()
        m.failed()
        m.ryde()
        m.backarrow()
        m.newbooking()
        m.available()
        m.backarrow()
        m.technical()
        m.nobus()
        m.backarrow()
        m.redBusReferralHelp()
        m.nothanks()
        m.backarrow()
        m.offers()
        m.nothanks()
        m.backarrow()
        m.redBusWalletHelp()
        m.wallethelp()
        m.backarrow()


