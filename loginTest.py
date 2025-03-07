import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleTestCase(unittest.TestCase):
    def setUp(self):
        # Configure Firefox for remote WebDriver
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        server = 'http://localhost:4444'
        
        self.browser = webdriver.Remote(command_executor=server, options=options)

    def test_successful_login(self):
        # If a URL was passed via command line, use it; otherwise default
        if len(sys.argv) > 1:
            url = sys.argv[1] + "/login.php"
        else:
            url = "http://localhost/login.php"

        self.browser.get(url)
        self.browser.find_element(By.ID, "username").send_keys("valid_username")
        self.browser.find_element(By.ID, "InputPassword").send_keys("valid_password")
        self.browser.find_element(By.NAME, "submit").click()
        self.assertIn("index.php", self.browser.current_url)

    def test_empty_username_password(self):
        if len(sys.argv) > 1:
            url = sys.argv[1] + "/login.php"
        else:
            url = "http://localhost/login.php"

        self.browser.get(url)
        self.browser.find_element(By.NAME, "submit").click()
        error_message = self.browser.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertEqual(error_message, "Data tidak boleh kosong !!")

    def test_invalid_username(self):
        if len(sys.argv) > 1:
            url = sys.argv[1] + "/login.php"
        else:
            url = "http://localhost/login.php"

        self.browser.get(url)
        self.browser.find_element(By.ID, "username").send_keys("invalid_username")
        self.browser.find_element(By.ID, "InputPassword").send_keys("any_password")
        self.browser.find_element(By.NAME, "submit").click()
        error_message = self.browser.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertEqual(error_message, "Register User Gagal !!")

    def test_invalid_password(self):
        if len(sys.argv) > 1:
            url = sys.argv[1] + "/login.php"
        else:
            url = "http://localhost/login.php"

        self.browser.get(url)
        self.browser.find_element(By.ID, "username").send_keys("valid_username")
        self.browser.find_element(By.ID, "InputPassword").send_keys("invalid_password")
        self.browser.find_element(By.NAME, "submit").click()
        error_message = self.browser.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertEqual(error_message, "Register User Gagal !!")

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')