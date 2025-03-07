import unittest, sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By

class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        server = 'http://localhost:4444'

        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

        if len(sys.argv) > 1:
            self.base_url = sys.argv[1]
        else:
            self.base_url = "http://localhost/register.php"

    def test_successful_registration(self):
        self.browser.get(self.base_url)
        print(self.browser.page_source)
        time.sleep(2)
        self.browser.find_element(By.ID, "name").send_keys("Test User")
        self.browser.find_element(By.ID, "username").send_keys("testuser")
        self.browser.find_element(By.ID, "InputEmail").send_keys("testuser@example.com")
        self.browser.find_element(By.ID, "InputPassword").send_keys("password123")
        self.browser.find_element(By.ID, "InputRePassword").send_keys("password123")
        self.browser.find_element(By.NAME, "submit").click()
        time.sleep(2)
        self.assertIn("index.php", self.browser.current_url)

    def test_empty_fields(self):
        self.browser.get(self.base_url)
        print(self.browser.page_source)
        time.sleep(2)
        self.browser.find_element(By.NAME, "submit").click()
        time.sleep(2)
        error_message = self.browser.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Data tidak boleh kosong !!", error_message)

    def test_passwords_do_not_match(self):
        self.browser.get(self.base_url)
        print(self.browser.page_source)
        time.sleep(2)
        self.browser.find_element(By.ID, "name").send_keys("Test User")
        self.browser.find_element(By.ID, "username").send_keys("testuser")
        self.browser.find_element(By.ID, "InputEmail").send_keys("testuser@example.com")
        self.browser.find_element(By.ID, "InputPassword").send_keys("password123")
        self.browser.find_element(By.ID, "InputRePassword").send_keys("password456")
        self.browser.find_element(By.NAME, "submit").click()
        time.sleep(2)
        error_message = self.browser.find_element(By.CLASS_NAME, "text-danger").text
        self.assertIn("Password tidak sama !!", error_message)

    def test_username_already_exists(self):
        self.browser.get(self.base_url)
        print(self.browser.page_source)
        time.sleep(2)
        self.browser.find_element(By.ID, "name").send_keys("Test User")
        self.browser.find_element(By.ID, "username").send_keys("existinguser")
        self.browser.find_element(By.ID, "InputEmail").send_keys("testuser@example.com")
        self.browser.find_element(By.ID, "InputPassword").send_keys("password123")
        self.browser.find_element(By.ID, "InputRePassword").send_keys("password123")
        self.browser.find_element(By.NAME, "submit").click()
        time.sleep(2)
        error_message = self.browser.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Username sudah terdaftar !!", error_message)

    def test_invalid_email_format(self):
        self.browser.get(self.base_url)
        print(self.browser.page_source)
        time.sleep(2)
        self.browser.find_element(By.ID, "name").send_keys("Test User")
        self.browser.find_element(By.ID, "username").send_keys("testuser")
        self.browser.find_element(By.ID, "InputEmail").send_keys("invalidemail")
        self.browser.find_element(By.ID, "InputPassword").send_keys("password123")
        self.browser.find_element(By.ID, "InputRePassword").send_keys("password123")
        self.browser.find_element(By.NAME, "submit").click()
        time.sleep(2)
        error_message = self.browser.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Invalid email format", error_message)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')