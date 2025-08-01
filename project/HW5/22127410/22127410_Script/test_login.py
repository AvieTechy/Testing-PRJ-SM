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

# Load test data
try:
    df = pd.read_csv("login_test_data.csv", on_bad_lines='skip')
    print("CSV loaded successfully. Shape:", df.shape)
except Exception as e:
    print("Error loading CSV:", e)
    exit(1)

# Init browsers
browsers = {
    "safari": lambda: Safari(),
    "chrome": lambda: webdriver.Chrome(service=ChromeService()),
    "firefox": lambda: webdriver.Firefox(service=FirefoxService()),
   
}

# Ensure log folder exists
os.makedirs("logs", exist_ok=True)

for browser_name, browser_func in browsers.items():
    print(f"\n🔍 Running tests on: {browser_name.upper()}")
    log_file = open(f"logs/login_results_{browser_name}.txt", "w", encoding="utf-8")

    def log(msg):
        print(msg)
        log_file.write(msg + "\n")

    for idx, row in df.iterrows():
        test_id = row.get("Test case ID", f"TC_{idx+1}")
        title = row.get("Title", "")
        inputs = row.get("Inputs", "")
        expected = row.get("Expected Result", "").lower().strip()

        # Parse email and password
        email = ""
        password = ""
        for line in str(inputs).splitlines():
            if "email" in line.lower():
                email = line.split(":", 1)[-1].strip().strip('"').strip("'")
            elif "password" in line.lower():
                password = line.split(":", 1)[-1].strip().strip('"').strip("'")

        driver = browser_func()
        driver.get("http://localhost:4200/#/auth/login")

        try:
            # Fill email
            email_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "email")))
            email_field.clear()
            email_field.send_keys(email)
            log(f"[{test_id}] Email: {email}")

            # Fill password
            pwd_field = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "app-password-input input[id='password']"))
            )
            pwd_field.clear()
            pwd_field.send_keys(password)
            log(f"[{test_id}] Password entered")

            # Submit login
            submit_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='login-submit']"))
            )
            submit_btn.click()
            time.sleep(2)

            # Get current status
            current_url = driver.current_url.lower()
            page_text = driver.page_source.lower()

            if "admin" in current_url or "admin dashboard" in page_text:
                actual = "admin dashboard loaded"
            elif "account" in current_url or "user dashboard" in page_text:
                actual = "user dashboard loaded"
            elif "invalid" in page_text or "not found" in page_text or "required" in page_text:
                actual = "error message"
            else:
                actual = "unknown"

            if expected in actual:
                log(f"[{test_id}] ✅ PASS | Expected: {expected} | Actual: {actual}")
            else:
                log(f"[{test_id}] ❌ FAIL | Expected: {expected} | Actual: {actual}")
                driver.save_screenshot(f"logs/{test_id}_{browser_name}_fail.png")

        except Exception as e:
            log(f"[{test_id}] ⚠️ ERROR: {str(e)}")
            driver.save_screenshot(f"logs/{test_id}_{browser_name}_exception.png")

        driver.quit()

    log_file.close()