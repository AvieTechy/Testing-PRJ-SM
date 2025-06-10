# Test Execution & Bug Report

## Test Execution

### Process

- Designed test cases for "Sign Up" (UC01) and "Checkout" (UC02) features using Equivalence Partitioning (EP) and Boundary Value Analysis (BVA), as documented in the test case file.
- Executed 41 test cases for Sign Up and 30 test cases for Checkout manually by tester Cao Uyen Nhi on 04/06/2025.
- Recorded test results, comparing actual outcomes against expected results, and logged defects for discrepancies.

### Results

1. **Sign Up**

- Valid inputs (e.g., all fields filled correctly, 10+ character password with required characters, 6-digit postal code) passed (e.g., TC_001, TC_011, TC_017).
- Invalid inputs (e.g., empty fields, invalid email format, emoji in name) correctly triggered error messages in some cases (e.g., TC_003–TC_008, TC_028–TC_030).
- Multiple test cases failed due to improper validation, such as allowing duplicate emails, weak passwords, invalid postal codes, and future DOBs (e.g., TC_009, TC_013–TC_016, TC_018–TC_021).

2. **Checkout**

- Valid inputs (e.g., cart with 1–10 items, complete billing address, valid payment details) processed successfully (e.g., TC_001, TC_002, TC_012).
- Some invalid inputs (e.g., empty address, city, or state) correctly prevented checkout (e.g., TC_013–TC_017).
- Several test cases failed due to issues like allowing empty carts, invalid quantities, and incorrect payment method fields (e.g., TC_003–TC_009, TC_027–TC_030).


## Bug Report

### Identified Bugs

1. **Sign Up (UC01)**

- **Duplicate Email (B001)**: System allows registration with an already registered email (e.g., customer@practicesoftwaretesting.com).
- **Password Validation (B002–B005)**: System fails to enforce password requirements (uppercase, lowercase, number, special symbol), allowing weak passwords (e.g., abc1234@, ABC1234@, Abcdefg@, Abc12345).
- **Postal Code Validation (B006–B008)**: System allows 5-digit, 7-digit, or non-numeric postal codes instead of requiring exactly 6 digits.
- **Future DOB (B009)**: System permits future dates of birth (e.g., 01/01/2050).
- **Incorrect Error Messages (B010–B011)**: Missing state or country triggers incorrect error messages (e.g., "Country required" for missing state).
- **Age Validation (B012–B013)**: System allows users under 16 (e.g., DOB 04/06/2009) or with very old DOBs (e.g., 01/01/1900).
- **Multiple Empty Fields (B014)**: System may proceed with multiple empty required fields.
- **Name Length Validation (B015–B016)**: System allows first/last names exceeding 50 characters.
- **Phone Number Validation (B017–B019)**: System rejects valid 10-digit phone numbers, allows 9-digit or 16-digit numbers.
- **City Validation (B020)**: System allows city names with numbers (e.g., 12345).


2. **Checkout (UC02)**

- **Quantity Validation (B021–B026)**: System allows checkout with quantities above 10, zero, negative, non-numeric, or empty, or resets quantity to 10 without error (e.g., quantity=100, 0, -1, "abc", "").
- **Cart Removal (B027)**: System does not allow removing items from the cart via the Remove button.
- **Bank Transfer Validation (B028–B031)**: System allows bank names with numbers, account numbers with letters, or account numbers shorter/longer than 8–34 digits.
- **Payment Method Fields (B032–B035)**: Selecting Credit Card, Cash on Delivery, Gift Card, or Buy Now Pay Later displays incorrect Bank Transfer input fields or fails to enable Confirm button.


### Resolutions

1. **Sign Up**

- Implement unique email validation to reject duplicate emails.
- Enforce password requirements (min 10 characters, uppercase, lowercase, number, special symbol).
- Restrict postal codes to exactly 6 numeric digits.
- Validate DOB to reject future dates and ensure users are at least 16 years old, with a reasonable historical range (e.g., post-1900).
- Fix error messages for missing state/country to display correct prompts.
- Ensure multiple empty fields trigger appropriate errors and prevent registration.
- Limit first/last names to 50 characters and reject invalid characters.
- Validate phone numbers to accept 10–15 digits and reject shorter/longer or non-numeric inputs.
- Restrict city field to letters and spaces only.

2. **Checkout**

- Enforce cart quantity validation (1–10) and disable checkout for invalid quantities (0, negative, non-numeric, empty).
- Fix Remove button functionality to clear items from the cart.
- Validate Bank Transfer fields: restrict Bank Name to letters/spaces, Account Number to 8–34 numeric digits.
- Ensure correct input fields are displayed for each payment method (Credit Card, Cash on Delivery, Gift Card, Buy Now Pay Later) and enable Confirm button appropriately.
