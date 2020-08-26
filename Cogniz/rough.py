import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys

global driver
#driver = webdriver.Firefox(executable_path="D:/Installed Apps/Webdrivers/geckodriver-v0.26.0-win64/geckodriver.exe")
driver = webdriver.Chrome(executable_path="D:/Installed Apps/Webdrivers/chromedriver_win32/chromedriver.exe")
# driver = webdriver.Opera(executable_path="D:/Installed Apps/Webdrivers/operadriver_win64/operadriver.exe")
# driver = webdriver.Edge(executable_path="D:/Installed Apps/Webdrivers/edgedriver_win64/msedgedriver.exe")
# driver = webdriver.Ie(executable_path="D:/Installed Apps/Webdrivers/IEDriverServer_x64_3.150.1/IEDriverServer.exe")

# driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://cognitensor.com/")

driver.find_element_by_xpath("/html/body/div/div/div/header/div[2]/div[2]/a[7]").click()

driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/input').send_keys("qatester@cognitensor.com")
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/input').send_keys("admin12345")
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[3]/div/button/span[1]').click()
driver.implicitly_wait(20)

driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[1]/div/a[2]").click()

driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[1]/div/a[1]/div/span").click()

driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/span[2]").click()

driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/input").send_keys("jnbfhbwerfbvuewgf")
time.sleep(5)
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/input").send_keys(Keys.CONTROL + "a", Keys.DELETE)

