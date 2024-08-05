"""test_OrangeHrm pytest file which includes 5 testcases"""
# imported Locator class
from TestLocators.OrangeHrm_Locators import Locators
# imported Input data class
from TestData.OrangeHrm_Data import InputData
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import pytest


class Test_OrangeHrmPage:
    # booting function to call starting of every testcase
    @pytest.fixture
    def booting_fun(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.alert = Alert(self.driver)

        yield
        self.driver.close()

    # Login testcase
    def test_login(self, booting_fun):
        try:
            self.driver.get(InputData().url)
            username = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().username)))
            password = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().password)))
            submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().login)))
            username.send_keys(InputData().username)
            password.send_keys(InputData().password)
            submit_button.click()
        except (NoSuchElementException, TimeoutException) as e:
            print(e)

    # forgot password testcase
    def test_forgot_password(self, booting_fun):
        try:
            self.driver.get(InputData().url)
            forgot_password = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().forgot_link)))
            forgot_password.click()
            username = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().username)))
            username.send_keys(InputData().username)
            reset_button = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Reset_password)))
            reset_button.click()
            reset_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().reset_msg))).text
            assert reset_msg == InputData().text_msg
            print("Pass, forgot password testcase")

        except NoSuchElementException as e:
            print(e)

    # header validation testcase
    def test_header_validation(self, booting_fun):
        try:
            self.test_login(booting_fun)
            admin = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().admin)))
            admin.click()
            user_management = self.wait.until(
                EC.presence_of_element_located((By.XPATH, Locators().user_management)))
            Job = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().Job)))
            Organization = self.wait.until(
                EC.presence_of_element_located((By.XPATH, Locators().Organization)))
            qualify = self.wait.until(
                EC.presence_of_element_located((By.XPATH, Locators().qualify)))

            nationality = self.wait.until(
                EC.presence_of_element_located((By.XPATH, Locators().Nationality_link)))
            configuration = self.wait.until(
                EC.presence_of_element_located((By.XPATH, Locators().configuration)))
            corporate_banking = self.wait.until(
                EC.presence_of_element_located((By.XPATH, Locators().corporate_bank)))
            header_list_validation = [user_management, Job, Organization, qualify, nationality,
                                      configuration,
                                      corporate_banking]
            for i in header_list_validation:
                if i.is_displayed():
                    print("pass,header validation testcase")
                else:
                    print("issue in validation")

        except NoSuchElementException as e:
            print(e)

    # main menu validation testcase
    def test_main_menu_validation(self, booting_fun):
        try:
            self.test_login(booting_fun)
            admin_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().admin))).text
            pim_text = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().pim))).text
            leave_text = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().leave))).text
            time_text = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().Time))).text
            recruitment_text = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().recruitment))).text
            my_info_text = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().my_info))).text
            performance_text = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().performance))).text
            dashboard_text = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().dashboard))).text
            directory_text = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().directory))).text
            maintenance_text = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().maintenance))).text
            claim_text = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().claim))).text
            buzz_text = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().buzz))).text
            menu_validation = [admin_text, pim_text, leave_text, time_text, recruitment_text, my_info_text,
                               performance_text,
                               dashboard_text, directory_text, maintenance_text, claim_text, buzz_text]
            print(menu_validation)
            assert menu_validation == InputData.menu_list
            print("pass, menu validation testcase")
        except NoSuchElementException as e:
            print(e)
