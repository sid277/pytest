import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

password = "admin12345"


@pytest.mark.usefixtures("test_init")
#@pytest.mark.skip(reason="no way of currently testing this")

class BaseTest:
    pass

class Test_Viz(BaseTest):

    def test_editUser(self):

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

        # Click Edit Profile
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/span[2]").click()

        # Enter the new profile details
        first_name = "Jon"
        last_name = "Smith"
        department = "QA"
        company_profile = "Cogni"

        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/input").send_keys(Keys.CONTROL + "a", Keys.DELETE)
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/input").send_keys(first_name)
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/input").send_keys(Keys.CONTROL + "a", Keys.DELETE)
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/input").send_keys(last_name)
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/div/div/input").send_keys(Keys.CONTROL + "a", Keys.DELETE)
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/div/div/input").send_keys(department)
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[4]/div/div/div/input").send_keys(Keys.CONTROL + "a", Keys.DELETE)
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[4]/div/div/div/input").send_keys(company_profile)
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[5]/button/span[1]").click()

        wait = WebDriverWait(self.driver, 10)
        loginStatus = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body"))).text
        print("================ Toast Message after Profile Edit: "+loginStatus+" ================")

        self.driver.refresh()

        displayed_name = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/span[2]").text
        assert displayed_name == first_name


    # def test_logoutUser(self):
    #     self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/h5").click()
    #     self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[2]/button[1]/span[1]").click()
    #     actualUrl = self.driver.current_url
    #     expectedUrl = "https://console.cognitensor.com/login"
    #     assert actualUrl == expectedUrl

    # first = self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/input").text
    # print(first)
    # act = ActionChains(self.driver)
    # act.send_keys(Keys.CONTROL).send_keys("a").send_keys(Keys.DELETE).perform()
    # time.sleep(10)
