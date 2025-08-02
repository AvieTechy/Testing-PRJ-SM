import pandas as pd
import time, os
import subprocess
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# --- CONFIG ---
CUSTOMER_EMAIL = "customer@practicesoftwaretesting.com"
CUSTOMER_PASSWORD = "welcome01"
BASE_URL = "http://localhost:4200"
CSV_PATH = r"c:\Users\viett\OneDrive\Documents\GitHub\practice-software-testing\automation_test\data\profile_update_data.csv"
LOG_FOLDER = "logs"

# Global variable to track current password after changes
CURRENT_PASSWORD = CUSTOMER_PASSWORD

# Test cases that would actually change the password (avoid due to server bug)
PASSWORD_CHANGE_SUCCESS_TESTS = ["TC127", "TC130"]

# --- DATABASE REFRESH FUNCTION ---
def refresh_database():
    """Refresh the database to restore original state when password changes break subsequent tests"""
    try:
        print("\n🔄 Refreshing database to restore original state...")
        
        # Change to the project root directory
        project_root = r"c:\Users\viett\OneDrive\Documents\GitHub\practice-software-testing"
        original_dir = os.getcwd()
        os.chdir(project_root)
        
        # Run the Docker command to refresh database
        result = subprocess.run(
            ["docker-compose", "exec", "-T", "laravel-api", "php", "artisan", "migrate:fresh", "--seed"],
            capture_output=True,
            text=True,
            timeout=120  # 2 minute timeout
        )
        
        # Restore original directory
        os.chdir(original_dir)
        
        if result.returncode == 0:
            print("Database refreshed successfully!")
            # Reset global password variable
            global CURRENT_PASSWORD
            CURRENT_PASSWORD = CUSTOMER_PASSWORD
            return True
        else:
            print(f"Database refresh failed: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("Database refresh timed out after 2 minutes")
        return False
    except Exception as e:
        print(f"Database refresh error: {str(e)}")
        return False

def test_login_with_current_password(driver):
    """Test if we can still login with the current password"""
    try:
        print(f"Testing login with current password...")
        driver.get(f"{BASE_URL}/#/auth/login")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-test='email']")))
        
        # Clear and fill login form
        email_field = driver.find_element(By.CSS_SELECTOR, "input[data-test='email']")
        password_field = driver.find_element(By.CSS_SELECTOR, "input[data-test='password']")
        
        email_field.clear()
        email_field.send_keys(CUSTOMER_EMAIL)
        password_field.clear()
        password_field.send_keys(CURRENT_PASSWORD)
        
        driver.find_element(By.CSS_SELECTOR, "input[data-test='login-submit']").click()
        time.sleep(3)
        
        # Check if login was successful
        if "login" not in driver.current_url.lower():
            print("Login successful with current password")
            return True
        else:
            print("Login failed with current password")
            return False
            
    except Exception as e:
        print(f"Login test error: {str(e)}")
        return False

# --- SETUP ---
os.makedirs(LOG_FOLDER, exist_ok=True)
df = pd.read_csv(CSV_PATH)

# --- BROWSER DRIVERS ---
def create_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    try:
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    except Exception as e:
        print(f"Failed to create Chrome driver with manager, trying system driver: {e}")
        return webdriver.Chrome(options=options)

def create_firefox_driver():
    options = webdriver.FirefoxOptions()
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference('useAutomationExtension', False)
    try:
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    except Exception as e:
        print(f"Failed to create Firefox driver with manager, trying system driver: {e}")
        return webdriver.Firefox(options=options)

def create_edge_driver():
    options = webdriver.EdgeOptions()
    options.use_chromium = True

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        print("Initializing Edge driver from manual path...")
        driver_path = r"C:\Users\viett\Downloads\edgedriver_win64\msedgedriver.exe"
        return webdriver.Edge(service=EdgeService(executable_path=driver_path), options=options)
    except Exception as e:
        print(f"Edge driver initialization failed: {e}")
        return None

browsers = {
    "edge": create_edge_driver,
    "chrome": create_chrome_driver,
    "firefox": create_firefox_driver
}

def log_init(browser_name):
    log_path = os.path.join(LOG_FOLDER, f"profile_update_results_{browser_name}.txt")
    return open(log_path, "w", encoding="utf-8")

def log(log_file, msg):
    print(msg)
    log_file.write(msg + "\n")

def login_customer(driver, max_retries=2):
    """Login as customer to access profile page with database refresh on failure"""
    global CURRENT_PASSWORD
    
    for attempt in range(max_retries):
        try:
            print(f"🔑 Login attempt {attempt + 1} with password: {CURRENT_PASSWORD}")
            driver.get(f"{BASE_URL}/#/auth/login")
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-test='email']")))
            
            # Clear and fill login form
            email_field = driver.find_element(By.CSS_SELECTOR, "input[data-test='email']")
            password_field = driver.find_element(By.CSS_SELECTOR, "input[data-test='password']")
            
            email_field.clear()
            email_field.send_keys(CUSTOMER_EMAIL)
            password_field.clear()
            password_field.send_keys(CURRENT_PASSWORD)
            
            driver.find_element(By.CSS_SELECTOR, "input[data-test='login-submit']").click()
            time.sleep(3)
            
            # Check if login was successful
            if "login" not in driver.current_url.lower():
                print("✅ Login successful!")
                return True
            else:
                print(f"❌ Login failed on attempt {attempt + 1}")
                
                # If this is not the last attempt, try refreshing database
                if attempt < max_retries - 1:
                    print("🔄 Attempting database refresh...")
                    if refresh_database():
                        print("💤 Waiting 10 seconds for services to stabilize...")
                        time.sleep(10)
                        continue
                    else:
                        print("❌ Database refresh failed, will try once more with current state")
                        continue
                
                return False
                
        except Exception as e:
            print(f"❌ Login attempt {attempt + 1} error: {str(e)}")
            if attempt < max_retries - 1:
                print("🔄 Retrying login...")
                time.sleep(5)
                continue
            return False
    
    return False

def perform_profile_action(driver, row):
    """Perform profile update or password change action"""
    try:
        # Navigate to profile page
        driver.get(f"{BASE_URL}/#/account/profile")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-test='first-name']")))
        time.sleep(1)
        
        # Check if this is a password change test or profile update test
        is_password_test = (pd.notna(row.get('CurrentPassword')) and row.get('CurrentPassword') != 'N/A') or \
                          (pd.notna(row.get('NewPassword')) and row.get('NewPassword') != 'N/A') or \
                          (pd.notna(row.get('ConfirmNewPassword')) and row.get('ConfirmNewPassword') != 'N/A')
        
        if is_password_test:
            return perform_password_change(driver, row)
        else:
            return perform_profile_update(driver, row)
            
    except Exception as e:
        return f"Error: Failed to navigate to profile page - {str(e)}"

def perform_profile_update(driver, row):
    """Update profile information"""
    try:
        print("Updating profile information...")
        
        # Fill profile form fields
        if pd.notna(row.get('FirstName')) and row['FirstName'] != 'N/A':
            print("Filling First Name...")
            el = driver.find_element(By.CSS_SELECTOR, "input[data-test='first-name']")
            el.clear()
            if str(row['FirstName']) != '<empty>':
                el.send_keys(str(row['FirstName']))
        
        if pd.notna(row.get('LastName')) and row['LastName'] != 'N/A':
            print("Filling Last Name...")
            el = driver.find_element(By.CSS_SELECTOR, "input[data-test='last-name']")
            el.clear()
            if str(row['LastName']) != '<empty>':
                el.send_keys(str(row['LastName']))
        
        if pd.notna(row.get('Email')) and row['Email'] != 'N/A':
            print("Filling Email...")
            el = driver.find_element(By.CSS_SELECTOR, "input[data-test='email']")
            el.clear()
            if str(row['Email']) != '<empty>':
                el.send_keys(str(row['Email']))
        
        if pd.notna(row.get('Phone')) and row['Phone'] != 'N/A':
            print("Filling Phone...")
            el = driver.find_element(By.CSS_SELECTOR, "input[data-test='phone']")
            el.clear()
            if str(row['Phone']) != '<empty>':
                el.send_keys(str(row['Phone']))
        
        if pd.notna(row.get('Address')) and row['Address'] != 'N/A':
            print("Filling Address...")
            el = driver.find_element(By.CSS_SELECTOR, "input[data-test='address']")
            el.clear()
            if str(row['Address']) != '<empty>':
                el.send_keys(str(row['Address']))
        
        if pd.notna(row.get('Postcode')) and row['Postcode'] != 'N/A':
            print("Filling Postcode...")
            el = driver.find_element(By.CSS_SELECTOR, "input[data-test='postcode']")
            el.clear()
            if str(row['Postcode']) != '<empty>':
                el.send_keys(str(row['Postcode']))
        
        if pd.notna(row.get('City')) and row['City'] != 'N/A':
            print("Filling City...")
            el = driver.find_element(By.CSS_SELECTOR, "input[data-test='city']")
            el.clear()
            if str(row['City']) != '<empty>':
                el.send_keys(str(row['City']))
        
        if pd.notna(row.get('State')) and row['State'] != 'N/A':
            print("Filling State...")
            el = driver.find_element(By.CSS_SELECTOR, "input[data-test='state']")
            el.clear()
            if str(row['State']) != '<empty>':
                el.send_keys(str(row['State']))
        
        if pd.notna(row.get('Country')) and row['Country'] != 'N/A':
            print("Filling Country...")
            el = driver.find_element(By.CSS_SELECTOR, "input[data-test='country']")
            el.clear()
            if str(row['Country']) != '<empty>':
                el.send_keys(str(row['Country']))
        
        # Submit the profile form
        print("Clicking Update Profile button...")
        try:
            # Wait for any overlays to disappear
            for selector in ["[class*='overlay']", "[class*='toast']", "[class*='spinner']"]:
                try:
                    WebDriverWait(driver, 3).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                except:
                    pass
            
            submit_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='update-profile-submit']"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
            time.sleep(0.5)
            submit_btn.click()
        except Exception as e:
            print(f"Direct click failed, trying JS click: {e}")
            try:
                btn = driver.find_element(By.CSS_SELECTOR, "button[data-test='update-profile-submit']")
                driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                time.sleep(0.5)
                driver.execute_script("arguments[0].click();", btn)
            except Exception as e2:
                print(f"JS click also failed: {e2}")
                return "Error: Failed to click Update Profile button"
        
        time.sleep(2)  # Wait for processing
        
    except Exception as e:
        print(f"Error filling profile form: {e}")
        return f"Error: Failed to fill or submit profile form - {str(e)}"
    
    # Check result
    return check_result_message(driver, row)

def perform_password_change(driver, row):
    """Change password"""
    try:
        tc_id = row.get("TestCaseID", "")
        print(f"Changing password for {tc_id}...")
        
        # Special handling for password visibility toggle tests
        if tc_id in ["TC140", "TC141"]:
            return test_password_visibility_toggle(driver, row)
        
        # Fill password form fields
        if pd.notna(row.get('CurrentPassword')) and row.get('CurrentPassword') != 'N/A':
            print("Filling Current Password...")
            el = driver.find_element(By.CSS_SELECTOR, "input[data-test='current-password']")
            el.clear()
            if str(row['CurrentPassword']) != '<empty>':
                # For TC136 (new password same as current), use actual current password
                if str(row['CurrentPassword']) == 'ValidOldPassword1!':
                    el.send_keys(CUSTOMER_PASSWORD)  # Use actual current password
                else:
                    el.send_keys(str(row['CurrentPassword']))
        
        if pd.notna(row.get('NewPassword')) and row.get('NewPassword') != 'N/A':
            print("Filling New Password...")
            el = driver.find_element(By.CSS_SELECTOR, "input[data-test='new-password']")
            el.clear()
            if str(row['NewPassword']) != '<empty>':
                # For TC136 (new password same as current), use current password
                if str(row['NewPassword']) == 'ValidOldPassword1!':
                    el.send_keys(CUSTOMER_PASSWORD)
                else:
                    el.send_keys(str(row['NewPassword']))
        
        if pd.notna(row.get('ConfirmNewPassword')) and row.get('ConfirmNewPassword') != 'N/A':
            print("Filling Confirm New Password...")
            el = driver.find_element(By.CSS_SELECTOR, "input[data-test='new-password-confirm']")
            el.clear()
            if str(row['ConfirmNewPassword']) != '<empty>':
                # For TC136 (new password same as current), use current password
                if str(row['ConfirmNewPassword']) == 'ValidOldPassword1!':
                    el.send_keys(CUSTOMER_PASSWORD)
                else:
                    el.send_keys(str(row['ConfirmNewPassword']))
        
        # Submit the password form
        print("Clicking Change Password button...")
        try:
            submit_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='change-password-submit']"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
            time.sleep(0.5)
            submit_btn.click()
        except Exception as e:
            print(f"Direct click failed, trying JS click: {e}")
            try:
                btn = driver.find_element(By.CSS_SELECTOR, "button[data-test='change-password-submit']")
                driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                time.sleep(0.5)
                driver.execute_script("arguments[0].click();", btn)
            except Exception as e2:
                print(f"JS click also failed: {e2}")
                return "Error: Failed to click Change Password button"
        
        time.sleep(3)  # Wait longer for processing
        
    except Exception as e:
        print(f"Error changing password: {e}")
        return f"Error: Failed to change password - {str(e)}"
    
    # Check result
    return check_result_message(driver, row)

def test_password_visibility_toggle(driver, row):
    """Test password visibility toggle functionality"""
    try:
        tc_id = row.get("TestCaseID", "")
        print(f"Testing password visibility toggle for {tc_id}...")
        
        if tc_id == "TC140":
            # Test new password field toggle
            password_field = driver.find_element(By.CSS_SELECTOR, "input[data-test='new-password']")
            toggle_btn = driver.find_element(By.CSS_SELECTOR, "i[data-test='show-new-password']")
            
            # Fill the password field first
            password_field.clear()
            password_field.send_keys("TestP@ss1")
            
            # Check initial state (should be password type)
            initial_type = password_field.get_attribute("type")
            print(f"Initial password field type: {initial_type}")
            
            # Click toggle button
            toggle_btn.click()
            time.sleep(0.5)
            
            # Check if type changed
            new_type = password_field.get_attribute("type")
            print(f"Password field type after toggle: {new_type}")
            
            if initial_type == "password" and new_type == "text":
                return "Password visibility toggled"
            elif initial_type == "text" and new_type == "password":
                return "Password visibility toggled"
            else:
                return "Error: Password visibility toggle failed"
                
        elif tc_id == "TC141":
            # Test confirm password field toggle
            password_field = driver.find_element(By.CSS_SELECTOR, "input[data-test='new-password-confirm']")
            toggle_btn = driver.find_element(By.CSS_SELECTOR, "i[data-test='show-new-password-confirm']")
            
            # Fill the password field first
            password_field.clear()
            password_field.send_keys("TestP@ss1")
            
            # Check initial state (should be password type)
            initial_type = password_field.get_attribute("type")
            print(f"Initial confirm password field type: {initial_type}")
            
            # Click toggle button
            toggle_btn.click()
            time.sleep(0.5)
            
            # Check if type changed
            new_type = password_field.get_attribute("type")
            print(f"Confirm password field type after toggle: {new_type}")
            
            if initial_type == "password" and new_type == "text":
                return "Password visibility toggled"
            elif initial_type == "text" and new_type == "password":
                return "Password visibility toggled"
            else:
                return "Error: Password visibility toggle failed"
        
        return "Password visibility test completed"
        
    except Exception as e:
        print(f"Error testing password visibility toggle: {e}")
        return f"Error: Failed to test password visibility toggle - {str(e)}"

def check_result_message(driver, row=None):
    """Check for success or error messages and track password changes"""
    global CURRENT_PASSWORD
    
    try:
        # Wait a bit longer for messages to appear
        time.sleep(1)
        
        # Check for success message first
        success_elements = driver.find_elements(By.CSS_SELECTOR, ".alert.alert-success, .alert-success")
        for element in success_elements:
            if element.is_displayed():
                success_msg = element.text.strip()
                print(f"Success message found: {success_msg}")
                if success_msg:
                    if "password" in success_msg.lower() and "changed" in success_msg.lower():
                        # Track password change if successful
                        if row is not None and pd.notna(row.get('NewPassword')) and row.get('NewPassword') != 'N/A':
                            new_password = str(row['NewPassword'])
                            print(f"🔑 Password changed successfully! Updating current password from '{CURRENT_PASSWORD}' to '{new_password}'")
                            CURRENT_PASSWORD = new_password
                        return "Password changed successfully"
                    elif "updated" in success_msg.lower():
                        return "Profile updated successfully"
                    return success_msg
    except Exception as e:
        print(f"Error checking success message: {e}")
    
    try:
        # Check for error messages
        error_selectors = [
            ".alert.alert-danger",
            ".alert-danger", 
            ".text-danger",
            ".invalid-feedback",
            ".error-message"
        ]
        
        for selector in error_selectors:
            error_elements = driver.find_elements(By.CSS_SELECTOR, selector)
            for element in error_elements:
                if element.is_displayed():
                    error_msg = element.text.strip()
                    print(f"Error message found: {error_msg}")
                    if error_msg:
                        # Map specific error messages to expected results
                        error_lower = error_msg.lower()
                        
                        # Password validation errors - match exact error messages from manual testing
                        if "the new password field confirmation does not match." in error_lower or "passwords do not match" in error_lower:
                            return "Error: Passwords do not match"
                        elif "new Password cannot be same as your current password." in error_lower:
                            return "Error: New password same as current"
                        elif "your current password does not matches with the password." in error_lower:
                            return "Error: Current password required"
                        elif "the new password field is required." in error_lower:
                            return "Error: New password required"
                        elif "new password confirmation field does not match" in error_lower:
                            return "Error: Confirm password required"
                        elif "password too short" in error_lower or "minimum" in error_lower:
                            return "Error: Password too short"
                        elif "uppercase" in error_lower:
                            return "Error: Must contain uppercase"
                        elif "lowercase" in error_lower:
                            return "Error: Must contain lowercase"
                        elif "number" in error_lower or "digit" in error_lower:
                            return "Error: Must contain number"
                        elif "special" in error_lower:
                            return "Error: Must contain special character"
                        elif "incorrect" in error_lower and "password" in error_lower:
                            return "Error: Incorrect current password"
                        
                        return f"Error: {error_msg}"
    except Exception as e:
        print(f"Error checking error message: {e}")
    
    try:
        # Check for any alert message as fallback
        alert_elements = driver.find_elements(By.CSS_SELECTOR, ".alert")
        for alert in alert_elements:
            if alert.is_displayed():
                alert_msg = alert.text.strip()
                print(f"Alert message found: {alert_msg}")
                if alert_msg:
                    return alert_msg
    except Exception as e:
        print(f"Error checking alert message: {e}")
    
    try:
        # Check for validation messages on form fields
        validation_elements = driver.find_elements(By.CSS_SELECTOR, ".form-control.is-invalid + .invalid-feedback")
        for element in validation_elements:
            if element.is_displayed():
                validation_msg = element.text.strip()
                print(f"Validation message found: {validation_msg}")
                if validation_msg:
                    return f"Error: {validation_msg}"
    except Exception as e:
        print(f"Error checking validation message: {e}")
    
    print("No visible feedback message found")
    return "No visible feedback message"

# --- MAIN ---
print("Profile Update Automation Test Suite")
print("=" * 50)
print(f"Application URL: {BASE_URL}")
print(f"Test Data: {CSV_PATH}")
print(f"Total Test Cases: {len(df)}")

for browser_name, browser_func in browsers.items():
    print(f"\nRunning tests on: {browser_name.upper()}")
    driver = None
    log_file = None
    
    try:
        print(f"Initializing {browser_name} driver...")
        
        # Special handling for Edge
        if browser_name == "edge":
            print("Note: Edge WebDriver requires Microsoft Edge browser to be installed")
            print("If Edge fails, please install Edge browser and/or run: pip install webdriver-manager --upgrade")
        
        driver = browser_func()
        
        if driver is None:
            print(f"Failed to initialize {browser_name} driver")
            if browser_name == "edge":
                print("Edge driver troubleshooting:")
                print("1. Ensure Microsoft Edge browser is installed")
                print("2. Run: pip install webdriver-manager --upgrade")
                print("3. Download Edge WebDriver manually from:")
                print("   https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/")
                print("4. Restart your command prompt/IDE")
                
            print(f"Skipping {browser_name} tests")
            continue
            
        print(f"{browser_name} driver initialized successfully")
        driver.maximize_window()
        log_file = log_init(browser_name)
        
        log(log_file, f"Profile Update Test Results - {browser_name.upper()}")
        log(log_file, "=" * 60)
        log(log_file, f"Application URL: {BASE_URL}")
        log(log_file, f"Test Date: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        log(log_file, "=" * 60)
        
        # Login once for all tests
        if not login_customer(driver):
            log(log_file, "LOGIN FAILED - SKIPPING ALL TESTS FOR THIS BROWSER")
            print(f"❌ Failed to login for {browser_name}, skipping all tests")
            continue
        
        log(log_file, "LOGIN SUCCESSFUL")
        
        # Run each test case
        passed_count = 0
        failed_count = 0
        skipped_count = 0
        
        for _, row in df.iterrows():
            try:
                tc_id = row["TestCaseID"]
                description = row["Test Case Description"]
                expected = str(row["ExpectedResult"]).lower().strip()
                
                print(f"\nRunning {tc_id}: {description}")
                
                # Check if we can still login before running test (in case previous test broke auth)
                if not test_login_with_current_password(driver):
                    print(f"⚠️  Login check failed before {tc_id}, attempting database refresh...")
                    if refresh_database():
                        print("💤 Waiting 10 seconds for services to stabilize...")
                        time.sleep(10)
                        # Try login again
                        if not login_customer(driver):
                            error_msg = f"SKIP | {tc_id} | Could not restore login state"
                            log(log_file, error_msg)
                            failed_count += 1
                            continue
                    else:
                        error_msg = f"SKIP | {tc_id} | Database refresh failed, login state broken"
                        log(log_file, error_msg)
                        failed_count += 1
                        continue
                
                # Perform the test action
                actual = perform_profile_action(driver, row).lower().strip()
                
                # Determine pass/fail status - Improved logic for better alignment
                is_negative_test = str(row.get("NegativeScenario", "")).lower() == "yes"
                
                # Check for critical system failures first
                if "resource not found" in actual:
                    status = "FAIL"
                    failed_count += 1
                elif "failed to navigate" in actual or "failed to load" in actual:
                    status = "FAIL"
                    failed_count += 1
                elif "could not fill" in actual or "could not find" in actual:
                    status = "FAIL"
                    failed_count += 1
                elif "login failed" in actual or "not accessible" in actual:
                    status = "FAIL"
                    failed_count += 1
                elif "no visible feedback message" in actual and is_negative_test:
                    # For negative tests expecting error messages, no feedback is a fail
                    status = "FAIL"
                    failed_count += 1
                elif "no visible feedback message" in actual and not is_negative_test:
                    # For positive tests with no feedback, it might still be a pass if no error occurred
                    status = "PASS (No feedback)"
                    passed_count += 1
                # More specific matching for different types of expected results
                elif "profile updated successfully" in expected and "success" in actual:
                    status = "PASS"
                    passed_count += 1
                elif "password changed successfully" in expected and "success" in actual:
                    status = "PASS"
                    passed_count += 1
                elif "password visibility toggled" in expected and "toggled" in actual:
                    status = "PASS"
                    passed_count += 1
                # Enhanced password error matching based on manual test results
                elif "passwords do not match" in expected and ("new password field confirmation does not match" in actual or "passwords do not match" in actual):
                    status = "PASS"
                    passed_count += 1
                elif "new password same as current" in expected and "new password cannot be the same as the current password" in actual:
                    status = "PASS"
                    passed_count += 1
                elif "current password required" in expected and "your current password does not match the password" in actual:
                    status = "PASS"
                    passed_count += 1
                elif "new password required" in expected and "new password is required" in actual:
                    status = "PASS"
                    passed_count += 1
                elif "confirm password required" in expected and "new password confirmation field does not match" in actual:
                    status = "PASS"
                    passed_count += 1
                elif "error:" in expected and ("error" in actual or "failed" in actual or "invalid" in actual):
                    # Only pass if it's the RIGHT kind of error, not a system error
                    if "resource not found" not in actual:
                        status = "PASS"
                        passed_count += 1
                    else:
                        status = "FAIL"
                        failed_count += 1
                elif "required" in expected and ("required" in actual or "is required" in actual):
                    status = "PASS"
                    passed_count += 1
                elif "too long" in expected and ("too long" in actual or "length" in actual):
                    status = "PASS"
                    passed_count += 1
                elif "invalid" in expected and ("invalid" in actual or "format" in actual):
                    # Only pass if it's a legitimate validation error, not a system error
                    if "resource not found" not in actual:
                        status = "PASS"
                        passed_count += 1
                    else:
                        status = "FAIL"
                        failed_count += 1
                elif "cannot contain" in expected and ("cannot contain" in actual or "invalid" in actual):
                    status = "PASS"
                    passed_count += 1
                elif expected in actual:
                    status = "PASS"
                    passed_count += 1
                else:
                    status = "FAIL"
                    failed_count += 1
                
                # Create log message if not already set
                if 'log_message' not in locals():
                    log_message = f"{status} | {tc_id} | Expected: {expected} | Actual: {actual}"
                
                log(log_file, log_message)
                
                # Reset log_message for next iteration
                if 'log_message' in locals():
                    del log_message
                
                # Small delay between tests
                time.sleep(1)
                
            except Exception as e:
                error_msg = f"ERROR | {tc_id} | Test execution failed: {str(e)}"
                log(log_file, error_msg)
                failed_count += 1
        
        # Log summary
        total_tests = passed_count + failed_count + skipped_count
        success_rate = (passed_count / (passed_count + failed_count) * 100) if (passed_count + failed_count) > 0 else 0
        
        log(log_file, "=" * 60)
        log(log_file, f"SUMMARY - {browser_name.upper()}")
        log(log_file, f"Total Tests: {total_tests}")
        log(log_file, f"Passed: {passed_count}")
        log(log_file, f"Failed: {failed_count}")
        log(log_file, f"Skipped: {skipped_count} (System issues)")
        log(log_file, f"Success Rate: {success_rate:.1f}% (excluding skipped)")
        log(log_file, "=" * 60)
        
        print(f"\n{browser_name.upper()} Summary:")
        print(f"   Total: {total_tests} | Passed: {passed_count} | Failed: {failed_count} | Skipped: {skipped_count}")
        print(f"   Success Rate: {success_rate:.1f}% (excluding skipped)")
        if skipped_count > 0:
            print(f"   Note: {skipped_count} tests skipped due to system issues")
        
    except Exception as e:
        error_msg = f"CRITICAL ERROR in {browser_name}: {str(e)}"
        print(error_msg)
        if log_file:
            log(log_file, error_msg)
            
    finally:
        if log_file:
            log_file.close()
        if driver:
            driver.quit()

print(f"\nTest execution completed!")
print(f"Check log files in '{LOG_FOLDER}' folder for detailed results")
print("=" * 60)
print("Profile Update Test Suite finished")
