from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (Ensure you have ChromeDriver installed)
driver = webdriver.Chrome()

# Open the Swag Labs Website
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)  # Wait for page to load

# Step 1: Login to the website
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()
time.sleep(2)

# Step 2: Add an item to the cart
add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_to_cart_button.click()
time.sleep(2)

# Step 3: Go to the cart
cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_button.click()
time.sleep(2)

# Step 4: Proceed to checkout
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()
time.sleep(2)

# Step 5: Enter checkout information
first_name = driver.find_element(By.ID, "first-name")
last_name = driver.find_element(By.ID, "last-name")
postal_code = driver.find_element(By.ID, "postal-code")

first_name.send_keys("kavya")
last_name.send_keys("s")
postal_code.send_keys("12345")

#first_name.send_keys("John")
#last_name.send_keys("Doe")
#postal_code.send_keys("12345")

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()
time.sleep(2)

# Step 6: Complete the purchase
finish_button = driver.find_element(By.ID, "finish")
finish_button.click()
time.sleep(2)

# Success Message
print("Test completed successfully!")

# Close the browser
driver.quit()
