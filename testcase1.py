from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



# Set up Chrome
driver = webdriver.Chrome()


# Open the login page
driver.get("https://the-internet.herokuapp.com/login")

# Find and fill the username and password fields
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Submit the form
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Verify login success
try:
    success_message = driver.find_element(By.ID, "flash").text
    if "You logged into a secure area!" in success_message:
        print("Login Test Passed")
    else:
        print("Login Test Failed")
except Exception as e:
    print("Error during login verification:", e)

# Close the browser
driver.quit()
