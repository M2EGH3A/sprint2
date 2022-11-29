import pytest
from selenium import webdriver
from Library.config import Config
# path = r"C:\Users\Administrator\Downloads\chromedriver_win32 (2)\chromedriver.exe"


@pytest.fixture(params=["Chrome"])
def _driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(Config.ChromeDriver)


    # elif request.param == "Edge":
    #     driver = webdriver.Edge(Config.EdgeDriver)
    # elif request.param == "Firefox":
    #
    #     driver = webdriver.Firefox(Config.FirefoxDriver)







    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(60)
    yield driver
    driver.save_screenshot("test_redbus.png")
    print(driver.title)
    driver.close()