from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

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
    email_1 = "yourmail@gmail.com"
    email_fill = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='ap_email_login']")))
    time.sleep(5)
    email_fill.send_keys(email_1)
    print("Email filled successfully->",email_fill.text)

    continue_but=driver.find_element(By.XPATH,'//span[@id="continue"]//input[@class="a-button-input"]')
    time.sleep(5)
    continue_but.click()
    print("Continue button clicked successfully.")

    # Wait until the URL changes to the specific sign-in URL
    wait.until(EC.url_contains("https://www.amazon.in/ap/signin"))
    print("Navigated to the sign-in page.")
    time.sleep(15)
    # click forgot password
    fgt_pwd = driver.find_element(By.ID,"auth-fpp-link-bottom")
    time.sleep(5)
    fgt_pwd.click()
    print("Forgot Password clicked successfully.")
    time.sleep(10)
    email_fill = driver.find_element(By.XPATH, "//input[@id='ap_email']")
    time.sleep(5)
    email_fill.clear()
    email_fill.send_keys("yourmail@gmail.com")
    print("Email filled successfully.")
    # verifying with wrong OTP
    time.sleep(10)
    clk_continue= driver.find_element(By.XPATH,"//input[@id='continue']")
    clk_continue.click()
    time.sleep(10)
    otp_input = driver.find_element(By.ID,"cvf-input-code")
    # Generate a 6-digit numeric OTP to give wrong OTP
    otp_rand = random.randint(100000, 999999)
    time.sleep(5)
    otp_input.send_keys(str(otp_rand))
    print("OTP entered:",otp_rand)
    time.sleep(5)
    clk_continue = driver.find_element(By.XPATH,"//input[@aria-label='Verify OTP Button']")
    clk_continue.click()
    print("verify OTP button clicked successfully.")
    time.sleep(5)
    # Locate alert message
    alert_message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "//div[@class='a-row a-spacing-micro']//div[@class='a-box a-alert-inline a-alert-inline-error cvf-widget-alert cvf-widget-alert-id-cvf-invalid-code']//div[@class='a-section cvf-alert-section cvf-widget-alert-message']")
        )
    )

    # Check visibility and get text
    is_visible = alert_message_element.is_displayed()
    print("Element is visible:", is_visible)
    alert_message_text = alert_message_element.text
    print("Alert message text:", alert_message_text)
# resend OTP
    print("Resending the OTP...")
    resend_otp = driver.find_element(By.ID, "cvf-resend-link")
    resend_otp.click()
    time.sleep(5)
    otp_input.send_keys(str(otp_rand))

except Exception as e:
    print("Exception occurred:")
    print(e)
    driver.save_screenshot("error_screenshot.png")
    print("Screenshot saved as error_screenshot.png")
finally:
    driver.quit()