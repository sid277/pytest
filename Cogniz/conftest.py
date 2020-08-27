import time
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

password = "admin12345"

@pytest.fixture(params=["firefox", "chrome"], scope='class')
def test_init(request):
    # open browser window
    global driver
    if request.param == "firefox":
        driver = webdriver.Firefox(executable_path="D:/Installed Apps/Webdrivers/geckodriver-v0.26.0-win64/geckodriver.exe")
    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path="D:/Installed Apps/Webdrivers/chromedriver_win32/chromedriver.exe")
    # if request.param == "opera":
    #     driver = webdriver.Opera(executable_path="D:/Installed Apps/Webdrivers/operadriver_win64/operadriver.exe")
    # if request.param == "edge":
    #     driver = webdriver.Edge(executable_path="D:/Installed Apps/Webdrivers/edgedriver_win64/msedgedriver.exe")
    # if request.param == "ie":
    #     driver = webdriver.Ie(executable_path="D:/Installed Apps/Webdrivers/IEDriverServer_x64_3.150.1/IEDriverServer.exe")
    driver.maximize_window()

    # yield is used to call all the linked functions with current function through fixture
    yield driver
    # driver.implicitly_wait(10)

    # close the browser in the end
    driver.quit()
