import pytest
password = "admin12345"

@pytest.mark.usefixtures("test_init")
class BaseTest:
    pass

class Test_Viz(BaseTest):

    def test_login(self):

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

        # get text appears in the landing page for assertion
        actualHead = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/h2").text
        expectedHead = "Deep Optics"
        assert actualHead == expectedHead