import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox(executable_path="./geckodriver")
'''driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon abcd")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()close'''
class DemoMaharaOrgLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="./geckodriver")
    def test_valid_login(self):
        driver = self.driver
        driver.get("http://demo.mahara.org/")
        self.assertIn("Home - Mahara", driver.title)
        username = driver.find_element_by_id("login_login_username")
        username.send_keys("student2")
        password=driver.find_element_by_id("login_login_password")
        password.send_keys("TestCaseing1")
        loginbutton = driver.find_element_by_id("login_submit")
        loginbutton.click()
        self.assertTrue(driver.find_element_by_link_text("Logout"),"Logout link")
    def test_password_required_message(self):
        driver = self.driver
        driver.get("http://demo.mahara.org/")
        username= driver.find_element_by_id("login_login_username")
        username.send_keys("student2")
        loginbutton=driver.find_element_by_id("login_submit")
        loginbutton.click()
        time.sleep(3)
        self.assertTrue(driver.find_element_by_id("login_login_password_error"),"This field is required.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
