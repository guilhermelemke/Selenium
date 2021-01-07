from selenium.webdriver import Firefox
from time import sleep
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..")) # ".." two nested folders, depends on structure
from POM.Pages.loginPage import LoginPage
from POM.Pages.homePage import HomePage
import HtmlTestRunner


class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.driver = Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver

        driver.get('https://opensource-demo.orangehrmlive.com')

        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()

        homepage = HomePage(driver)
        sleep(1)
        homepage.click_welcome()
        sleep(1)
        homepage.click_logout()
        sleep(2)

    def test_02_login_invalid(self):
        driver = self.driver

        driver.get('https://opensource-demo.orangehrmlive.com')

        login = LoginPage(driver)
        login.enter_username('Admin1')
        login.enter_password('admin123')
        login.click_login()
        message = driver.find_element_by_xpath("").text
        self.assertEqual(message, "Invalid credentials123")
        sleep(2)

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print('Test Completed')


# if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/320084928/Documents/Work Folder/Dev/Python/Selenium/Selenium/POM/reports"))

# python3 -m unittest login.py
