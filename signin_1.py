
# 1.successful signin with valid credentials

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.amazon.in/")

# Wait timeout
wait = WebDriverWait(driver, 10)

try:
    # Wait until the element is present and clickable
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='nav-link-accountList']")))

    # Click the element
    element.click()
    print("Element clicked successfully.")
    time.sleep(20)

    email_fill=driver.find_element(By.XPATH, "//input[@id='ap_email_login']")
    email_fill.send_keys("yourmail@gmail.com")
    print("Email filled successfully.")

    continue_but=driver.find_element(By.XPATH,'//span[@id="continue"]//input[@class="a-button-input"]')
    continue_but.click()
    print("Continue button clicked successfully.")

    # Wait until the URL changes to the specific sign-in URL
    wait.until(EC.url_contains("https://www.amazon.in/ap/signin"))
    print("Navigated to the sign-in page.")
    time.sleep(20)

    # fill password
    password_fill = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
    password_fill.send_keys("YourPasswordHere")
    print("Password filled successfully.")
    time.sleep(15)
    # enter sign-in and validate credentials
    signInSubmit = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='signInSubmit']")))
    signInSubmit.click()
    print("Sign-in button clicked successfully.")

# know where it redirects
    time.sleep(20)

except Exception as e:
    print("Exception occurred:")
    print(e)

# Close the browser
driver.quit()


