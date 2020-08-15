from selenium import webdriver
import pytest


def test_firstViz():

    global driver

    driver = webdriver.Firefox(executable_path="D:/Installed Apps/Webdrivers/geckodriver-v0.26.0-win64/geckodriver.exe")

    driver.implicitly_wait(30)

    driver.maximize_window()
    # navigate to the application home page

    driver.get("https://cognitensor.com/")
    # click login

    driver.find_element_by_xpath("/html/body/div/div/div/header/div[2]/div[2]/a[7]").click()

    driver.implicitly_wait(30)

    # close the browser window
    driver.quit()

    print("Test Completed Successfully.")



