# 6.3. switch to another user

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
    user_mail="yourmail@gmail.com"
    email_fill.send_keys(user_mail)
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
    # wrong password error message
    # Wait for the error message to appear
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='a-box-inner a-alert-container']//span[@class='a-list-item']")))

    # Capture the error text
    error_text = error_message.text
    print(f"Captured error message: {error_text}")

    # Verify if the error message is correct
    if "Your password is incorrect" in error_text:
        print("Error message verified: Password is incorrect.")
        # change if password is incorrect
        change_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Change")))
        change_link.click()
        print("Change link clicked successfully.")
        time.sleep(20)
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "ap_email_login")))
        email_change = email_field.get_attribute("value")
        if user_mail == email_change:
            user_mail2 = "secondmail@gmail.com"
            email_field.send_keys(user_mail2)
            print("email changed from ",user_mail," to ",user_mail2)
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
            wait.until(EC.url_contains("https://www.amazon.in/?ref_=nav_ya_signin"))
            print("Sign-in button clicked successfully.")


    else:
        print("Unexpected error message.")

# know where it redirects
    time.sleep(20)

except Exception as e:
    print("Exception occurred:")
    print(e)

# Close the browser
driver.quit()



