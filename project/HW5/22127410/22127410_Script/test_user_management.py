import pandas as pd
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.safari.webdriver import WebDriver as Safari
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# --- CONFIG ---
ADMIN_EMAIL = "admin@practicesoftwaretesting.com"
ADMIN_PASSWORD = "welcome01"
BASE_URL = "http://localhost:4200"
CSV_PATH = "user_manage_data.csv"
LOG_FOLDER = "logs"

# --- SETUP ---
os.makedirs(LOG_FOLDER, exist_ok=True)
df = pd.read_csv(CSV_PATH)

# --- BROWSER DRIVERS ---
browsers = {
    "chrome": lambda: webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
    "firefox": lambda: webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())),
    "safari": lambda: Safari()
}

def log_init(browser_name):
    log_path = os.path.join(LOG_FOLDER, f"uc02_results_{browser_name}.txt")
    return open(log_path, "w", encoding="utf-8")

def log(log_file, msg):
    print(msg)
    log_file.write(msg + "\n")

def login_admin(driver):
    driver.get(f"{BASE_URL}/#/auth/login")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email")))
    driver.find_element(By.ID, "email").send_keys(ADMIN_EMAIL)
    driver.find_element(By.CSS_SELECTOR, "app-password-input input[id='password']").send_keys(ADMIN_PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "input[data-test='login-submit']").click()
    WebDriverWait(driver, 10).until(lambda d: "/dashboard" in d.current_url or "/admin" in d.current_url)

def perform_action(driver, row):
    # ...existing code...
    action = str(row.get("Action", "")).strip().lower()
    driver.get(f"{BASE_URL}/#/admin/users")
    time.sleep(1)

    if action == "delete":
        try:
            user_row = driver.find_element(By.XPATH, f"//td[contains(text(), '{row['Email']}')]/..")
            user_row.find_element(By.XPATH, ".//button[contains(text(),'Delete') or @data-test='delete']").click()
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
            time.sleep(1)
            return "User deleted successfully"
        except Exception as e:
            return "Error: Could not delete user"

    elif action == "edit":
        try:
            user_row = driver.find_element(By.XPATH, f"//td[contains(text(), '{row['Email']}')]/..")
            user_row.find_element(By.XPATH, ".//button[contains(text(),'Edit') or @data-test='edit']").click()
        except:
            return "Error: User not found for editing"
    else:
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="user-add"]')))
                add_user_elem = driver.find_element(By.CSS_SELECTOR, '[data-test="user-add"]')
            except Exception:
                try:
                    add_user_elem = driver.find_element(By.XPATH, "//button[contains(text(), 'Add User')]")
                except Exception:
                    return "Error: 'Add User' button not found"
            try:
                add_user_elem.click()
            except Exception:
                driver.execute_script("arguments[0].click();", add_user_elem)
            # Chờ form hiện ra trước khi điền dữ liệu
            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "firstname")))
            except Exception:
                return "Error: Add User form did not appear"
    # Fill form
    try:
        if 'First Name' in row:
            print("Điền First Name...")
            el = driver.find_element(By.ID, "firstname")
            el.clear()
            el.send_keys(str(row['First Name']))
        if 'Last Name' in row:
            print("Điền Last Name...")
            el = driver.find_element(By.ID, "lastname")
            el.clear()
            el.send_keys(str(row['Last Name']))
        if 'DOB' in row and pd.notna(row['DOB']):
            print("Điền DOB...")
            el = driver.find_element(By.ID, "dob")
            el.clear()
            el.send_keys(str(row['DOB']))
        if 'Address' in row and pd.notna(row['Address']):
            print("Điền Address...")
            try:
                el = driver.find_element(By.ID, "address")
                el.clear()
                el.send_keys(str(row['Address']))
            except Exception as e:
                print(f"⚠️ Không điền được Address: {e}")
        if 'City' in row and pd.notna(row['City']):
            print("Điền City...")
            el = driver.find_element(By.ID, "city")
            el.clear()
            el.send_keys(str(row['City']))
        if 'State' in row and pd.notna(row['State']):
            print("Điền State...")
            el = driver.find_element(By.ID, "state")
            el.clear()
            el.send_keys(str(row['State']))
        if 'Country' in row:
            print("Chọn Country...")
            try:
                country_dropdown = Select(driver.find_element(By.ID, "country"))
                all_options = [opt.text for opt in country_dropdown.options]
                country_to_select = str(row["Country"])
                if country_to_select in all_options:
                    country_dropdown.select_by_visible_text(country_to_select)
                else:
                    print(f"⚠️ Không tìm thấy '{country_to_select}' trong dropdown. Chọn giá trị đầu tiên: {all_options[0]}")
                    country_dropdown.select_by_visible_text(all_options[0])
            except Exception as e:
                print(f"⚠️ Không chọn được Country: {e}")
                return "Error: Failed to select Country"
        if 'Phone' in row and pd.notna(row['Phone']):
            print("Điền Phone...")
            el = driver.find_element(By.ID, "phone")
            el.clear()
            el.send_keys(str(row['Phone']))
        if 'Email' in row and action != "edit":
            print("Điền Email...")
            el = driver.find_element(By.ID, "email")
            el.clear()
            el.send_keys(str(row['Email']))
        if 'Password' in row:
            print("Điền Password...")
            el = driver.find_element(By.ID, "password")
            el.clear()
            el.send_keys(str(row['Password']))
        
        print("Click Save...")
        try:
            # Chờ overlay/toast/spinner biến mất nếu có
            for selector in ["[class*='overlay']", "[class*='toast']", "[class*='spinner']"]:
                try:
                    WebDriverWait(driver, 3).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                except:
                    pass
            submit_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='user-submit']"))
            )
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
            time.sleep(0.5)
            submit_btn.click()
        except Exception as e:
            print(f"⚠️ Click trực tiếp không được, thử click bằng JS: {e}")
            try:
                btn = driver.find_element(By.CSS_SELECTOR, "[data-test='user-submit']")
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                time.sleep(0.5)
                driver.execute_script("arguments[0].click();", btn)
            except Exception as e2:
                print(f"⚠️ Click bằng JS cũng lỗi: {e2}")
                return "Error: Failed to click Save button"
        time.sleep(1)
    except Exception as e:
        print(f"Lỗi khi điền dữ liệu: {e}")
        return "Error: Failed to fill or submit form"

    # Check result
    try:
        success_msg = driver.find_element(By.CLASS_NAME, "alert-success").text.strip()
        return success_msg
    except:
        try:
            error_msg = driver.find_element(By.CLASS_NAME, "alert-danger").text.strip()
            return error_msg if error_msg else "Error: Message blank"
        except:
            return "unknown"

# --- MAIN ---
for browser_name, browser_func in browsers.items():
    print(f"\n🔍 Running tests on: {browser_name.upper()}")
    driver = browser_func()
    log_file = log_init(browser_name)
    try:
        login_admin(driver)
        for _, row in df.iterrows():
            expected = str(row["Expected Result"]).lower().strip()
            actual = perform_action(driver, row).lower().strip()
            tc_id = row["Test case ID"]
            status = "✅ PASS" if expected in actual else "❌ FAIL"
            log(log_file, f"{status} | {tc_id} | Expected: {expected} | Actual: {actual}")
    finally:
        log_file.close()
        driver.quit()