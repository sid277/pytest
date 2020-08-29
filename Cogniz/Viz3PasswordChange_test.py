import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

password = "admin12345"

@pytest.mark.usefixtures("test_init")
#@pytest.mark.skip(reason="no way of currently testing this")

class BaseTest:
    pass

class Test_Viz(BaseTest):

    def test_changePassword(self):

        # navigate to the application home page
        self.driver.get("https://cognitensor.com/")

        # click login
        self.driver.find_element_by_xpath("/html/body/div/div/div/header/div[2]/div[2]/a[7]").click()
        self.driver.implicitly_wait(20)

        # fill login form
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/input').send_keys("qatester@cognitensor.com")
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/input').send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[3]/div/button/span[1]').click()
        self.driver.implicitly_wait(20)

        # Click the "Viz" at the top to navigate to Cogniviz
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[1]/div/a[2]").click()

        # Click Profile section
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[1]/div/a[1]/div/span").click()

        # Click Settings option in profile tab
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/button[3]/span").click()

        # Clear the input box and enter the current password
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/input").clear()
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/input").send_keys(password)

        # clear the input box and enter the new password
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/input").clear()
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/input").send_keys(password)

        # clear the input box and re-enter the new password
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/input").clear()
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/input").send_keys(password)

        # click submit button
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/button/span[1]").click()

        # wait and get the text of toast message
        wait = WebDriverWait(self.driver, 10)
        toast = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body"))).text
        print("================= Toast Message after Password Change: "+toast+" ==========================")

        # Logout and login again to verify changed password

        # Logout
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/h5").click()
        self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[2]/button[1]/span[1]").click()

        # Login again
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/input').send_keys("qatester@cognitensor.com")
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/input').send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[3]/div/button/span[1]').click()

        actualHead = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/h2").text
        expectedHead = "Deep Optics"
        assert actualHead == expectedHead
