from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pwdgenerator import generate_password
import pandas as pd



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

    email_fill = driver.find_element(By.XPATH, "//input[@id='ap_email_login']")
    user_mail = "secondmail@gmail.com"
    email_fill.send_keys(user_mail)
    print("Email filled successfully.")

    continue_but = driver.find_element(By.XPATH, '//span[@id="continue"]//input[@class="a-button-input"]')
    continue_but.click()
    print("Continue button clicked successfully.")

    # Wait until the URL changes to the specific sign-in URL
    wait.until(EC.url_contains("https://www.amazon.in/ax/claim/intent"))
    print("Navigated to the create account page.")
    time.sleep(20)

    create_acct = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
    create_acct.click()
    print("Create account clicked successfully.")
    time.sleep(20)

    dropdown_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='a-button-inner']"))
    )
    dropdown_button.click()
    print("Dropdown clicked successfully.")

    # Wait for the dropdown options to be visible
    time.sleep(10)  # Adjust if necessary

    # Select an option from the dropdown
    option_to_select = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//li[@class='a-dropdown-item']//a[@id='auth-country-picker_92']"))
    )
    option_to_select.click()
    print("Option 'India (+91)' selected successfully.")

    phone_num = driver.find_element(By.ID, "ap_phone_number")
    phone_num.send_keys("123456789") # replace number
    print("Phone number entered:", phone_num.get_attribute('value'))

    cust_name = driver.find_element(By.ID, "ap_customer_name")
    cust_name.send_keys("Your name")

    password = generate_password(length=16, use_special_chars=True)
    print("Generated password:", password)

    passwd = driver.find_element(By.ID, "ap_password")
    passwd.send_keys(password)

    # Collect the details to store
    data = {
        "Phone Number": [phone_num.get_attribute('value')],
        "Customer Name": [cust_name.get_attribute('value')],
        "Password": [password]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Save to Excel
    df.to_excel("user_details.xlsx", index=False)

    print("User details saved to Excel file successfully.")

    # Click the continue button
    continue_clk = driver.find_element(By.XPATH, "//input[@id='continue']")
    continue_clk.click()
    print("Continue button clicked successfully.")

except Exception as e:
    print("Exception occurred:")
    print(e)

# Close the browser
driver.quit()
#Option 'India (+91)' selected successfully.
# Phone number entered: 123456789
# Generated password: bsT[e7a~fhVkp`Q:
