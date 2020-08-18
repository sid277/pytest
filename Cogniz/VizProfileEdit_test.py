from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


# class VizScript:

# browsers = ["firefox", "chrome", "opera", "edge", "ie"]
#
# for browser in browsers:
#     global driver
#     if browser == "firefox":
#         driver = webdriver.Firefox(executable_path="D:/Installed Apps/Webdrivers/geckodriver-v0.26.0-win64/geckodriver.exe")
#     elif browser == "chrome":
#         driver = webdriver.Chrome(executable_path="D:/Installed Apps/Webdrivers/chromedriver_win32/chromedriver.exe")
#     elif browser == "opera":
#         driver = webdriver.Opera(executable_path="D:/Installed Apps/Webdrivers/operadriver_win64/operadriver.exe")
#     elif browser == "edge":
#         driver = webdriver.Edge(executable_path="D:/Installed Apps/Webdrivers/edgedriver_win64/msedgedriver.exe")
#     elif browser == "ie":
#         driver = webdriver.Ie(executable_path="D:/Installed Apps/Webdrivers/IEDriverServer_x64_3.150.1/IEDriverServer.exe")

password = "admin12345"

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
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/input').send_keys(password)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[3]/div/button/span[1]').click()
    driver.implicitly_wait(20)
    actualHead = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/h2").text
    expectedHead = "Deep Optics"
    assert actualHead == expectedHead

def test_clickViz(test_openBrowser):
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[1]/div/a[2]").click()
    actualUrl = driver.current_url
    expectedUrl = "https://console.cognitensor.com/athena"
    assert actualUrl == expectedUrl

def test_userProfile(test_openBrowser):
    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[1]/div/a[1]/div/span").click()
    actualUrl = driver.current_url
    expectedUrl = "https://console.cognitensor.com/athena/profile"
    assert actualUrl == expectedUrl

def test_editUser(test_openBrowser):
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/span[2]").click()
    first_name = "Jon"
    last_name = "Smith"
    department = "QA"
    company_profile = "Cogni"

    driver.implicitly_wait(10)

    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/input").clear()
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/input").send_keys(first_name)
    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/input").clear()
    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/input").send_keys(last_name)
    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/div/div/input").clear()
    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/div/div/input").send_keys(department)
    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[4]/div/div/div/input").clear()
    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[4]/div/div/div/input").send_keys(company_profile)
    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[5]/button/span[1]").click()

    wait = WebDriverWait(driver, 10)
    loginStatus = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body"))).text
    print(loginStatus)
    driver.refresh()

    displayed_name = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/span[2]").text
    assert displayed_name == first_name

def test_changePassword(test_openBrowser):

    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/button[3]/span").click()

    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/input").clear()
    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/input").send_keys(password)

    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/input").clear()
    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/input").send_keys("")

    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/input").clear()
    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/input").send_keys("")

    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/button/span[1]").click()

    wait = WebDriverWait(driver, 10)
    toast = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body"))).text
    #toast = driver.find_element_by_class_name("Toastify__toast-container Toastify__toast-container--bottom-right").text
    print(toast)

    driver.implicitly_wait(20)
    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[1]/a[1]/span").click()

def test_dashboard(test_openBrowser):

    driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[1]/div/a[2]/div/span").click()

    driver.find_element_by_link_text("test_board1").click()




# def test_logoutUser(test_openBrowser):
#
#     driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/h5").click()
#     driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[2]/button[1]/span[1]").click()
#     actualUrl = driver.current_url
#     expectedUrl = "https://console.cognitensor.com/login"
#     assert actualUrl == expectedUrl

