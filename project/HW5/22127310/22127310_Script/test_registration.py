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

# Load test data with error handling
try:
    df = pd.read_csv("registration_test_data.csv", on_bad_lines='skip')
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

# Run test on each browser
for browser_name, browser_func in browsers.items():
    print(f"\n🔍 Running tests on: {browser_name.upper()}")

    # Create log file for each browser
    log_path = f"logs/test_results_{browser_name}.txt"
    log_file = open(log_path, "w", encoding="utf-8")

    def log(msg):
        log_file.write(msg + "\n")

    for index, row in df.iterrows():
        # Directly use columns from CSV
        first_name = str(row["First Name"]) if pd.notna(row["First Name"]) else ""
        last_name = str(row["Last Name"]) if pd.notna(row["Last Name"]) else ""
        dob = str(row["DOB"]) if pd.notna(row["DOB"]) else ""
        # Normalize DOB to YYYY-MM-DD format
        if dob:
            try:
                dob = datetime.strptime(dob, "%m/%d/%Y").strftime("%Y-%m-%d")
            except ValueError:
                dob = ""
        address = str(row["Address"]) if pd.notna(row["Address"]) else ""
        postal_code = str(row["Postal Code"]) if pd.notna(row["Postal Code"]) else ""
        city = str(row["City"]) if pd.notna(row["City"]) else ""
        state = str(row["State"]) if pd.notna(row["State"]) else ""
        country = str(row["Country"]) if pd.notna(row["Country"]) else ""
        phone = str(row["Phone"]) if pd.notna(row["Phone"]) else ""
        email = str(row["Email"]) if pd.notna(row["Email"]) else ""
        password = str(row["Password"]) if pd.notna(row["Password"]) else ""
        expected = str(row["Expected"]).lower()

        driver = browser_func()
        try:
            driver.get("http://localhost:4200/#/auth/register")
            wait_for_angular(driver)

            # Helper function to fill text fields
            def fill_field(field_id, value):
                for attempt in range(3):
                    try:
                        element = WebDriverWait(driver, 15).until(
                            EC.visibility_of_element_located((By.ID, field_id))
                        )
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
                        driver.execute_script("arguments[0].style.zIndex = '9999';", element)
                        time.sleep(0.5)
                        if not element.is_displayed() or not element.is_enabled():
                            raise Exception(f"{field_id} not interactable")
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, field_id)))
                        element.clear()
                        element.send_keys(str(value))
                        if field_id == "dob":
                            entered_value = element.get_attribute("value")
                        return True
                    except Exception:
                        if attempt < 2:
                            wait_for_angular(driver)
                            time.sleep(1)
                            try:
                                label = driver.find_element(By.XPATH, f"//label[@for='{field_id}']")
                                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", label)
                                label.click()
                                time.sleep(0.5)
                            except:
                                pass
                        else:
                            return False
                return False

            # Helper function to handle dropdowns
            def select_dropdown(field_id, value):
                try:
                    dropdown = Select(WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.ID, field_id))
                    ))
                    value_to_select = str(value).strip()
                    if value_to_select in [opt.text for opt in dropdown.options]:
                        dropdown.select_by_visible_text(value_to_select)
                    else:
                        dropdown.select_by_visible_text(dropdown.options[0].text)
                    return True
                except Exception:
                    return False

            # Fill registration form
            fill_field("first_name", first_name)
            fill_field("last_name", last_name)
            fill_field("dob", dob)
            fill_field("address", address)
            fill_field("postcode", postal_code)
            fill_field("city", city)
            if state and not fill_field("state", state):
                log(f"TC_{index + 1} FAILED | {email} / {password} | Expected: {expected} | Actual: Failed to fill State | Error: State field issue")
                driver.quit()
                continue
            if country and not select_dropdown("country", country):
                log(f"TC_{index + 1} FAILED | {email} / {password} | Expected: {expected} | Actual: Failed to select Country | Error: Country dropdown issue")
                driver.quit()
                continue
            fill_field("phone", phone)
            if not fill_field("email", email):
                log(f"TC_{index + 1} FAILED | {email} / {password} | Expected: {expected} | Actual: Failed to fill Email | Error: Email field issue")
                driver.quit()
                continue
            try:
                password_field = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "app-password-input input[id='password']"))
                )
                password_field.clear()
                password_field.send_keys(password)
            except Exception:
                log(f"TC_{index + 1} FAILED | {email} / {password} | Expected: {expected} | Actual: Failed to fill Password | Error: Password field issue")
                driver.quit()
                continue

            # Submit form
            try:
                submit_btn = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
                )
                submit_btn.click()
            except Exception:
                log(f"TC_{index + 1} FAILED | {email} / {password} | Expected: {expected} | Actual: Failed to Submit | Error: Submit button issue")
                driver.quit()
                continue
            time.sleep(2)

            # Get page source for checking
            page_text = driver.page_source.lower()
            error_message = ""
            for by, sel in [(By.CLASS_NAME, "error-message"), (By.CSS_SELECTOR, ".alert-danger")]:
                try:
                    error_elem = driver.find_element(by, sel)
                    error_message = error_elem.text.strip().lower()
                    break
                except Exception:
                    continue

            # Registration success detection
            current_url = driver.current_url.lower()
            actual_result = "registration successful" if "register/success" in current_url or "account" in current_url else error_message or "unknown"

            # Check result
            expected_main = expected.split(":")[-1].strip() if ":" in expected else expected
            if expected_main in actual_result:
                log(f"TC_{index + 1} PASSED | {email} / {password} | Expected: {expected_main} | Actual: {actual_result} | Error: ")
            else:
                log(f"TC_{index + 1} FAILED | {email} / {password} | Expected: {expected_main} | Actual: {actual_result} | Error: {error_message}")

        except Exception:
            log(f"TC_{index + 1} FAILED | {email} / {password} | Expected: {expected} | Actual: Test Error | Error: General exception")

        driver.quit()

    log_file.close()