# web-scraping-addtocart
Swag Labs E2E Automation with Selenium

This Python script automates a complete purchase flow on the [Swag Labs demo website](https://www.saucedemo.com/) using Selenium WebDriver. It logs in, adds a product to the cart, proceeds through checkout, and completes the purchase.

---

## Features

- Opens the Swag Labs demo website
- Logs in with valid credentials
- Adds the "Sauce Labs Backpack" item to the cart
- Navigates to the cart and proceeds to checkout
- Fills in user checkout information
- Completes the purchase
- Prints a success message upon completion
- Closes the browser automatically

---

## Requirements

- Python 3.x
- Selenium
- Chrome browser
- ChromeDriver compatible with your Chrome version (make sure `chromedriver` is in your system PATH)

---

## Installation

1. Install Selenium:
   ```bash
   pip install selenium
2. Download ChromeDriver and add it to your system PATH.
Usage

Clone this repository or download the script file.

Run the script:

python sladdtocart.py
The script will open a Chrome browser window, perform the entire checkout flow on the Swag Labs website, print "Test completed successfully!", then close the browser.
