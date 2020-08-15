from selenium import webdriver
import pytest


# class VizScript:
# def setup_module(module):
@pytest.fixture(scope="module")
def test_openBrowser():
    # open browser window

    global driver
    driver = webdriver.Firefox(executable_path="D:/Installed Apps/Webdrivers/geckodriver-v0.26.0-win64/geckodriver.exe")
    # driver.implicitly_wait(30)
    driver.maximize_window

    yield driver

    driver.implicitly_wait(10)
    #driver.quit()


def test_gotoUrl(test_openBrowser):
    # navigate to the application home page

    driver.get("https://cognitensor.com/")
    actualTitle = driver.title
    expectedTitle = "Cognitensor | an A.I. company"
    assert actualTitle == expectedTitle


def test_login(test_openBrowser):
    # click login

    driver.find_element_by_xpath("/html/body/div/div/div/header/div[2]/div[2]/a[7]").click()
    driver.implicitly_wait(20)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/input').send_keys("qatester@cognitensor.com")
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/input').send_keys("admin12345")
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[3]/div/button/span[1]').click()
    driver.implicitly_wait(20)
    actualUrl = driver.current_url
    expectedUrl = "https://console.cognitensor.com/landing/main"
    assert actualUrl == expectedUrl


#def test_close_browser():
    # close browser at the end


