# FILE: loginTest.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_successful_login(self):
        driver = self.driver
        driver.get("http://localhost/login.php")
        driver.find_element(By.ID, "username").send_keys("valid_username")
        driver.find_element(By.ID, "InputPassword").send_keys("valid_password")
        driver.find_element(By.NAME, "submit").click()
        self.assertIn("index.php", driver.current_url)

    def test_empty_username_password(self):
        driver = self.driver
        driver.get("http://localhost/login.php")
        driver.find_element(By.NAME, "submit").click()
        error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertEqual(error_message, "Data tidak boleh kosong !!")

    def test_invalid_username(self):
        driver = self.driver
        driver.get("http://localhost/login.php")
        driver.find_element(By.ID, "username").send_keys("invalid_username")
        driver.find_element(By.ID, "InputPassword").send_keys("any_password")
        driver.find_element(By.NAME, "submit").click()
        error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertEqual(error_message, "Register User Gagal !!")

    def test_invalid_password(self):
        driver = self.driver
        driver.get("http://localhost/login.php")
        driver.find_element(By.ID, "username").send_keys("valid_username")
        driver.find_element(By.ID, "InputPassword").send_keys("invalid_password")
        driver.find_element(By.NAME, "submit").click()
        error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertEqual(error_message, "Register User Gagal !!")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()