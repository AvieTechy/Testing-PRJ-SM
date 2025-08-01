import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.safari.webdriver import WebDriver as Safari
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.common.exceptions import StaleElementReferenceException

EMAIL = "customer@practicesoftwaretesting.com"
PASSWORD = "welcome01"

# Load test data with error handling
try:
    df = pd.read_csv("checkout_test_data.csv", on_bad_lines='skip')
    print("CSV loaded successfully. Shape:", df.shape)
except pd.errors.ParserError as e:
    print(f"Error parsing CSV: {e}")
    print("Please check the CSV file for inconsistencies (e.g., extra commas or missing values).")
    exit(1)

# Initialize browsers
browsers = {
    "firefox": lambda: webdriver.Firefox(service=FirefoxService()),
    "safari": lambda: Safari(),
    "chrome": lambda: webdriver.Chrome(service=ChromeService()),
}

# Create logs folder
os.makedirs("logs", exist_ok=True)

# Helper function to wait for Angular
def wait_for_angular(driver, timeout=15):
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return window.getAllAngularTestabilities().every(t => t.isStable());")
        )
    except Exception:
        pass
def go_to_product(driver, product_id, log, test_case_id, title, expected):
    try:
        driver.get(f"http://localhost:4200/#/product/{product_id}")
        wait_for_angular(driver)
        return True
    except Exception as e:
        log(f"{test_case_id} FAILED | {title} | Expected: {expected} | Actual: Failed to open product page | Error: {str(e)}")
        driver.quit()
        return False
    pass
def add_to_cart(driver, log, test_case_id, title, expected):
    try:
        driver.find_element(By.ID, "btn-add-to-cart").click()
        wait_for_angular(driver)
        return True
    except Exception as e:
        log(f"{test_case_id} FAILED | {title} | Expected: {expected} | Actual: Failed to add to cart | Error: {str(e)}")
        driver.quit()
        return False

def go_to_cart(driver, log, test_case_id, title, expected):
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="nav-cart"]')))
        driver.find_element(By.CSS_SELECTOR, '[data-test="nav-cart"]').click()
        wait_for_angular(driver)
        return True
    except Exception as e:
        log(f"{test_case_id} FAILED | {title} | Expected: {expected} | Actual: Failed to go to cart | Error: {str(e)}")
        driver.quit()
        return False

def update_quantity_and_checkout(driver, quantity, log, test_case_id, title, expected):
    try:
        retry = 0
        while retry < 3:
            try:
                qty_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="number"]')))
                qty_input.clear()
                qty_input.send_keys(quantity)
                checkout_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='proceed-1']")))
                checkout_btn.click()
                wait_for_angular(driver)
                return True
            except StaleElementReferenceException:
                retry += 1
                time.sleep(1)
        raise Exception("StaleElementReferenceException after 3 retries")
    except Exception as e:
        log(f"{test_case_id} FAILED | {title} | Expected: {expected} | Actual: Failed to go to checkout | Error: {str(e)}")
        driver.quit()
        return False

def login(driver, log, test_case_id, title, expected):
    try:
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'email')))
        driver.find_element(By.ID, 'email').send_keys(EMAIL)
        driver.find_element(By.ID, 'password').send_keys(PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "[data-test='login-submit']").click()
        wait_for_angular(driver)
        driver.find_element(By.CSS_SELECTOR, "[data-test='proceed-2']").click()
        return True
    except Exception as e:
        log(f"{test_case_id} FAILED | {title} | Expected: {expected} | Actual: Failed to login | Error: {str(e)}")
        driver.quit()
        return False

def fill_billing_address(driver, street, city, state, country, postcode, log, test_case_id, title, expected):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "address")))
        driver.find_element(By.ID, "address").send_keys(street)
        driver.find_element(By.ID, "city").send_keys(city)
        driver.find_element(By.ID, "state").send_keys(state)
        driver.find_element(By.ID, "country").send_keys(country)
        driver.find_element(By.ID, "postcode").send_keys(postcode)
        driver.find_element(By.CSS_SELECTOR, "[data-test='proceed-3']").click()
        return True
    except Exception as e:
        log(f"{test_case_id} FAILED | {title} | Expected: {expected} | Actual: Failed to fill Billing Address | Error: {str(e)}")
        driver.quit()
        return False

def select_payment(driver, payment_method, bank_name, account_name, account_number, expected, log, test_case_id, title):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "payment-method")))
        payment_dropdown = Select(driver.find_element(By.ID, "payment-method"))
        matched = False
        for option in payment_dropdown.options:
            if option.text.strip().lower() == payment_method.strip().lower():
                payment_dropdown.select_by_visible_text(option.text)
                matched = True
                break
        if not matched:
            raise Exception(f"Payment method '{payment_method}' not found in dropdown")
        if payment_method.lower() == "bank transfer":
            driver.find_element(By.ID, "bank-name").send_keys(bank_name)
            driver.find_element(By.ID, "account-name").send_keys(account_name)
            driver.find_element(By.ID, "account-number").send_keys(account_number)
        if any(pm in expected.lower() for pm in ["credit card", "gift card", "buy now pay later"]):
            payment_fields = driver.find_elements(By.CSS_SELECTOR, ".payment-input")
            if not payment_fields:
                log(f"{test_case_id} FAILED | {title} | Expected: {expected} | Actual: Payment fields not displayed | Error: ")
                driver.quit()
                return False
        return True
    except Exception as e:
        log(f"{test_case_id} FAILED | {title} | Expected: {expected} | Actual: Failed to select Payment Method | Error: {str(e)}")
        driver.quit()
        return False

def confirm_checkout(driver, log, test_case_id, title, expected):
    try:
        confirm_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='finish']"))
        )
        confirm_btn.click()
        wait_for_angular(driver)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".confirmation-message, .alert"))
        )
        log(f"{test_case_id} PASSED | {title} | Expected: {expected} | Actual: Checkout confirmation displayed")
        return True
    except Exception as e:
        log(f"{test_case_id} FAILED | {title} | Expected: {expected} | Actual: Failed to confirm checkout | Error: {str(e)}")
        driver.quit()
        return False
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return window.getAllAngularTestabilities().every(t => t.isStable());")
        )
    except Exception:
        pass

# Run test on each browser
for browser_name, browser_func in browsers.items():
    print(f"\n🔍 Running tests on: {browser_name.upper()}")

    # Create log file for each browser
    log_path = f"logs/test_results_{browser_name}.txt"
    log_file = open(log_path, "w", encoding="utf-8")

    def log(msg):
        print(msg)  # In ra terminal
        log_file.write(msg + "\n")  # Ghi vào file

    for index, row in df.iterrows():
        # Directly use columns from CSV
        test_case_id = row["TestCaseID"]
        quantity = str(row["Quantity"]) if pd.notna(row["Quantity"]) else ""
        street = str(row["Street"]) if pd.notna(row["Street"]) else "Test Street 98"
        city = str(row["City"]) if pd.notna(row["City"]) else "Vienna"
        country = str(row["Country"]) if pd.notna(row["Country"]) else "Austria"
        state = str(row["State"]) if pd.notna(row["State"]) else "Vienna"
        postcode = str(row["Postcode"]) if pd.notna(row["Postcode"]) else "1010"
        payment_method = str(row["PaymentMethod"]) if pd.notna(row["PaymentMethod"]) else "Cash on Delivery"
        bank_name = str(row["BankName"]) if pd.notna(row["BankName"]) else ""
        account_name = str(row["AccountName"]) if pd.notna(row["AccountName"]) else ""
        account_number = str(row["AccountNumber"]) if pd.notna(row["AccountNumber"]) else ""
        expected = str(row["Expected"]).lower()
        title = str(row["Title"]).lower()

        driver = browser_func()
        product_id = 1  # Nếu cần lấy từ dữ liệu, thay đổi ở đây
        steps = [
            lambda: go_to_product(driver, product_id, log, test_case_id, title, expected),
            lambda: add_to_cart(driver, log, test_case_id, title, expected),
            lambda: go_to_cart(driver, log, test_case_id, title, expected),
            lambda: update_quantity_and_checkout(driver, quantity, log, test_case_id, title, expected),
            lambda: login(driver, log, test_case_id, title, expected),
            lambda: fill_billing_address(driver, street, city, state, country, postcode, log, test_case_id, title, expected),
            lambda: select_payment(driver, payment_method, bank_name, account_name, account_number, expected, log, test_case_id, title),
            lambda: confirm_checkout(driver, log, test_case_id, title, expected)
        ]
        for step in steps:
            if not step():
                break
        driver.quit()
        