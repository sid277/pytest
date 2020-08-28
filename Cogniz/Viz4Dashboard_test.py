import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

password = "admin12345"
expected_dashboard = "test_board1"


@pytest.mark.usefixtures("test_init")
#@pytest.mark.skip(reason="no way of currently testing this")

class BaseTest:
    pass


class Test_Viz(BaseTest):

    def test_dashboard(self):

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

        self.driver.implicitly_wait(20)

        # Click Viz link
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[1]/div/a[2]").click()

        # Click dashboard option in sidebar
        self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[1]/div/a[2]/div/span").click()

        no_of_dashboards_in = str(len(self.driver.find_elements_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[2]/div[2]/div/div/a")))
        no_of_dashboards_out = self.driver.find_element_by_xpath("//*[@id=\"dashboard\"]/div/div[2]/div[1]/div/a[2]/span").text

        assert no_of_dashboards_in == no_of_dashboards_out


    def test_selectDashboard(self):

        # Click the desired dashboard with text "expected_dashboard"
        self.driver.find_element_by_link_text(expected_dashboard).click()

        actual_dashboard = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/span").text

        assert expected_dashboard == actual_dashboard

    def test_countTabs(self):

        # Count the div containing the components
        actual_no_tabs = len(self.driver.find_elements_by_class_name("MuiTab-wrapper"))
        print("================== Total number of Tabs in dashboard: " + str(actual_no_tabs) + " =======================")

        if actual_no_tabs == 0:
            print("There is no tab in the dashboard")

        else:
            for tab in range(actual_no_tabs):
                self.driver.switch_to.default_content()

                # Click the tab link at the top
                self.driver.find_element_by_xpath("//*[@id=\"simple-tab-{}\"]".format(tab)).click()

                # Get the name of the tab
                tab_name = self.driver.find_element_by_xpath("//*[@id=\"simple-tab-{}\"]/span[1]".format(tab)).text

                # Count the number of components in the tab
                actual_components_in_tab = len(self.driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[2]/div"))

                print("===========================================")
                print(" Total Components in {}: ".format(tab_name) + str(actual_components_in_tab))

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
                print("No_of_tabs not showing data in tab {}: ".format(tab_name) + str(no_data_tab_count))

                # Click filter button
                self.driver.find_element_by_xpath("//*[@id=\"dashboard-tab\"]/div[2]/div[1]/button").click()

                # Count number of filters available
                no_of_filters = len(self.driver.find_elements_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div"))

                print("No_of_Filters available in tab {}: ".format(tab_name) + str(no_of_filters))

                wait = WebDriverWait(self.driver, 10)
                wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id=\"dashboard-tab\"]/div[2]/div[1]/div/div/div[1]/span/div/button[2]"))).click()

                #self.driver.find_element_by_xpath("//*[@id=\"dashboard-tab\"]/div[2]/div[1]/div/div/div[1]/span/div/button[2]").click()

                print("===========================================")

                # alert1 = "alert('Total Components with no data in tab2 = {}')".format(no_data_tab_count)
                # self.driver.execute_script(alert1)
                # time.sleep(3)
                # self.driver.switch_to.alert.accept()
                # self.driver.switch_to.default_content()
