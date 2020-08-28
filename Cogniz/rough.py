import random
import time
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

password = "admin12345"


@pytest.fixture(params=["firefox"], scope='class')
def test_init(request):
    if request.param == "firefox":
        web_driver = webdriver.Firefox(
            executable_path="D:/Installed Apps/Webdrivers/geckodriver-v0.26.0-win64/geckodriver.exe")
    if request.param == "chrome":
        web_driver = webdriver.Chrome(
            executable_path="D:/Installed Apps/Webdrivers/chromedriver_win32/chromedriver.exe")
    # if request.param == "opera":
    #     driver = webdriver.Opera(executable_path="D:/Installed Apps/Webdrivers/operadriver_win64/operadriver.exe")
    # if request.param == "edge":
    #     driver = webdriver.Edge(executable_path="D:/Installed Apps/Webdrivers/edgedriver_win64/msedgedriver.exe")
    # if request.param == "ie":
    #     driver = webdriver.Ie(executable_path="D:/Installed Apps/Webdrivers/IEDriverServer_x64_3.150.1/IEDriverServer.exe")
    request.cls.driver = web_driver
    web_driver.maximize_window()

    # yield is used to call all the linked functions with current function through fixture
    yield web_driver
    # driver.implicitly_wait(10)

    # close the browser in the end
    # driver.quit()


@pytest.mark.usefixtures("test_init")
class BaseTest:
    pass


class Test_Viz(BaseTest):

    def test_filter(self):

        # navigate to the application home page
        self.driver.get("https://cognitensor.com/")

        # click login
        self.driver.find_element_by_xpath("/html/body/div/div/div/header/div[2]/div[2]/a[7]").click()
        self.driver.implicitly_wait(20)

        # fill login form
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/input').send_keys("qatester@cognitensor.com")
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/input').send_keys(password)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[3]/div/button/span[1]').click()
        self.driver.implicitly_wait(20)

        # Click Viz link
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[1]/div/a[2]").click()

        expected_dashboard = "test_board1"

        # Click dashboard option in sidebar
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[1]/div/a[2]/div/span").click()

        # Click the desired dashboard with text "expected_dashboard"
        self.driver.find_element_by_link_text(expected_dashboard).click()

        # Click filter button
        self.driver.find_element_by_xpath("//*[@id=\"dashboard-tab\"]/div[2]/div[1]/button").click()

        # Count number of filters available
        no_of_filters = len(
            self.driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div"))

        print(no_of_filters)

        self.driver.find_element_by_xpath("//*[@id=\"dashboard-tab\"]/div[2]/div[1]/div/div/div[1]/span/div/button[2]").click()