import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

config = {
    'EMAIL': '20190208@yopmail.com',
    'PASSWORD': 'accfortest0208'
}

login_url = 'http://www.amazon.com/'


class SignInOut(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_sign_in_function(self):
        driver = self.driver
        driver.get(login_url)
        # Wait for data toaster to appear, then click it
        data_toaster = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='nav-main']/div[1]/div[2]/div/div[3]/span[1]/span")))
        data_toaster.click()
        # Find sign-in button in main page and then click it
        sign_in_button = driver.find_element_by_id('nav-link-accountList')
        sign_in_button.click()
        # Enter account
        driver.find_element_by_id('ap_email').send_keys(config['EMAIL'])
        # Enter password
        driver.find_element_by_id('ap_password').send_keys(config['PASSWORD'])
	    # Click submit button (id=signInSubmit)
        driver.find_element_by_id('signInSubmit').click()
	    # Find user info
        user_info = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='nav-link-accountList']/span[1]")))
    
        # Assert if user info shows in main page. If it fails, selenium will display "AssertionError".
        assert "Hello, William" in user_info.text

    def tearDown(self):
        self.driver.close()
    
if __name__ == '__main__':
    unittest.main()