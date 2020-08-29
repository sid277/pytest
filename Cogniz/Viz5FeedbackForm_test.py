import random
from selenium.webdriver.support import expected_conditions as ec
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

password = "admin12345"

@pytest.mark.usefixtures("test_init")
#@pytest.mark.skip(reason="no way of currently testing this")

class BaseTest:
    pass

class Test_Viz(BaseTest):

    def test_feedback(self):

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

        # Click Feedback at the bottom
        self.driver.find_element_by_xpath('//*[@id="dashboard"]/div/div[2]/div[1]/div/div/a/div/span').click()

        expected_url = "https://console.cognitensor.com/athena/feedback"

        actual_url = self.driver.current_url

        assert actual_url==expected_url

    def test_RateCogniViz(self):

        # Click the svg icon to open
        self.driver.find_element_by_xpath('//*[@id="panel1bh-header"]/div[2]').click()

        # Select the star rating and review
        star_rating = 4
        review_list = ["Test Review1", "Test Review2", "Test Review3", "Test Review4"]
        review_text = random.choice(review_list)

        # Click the star rating system and enter review
        self.driver.find_element_by_xpath(
            "//*[@id=\"panel1bh-content\"]/div/div/span[2]/label[{}]".format(star_rating)).click()
        self.driver.find_element_by_xpath("//*[@id=\"panel1bh-content\"]/div/div/div/div/textarea").send_keys(
            review_text)
        self.driver.find_element_by_xpath("//*[@id=\"panel1bh-content\"]/div/div/button[1]/span[1]").click()

        wait = WebDriverWait(self.driver, 10)
        loginStatus = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body"))).text
        print("================ Toast Message after Rate Cogniviz form: " + loginStatus + " ================")

        assert loginStatus=="Thanks for the review!"

    def test_HelpUsImprove(self):

        # Click the svg icon to open
        self.driver.find_element_by_xpath('//*[@id="panel2bh-header"]/div[2]').click()

        # Enter the Title and description for change
        title = "Testing Title"
        change_list = ["Test Change1", "Test Change2", "Test Change3", "Test Change4"]
        change_text = random.choice(change_list)

        # Click the star rating system and enter review
        try:
            self.driver.find_element_by_xpath(
                "//*[@id=\"panel2bh-content\"]/div/div/div[1]/div/input").send_keys(title)
            self.driver.find_element_by_xpath("//*[@id=\"panel2bh-content\"]/div/div/div[2]/div/textarea").send_keys(
                change_text)
            self.driver.find_element_by_xpath("//*[@id=\"panel2bh-content\"]/div/div/button[1]/span[1]").click()

            wait = WebDriverWait(self.driver, 10)
            loginStatus = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body"))).text
            print("================ Toast Message after HelpUsImprove feedback form: " + loginStatus + " ================")
        except Exception as e:
            print(e)

        assert loginStatus == "Thanks for the review!"

    def test_Help(self):

        # Click the svg icon to open
        self.driver.find_element_by_xpath('//*[@id="panel3bh-header"]/div[2]').click()

        # Enter the Title and description for change
        title = "Testing Title"
        exp_list = ["Test Explanation1", "Test Explanation2", "Test Explanation3", "Test Explanation4"]
        exp_text = random.choice(exp_list)

        # Click the star rating system and enter review
        try:
            self.driver.find_element_by_xpath(
                "//*[@id=\"panel3bh-content\"]/div/div/div[1]/div/input").send_keys(title)
            #self.driver.find_element_by_xpath("//*[@id=\"panel3bh-content\"]/div/div/div[2]/div/div/div/button[2]/span[1]").click()
            #select = Select(self.driver.find_element_by_xpath("//*[@id=\"mui-44433\"]"))
            #select.select_by_index(2)
            #options = len(self.driver.find_elements_by_css_selector("aria-activedescendant"))
            # mui-44433-option-3

            self.driver.find_element_by_xpath("//*[@id=\"panel3bh-content\"]/div/div/div[3]/div/textarea").send_keys(
                exp_text)
            self.driver.find_element_by_xpath("//*[@id=\"panel3bh-content\"]/div/div/button[1]/span[1]").click()

            wait = WebDriverWait(self.driver, 10)
            loginStatus = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "Toastify__toast-body"))).text
            print("================ Toast Message after Help feedback form: " + loginStatus + " ================")
        except Exception as e:
            print(e)

        assert loginStatus == "Thanks for the review!"

