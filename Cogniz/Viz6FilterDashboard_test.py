import time
import pytest

password = "admin12345"

@pytest.mark.usefixtures("test_init")
@pytest.mark.skip(reason="no way of currently testing this")
class BaseTest:
    pass

class Test_Viz(BaseTest):

    def test_filters(self):
        expected_dashboard = "test_board1"

        # navigate to the application home page
        self.driver.get("https://cognitensor.com/")

        # click login
        self.driver.find_element_by_xpath("/html/body/div/div/div/header/div[2]/div[2]/a[7]").click()
        self.driver.implicitly_wait(20)

        # fill login form
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div/input').send_keys(
            "qatester@cognitensor.com")
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/input').send_keys(
            password)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[3]/div/button/span[1]').click()
        self.driver.implicitly_wait(20)

        self.driver.implicitly_wait(20)

        # Click Viz link
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[1]/div/a[2]").click()

        # Click dashboard option in sidebar
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[1]/div/a[2]/div/span").click()

        # Click the desired dashboard with text "expected_dashboard"
        self.driver.find_element_by_link_text(expected_dashboard).click()

        # Click filter button
        self.driver.find_element_by_xpath("//*[@id=\"dashboard-tab\"]/div[2]/div[1]/button").click()

        # Count number of filters available
        no_of_filters = len(self.driver.find_elements_by_class_name("five wide computer sixteen wide mobile column"))

        print(no_of_filters)

