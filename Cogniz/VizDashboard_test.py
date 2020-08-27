import time
from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

password = "admin12345"

#
# @pytest.fixture(params=["firefox", "chrome"], scope='class')
# def test_init(request):
#     # open browser window
#     global driver
#     if request.param == "firefox":
#         driver = webdriver.Firefox(executable_path="D:/Installed Apps/Webdrivers/geckodriver-v0.26.0-win64/geckodriver.exe")
#     if request.param == "chrome":
#         driver = webdriver.Chrome(executable_path="D:/Installed Apps/Webdrivers/chromedriver_win32/chromedriver.exe")
#     # if request.param == "opera":
#     #     driver = webdriver.Opera(executable_path="D:/Installed Apps/Webdrivers/operadriver_win64/operadriver.exe")
#     # if request.param == "edge":
#     #     driver = webdriver.Edge(executable_path="D:/Installed Apps/Webdrivers/edgedriver_win64/msedgedriver.exe")
#     # if request.param == "ie":
#     #     driver = webdriver.Ie(executable_path="D:/Installed Apps/Webdrivers/IEDriverServer_x64_3.150.1/IEDriverServer.exe")
#     driver.maximize_window()
#
#     # yield is used to call all the linked functions with current function through fixture
#     yield driver
#     # driver.implicitly_wait(10)
#
#     # close the browser in the end
#     driver.quit()


@pytest.mark.usefixtures("test_init")
class BaseTest:
    pass

class Test_Viz(BaseTest):

    def test_dashboard(self):
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

        actual_dashboard = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/span").text

        assert expected_dashboard == actual_dashboard

    def test_countTabs(self):

        # Count the div containing the components
        actual_no_tabs = len(self.driver.find_elements_by_class_name("MuiTab-wrapper"))
        print("================== Total number of Tabs in dashboard: " + str(actual_no_tabs) + " =======================")

        if actual_no_tabs == 0:
            print("There is no tab in the dashboard")

        elif actual_no_tabs == 1:

            actual_components_tab1 = len(self.driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div"))
            # alert = "alert('Total Components in tab1 = {}')".format(actual_components_tab1)
            print("=================== Total Components in tab1" + str(actual_components_tab1) + " ============================")
            # self.driver.execute_script(alert)
            # time.sleep(4)
            # self.driver.switch_to.alert.accept()
            # self.driver.switch_to.default_content()
            no_data_tab_count = 0
            for com in range(actual_components_tab1):
                com_div = com + 1

                try:
                    large_view_icon = self.driver.find_element_by_xpath("//*[@id=\"dashboard-tab\"]/div[2]/div[2]/div[{}]/div[1]/div/div/i".format(com_div)).is_displayed()
                    if large_view_icon:
                        self.driver.find_element_by_xpath("//*[@id=\"dashboard-tab\"]/div[2]/div[2]/div[{}]/div[1]/div/div/i".format(com_div)).click()
                        time.sleep(3)
                        self.driver.find_element_by_css_selector("body > div.ui.page.modals.dimmer.transition.visible.active > div > i").click()
                    else:
                        com_div = com_div + 1
                except Exception as e:
                    pass
                    #print(e)

                try:
                    if self.driver.find_element_by_xpath("//*[@id=\"dashboard-tab\"]/div[2]/div[2]/div[{}]/div[2]/div/span".format(com_div)).is_enabled():
                        no_data_tab_count = no_data_tab_count + 1
                except Exception as e:
                    pass
                    #print(e)

                #self.driver.switch_to.default_content()

            print("============= No_of_tabs not showing data in tab1 : " + str(no_data_tab_count) + " ===================")
            # alert1 = "alert('Total Components with no data in tab1 = {}')".format(no_data_tab_count)
            # self.driver.execute_script(alert1)
            # time.sleep(3)
            # self.driver.switch_to.alert.accept()
            # self.driver.switch_to.default_content()

        else:
            for tab in range(actual_no_tabs):
                self.driver.switch_to.default_content()
                self.driver.find_element_by_xpath("//*[@id=\"simple-tab-{}\"]".format(tab)).click()
                actual_components_in_tab = len(self.driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div"))
                print("=================== Total Components in tab {}: ".format(tab) + str(actual_components_in_tab) + " ============================")
                # alert = "alert('Total Components in tab2 = {}')".format(actual_components_tab2)
                # self.driver.execute_script(alert)
                # time.sleep(3)
                # self.driver.switch_to.alert.accept()
                # self.driver.switch_to.default_content()
                no_data_tab_count = 0
                for com in range(actual_components_in_tab):
                    com_div = com + 1

                    try:
                        large_view_icon = self.driver.find_element_by_xpath("//*[@id=\"dashboard-tab\"]/div[2]/div[2]/div[{}]/div[1]/div/div/i".format(com_div)).is_displayed()
                        if large_view_icon:
                            pass
                            # self.driver.find_element_by_xpath("//*[@id=\"dashboard-tab\"]/div[2]/div[2]/div[{}]/div[1]/div/div/i".format(com_div)).click()
                            # time.sleep(3)
                            # self.driver.find_element_by_css_selector("body > div.ui.page.modals.dimmer.transition.visible.active > div > i").click()
                        else:
                            com_div = com_div + 1
                    except Exception as e:
                        pass

                    try:
                        if self.driver.find_element_by_xpath("//*[@id=\"dashboard-tab\"]/div[2]/div[2]/div[{}]/div[2]/div/span".format(com_div)).is_enabled():
                            no_data_tab_count = no_data_tab_count + 1
                    except Exception as e:
                        pass

                    self.driver.switch_to.default_content()

                print("============= No_of_tabs not showing data in tab {}: ".format(tab) + str(no_data_tab_count) + " ===================")
                # alert1 = "alert('Total Components with no data in tab2 = {}')".format(no_data_tab_count)
                # self.driver.execute_script(alert1)
                # time.sleep(3)
                # self.driver.switch_to.alert.accept()
                # self.driver.switch_to.default_content()
