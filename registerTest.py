from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

base_url = "http://localhost/quiz-pengupil/register.php"

# Test Case 1: Successful Registration
def test_successful_registration():
    driver.get(base_url)
    time.sleep(2)  # Wait for the page to load
    driver.find_element(By.ID, "name").send_keys("Test User")
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "InputEmail").send_keys("testuser@example.com")
    driver.find_element(By.ID, "InputPassword").send_keys("password123")
    driver.find_element(By.ID, "InputRePassword").send_keys("password123")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    assert "index.php" in driver.current_url

# Test Case 2: Empty Fields
def test_empty_fields():
    driver.get(base_url)
    time.sleep(2)  # Wait for the page to load
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
    assert "Data tidak boleh kosong !!" in error_message

# Test Case 3: Passwords Do Not Match
def test_passwords_do_not_match():
    driver.get(base_url)
    time.sleep(2)  # Wait for the page to load
    driver.find_element(By.ID, "name").send_keys("Test User")
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "InputEmail").send_keys("testuser@example.com")
    driver.find_element(By.ID, "InputPassword").send_keys("password123")
    driver.find_element(By.ID, "InputRePassword").send_keys("password456")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    error_message = driver.find_element(By.CLASS_NAME, "text-danger").text
    assert "Password tidak sama !!" in error_message

# Test Case 4: Username Already Exists
def test_username_already_exists():
    driver.get(base_url)
    time.sleep(2)  # Wait for the page to load
    driver.find_element(By.ID, "name").send_keys("Test User")
    driver.find_element(By.ID, "username").send_keys("existinguser")
    driver.find_element(By.ID, "InputEmail").send_keys("testuser@example.com")
    driver.find_element(By.ID, "InputPassword").send_keys("password123")
    driver.find_element(By.ID, "InputRePassword").send_keys("password123")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
    assert "Username sudah terdaftar !!" in error_message

# Test Case 5: Invalid Email Format
def test_invalid_email_format():
    driver.get(base_url)
    time.sleep(2)  # Wait for the page to load
    driver.find_element(By.ID, "name").send_keys("Test User")
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "InputEmail").send_keys("invalidemail")
    driver.find_element(By.ID, "InputPassword").send_keys("password123")
    driver.find_element(By.ID, "InputRePassword").send_keys("password123")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(2)
    error_message = driver.find_element(By.CLASS_NAME, "alert-danger").text
    assert "Invalid email format" in error_message  # Assuming this error message is implemented

# Run the test cases
test_successful_registration()
test_empty_fields()
test_passwords_do_not_match()
test_username_already_exists()
test_invalid_email_format()

# Close the WebDriver
driver.quit()