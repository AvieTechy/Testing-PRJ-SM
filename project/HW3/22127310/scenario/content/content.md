# Group Information

Group ID: 07

| Member Name        | Student ID | Assigned Features          | Status      |
|:-------------------------|:-----------|:---------------------------|:------|
| Cao Uyển Nhi       | 22127310   | - SignUp                   | Done |
|                    |            | - Checkout                 | Done |
| Lưu Thanh Thuý     | 22127410   | - SignIn                   | Done |
|                    |            | - User Management          | Done |
| Nguyễn Phước Minh Trí      | 22127424   | - Catalog                | Done |
|                    |            | - Categories                | Done |
| Võ Lê Việt Tú      | 22127435   | - MyProfile                | Done |
|                    |            | - Order Management                | Done |
| Trần Thị Cát Tường | 22127444   | - Contact                  | Done |
|                    |            | - Category Management      | Done |


# Scenario Definition

## Feature 1: Customer Registration

### Description

The **Customer Registration** feature enables new users to create an account by completing a registration form with required fields. The system ensures data integrity through client-side and server-side validation, checks for duplicate email addresses and phone numbers, and securely stores the account in the database upon successful validation. A success message is displayed to confirm account creation.

The registration form includes the following required fields:

- First Name: User's given name.
- Last Name: User's surname.
- Date of Birth: User's birth date to verify age eligibility.
- Address: User's street address.
- Postcode: Postal code for the address (format varies by country).
- City: City of residence.
- State: State or region (where applicable).
- Country: Country of residence.
- Phone Number: Contact number for communication.
- Email Address: Unique email for account identification.
- Password: Secure password for account access.

### Basic Flow

1. User Navigation: The user accesses the Customer Registration page via a web browser (e.g., through a "Sign Up" link on the homepage).
2. Form Completion: The user enters valid data in all required fields above.
3. Form Submission: The user clicks the “Register” button.
4. Validation:  
- Client-side: JavaScript checks for empty fields, invalid formats (e.g., email, phone, postcode), and password strength.
- Server-side: The backend re-validates all inputs to prevent bypassing client-side checks.
Duplicate Check: The system queries the database to ensure the email and phone number are unique.
5. Account Creation:  
- If all checks pass, the system hashes the password and stores the account in the database.
- The system returns a success message: “Account created successfully.”

### Alternate Flows
These alternate flows describe deviations from the basic flow due to invalid inputs, duplicates, or system errors.

**2.a. Required Field is Empty**

- Condition: Any required field (e.g., First Name, Email) is left blank.
- Action: Client-side validation highlights the empty field with an inline error (e.g., "This field is required") in red text below the input. The “Register” button may be disabled until all fields are filled.
- Outcome: Form submission is blocked until the user corrects the issue.

**2.b. First or Last Name Exceeds 120 Characters**

- Condition: First Name or Last Name input exceeds 120 characters (e.g., a very long string).
- Action: Client-side validation displays an error: "First Name must not exceed 120 characters" or "Last Name must not exceed 120 characters."
- Outcome: Submission is blocked until the name is shortened.

**2.c. Date of Birth Indicates User is Under 16**

- Condition: The entered Date of Birth results in an age less than 18 (e.g., "2010-01-01" for a 15-year-old in 2025).
- Action: Server-side validation calculates the age and displays: "You must be at least 18 years old to register."
- Outcome: Submission is blocked. The user must correct the Date of Birth or abandon registration.

**2.d. Postcode Format is Invalid**

- Condition: The postcode does not match the expected format for the selected country (e.g., "ABCDE" for a US postcode expecting "12345").
- Action: Client-side validation (using regex or a library like libphonenumber) shows an inline error: "Invalid postcode format."
- Outcome: Submission is blocked until a valid postcode is entered.

**2.e. Phone Number is Invalid**

- Condition: The phone number is too short, contains letters, or does not match the country’s format (e.g., "123" or "abc-123-4567").
- Action: Client-side and server-side validation display: "Invalid phone number format."
- Outcome: Submission is blocked until a valid phone number is provided.

**2.f. Email Address Format is Invalid**

- Condition: The email lacks proper structure (e.g., "user@.com" or "user.example.com").
- Action: Client-side validation shows: "Invalid email format."
- Outcome: Submission is blocked until a valid email is entered.

**2.g. Password is Too Weak**

- Condition: Password does not meet complexity requirements (e.g., < 8 characters, no uppercase, no numbers, no special characters).
- Action: Client-side validation displays: "Password must be at least 8 characters and include uppercase, lowercase, numbers, and special characters."
- Outcome: Submission is blocked until a stronger password is provided.

**5.a. Email Already Exists**

- Condition: The entered email matches an existing record in the database (case-insensitive).
- Action: Server-side check returns: "Email address is already in use."
- Outcome: Submission is blocked. The user is prompted to use a different email or recover the existing account.

**5.b. Phone Number Already Exists**

- Condition: The entered phone number matches an existing record.
- Action: Server-side check returns: "Phone number is already in use."
- Outcome: Submission is blocked. The user must provide a unique phone number.

**6.a. System/Database Failure During Storage**

- Condition: A database error occurs (e.g., connection timeout, server crash).
- Action: The system logs the error for debugging and displays: "Unable to create account. Please try again later."
- Outcome: The user is prompted to retry. The system may send an alert to administrators for investigation.

### Scenario Table

| **ID** | **Scenario Name**                         | **Description**                                                                 |
|------------|----------------------------------------|-----------------------------------------------------------------------------|
| S1-01       | Successful registration               | All fields are correctly filled. System stores data and shows success msg. |
| S1-02       | Missing First Name                    | First Name is empty → Inline error.                                        |
| S1-03       | Missing Last Name                     | Last Name is empty → Inline error.                                         |
| S1-04       | Missing Date of Birth                 | DOB is empty → Inline error.                                               |
| S1-05       | Underage User                         | DOB indicates < 16 → Error shown.                                          |
| S1-06       | Missing Address                       | Address is empty → Inline error.                                           |
| S1-07       | Missing Postcode                      | Postcode is empty → Inline error.                                          |
| S1-08       | Invalid Postcode                      | Alphabetic characters used → Validation fails.                             |
| S1-09       | Missing City                          | City is empty → Inline error.                                              |
| S1-10       | Missing State                         | State is empty → Inline error.                                             |
| S1-11       | Missing Country                       | Country not selected → Error shown.                                        |
| S1-12       | Missing Phone                         | Phone is empty → Inline error.                                             |
| S1-13       | Invalid Phone Format                  | Letters or short number → Error shown.                                     |
| S1-14       | Missing Email                         | Email is empty → Inline error.                                             |
| S1-15       | Invalid Email Format                  | Invalid format (e.g., missing “@”) → Error shown.                          |
| S1-16       | Duplicate Email                       | Email already exists → Error displayed.                                    |
| S1-17       | Missing Password                      | Password is empty → Inline error.                                          |
| S1-18       | Weak Password                         | Password lacks complexity → Error shown.                                   |
| S1-19       | Duplicate Phone Number                | Phone number exists → Error displayed.                                     |
| S1-20       | Database Save Failure                 | Backend error occurs → Error message shown.                                |


## Feature 2: Checkout Process

### Description

The **Checkout** feature enables a logged-in user to complete a purchase. The system validates the shopping cart contents, shipping information, and payment details. If all information is valid, it processes the payment, updates inventory, sends a confirmation email, and displays a success message to the user.

The checkout process includes the following key components:

- Shopping Cart: A list of items the user intends to purchase, including quantities and total cost.
- Shipping Information: Required fields such as Address, Postcode, City, State, Country, and Phone Number.
- Payment Details: Selected payment method (e.g., Credit Card, PayPal) and secure payment data input.
- Confirmation and Receipt: A final success screen and confirmation email after a successful transaction.

### Basic Flow

1. User Navigation: The logged-in user navigates to the Checkout page.
2. Cart Review: The user reviews their cart contents including item details, quantity, and total cost.
3. Shipping Information: The user enters or confirms their shipping details:
   - Address, Postcode, City, State, Country, Phone Number
4. Payment Selection: The user selects a payment method such as Credit Card or PayPal.
5. Order Submission: The user clicks the “Confirm Order” button.
6. Payment Processing: The system processes the payment via a secure payment gateway.
7. Inventory Update: The system updates inventory based on the items purchased.
8. Confirmation Email: The system sends a confirmation email to the user’s registered email.
9. Success Message: The system displays the message: “Order placed successfully.”

### Alternate Flows

**1.a. User is Not Logged In**

- Condition: The user is not logged in when accessing the checkout page.
- Action: The system redirects the user to the login page with a message: "Please log in to proceed with checkout."
- Outcome: User must log in to continue with checkout.

**2.a. Cart is Empty**

- Condition: The user's cart contains no items.
- Action: The system displays an error message: "Your cart is empty. Add items to proceed."
- Outcome: User cannot proceed until the cart has items.

**3.a. Missing Shipping Information**

- Condition: One or more required shipping fields are left blank.
- Action: Inline error messages are displayed for each missing field. Submission is blocked.
- Outcome: The user must complete all required fields.

**3.b. Invalid Shipping Information**

- Condition: One or more fields contain invalid data (e.g., invalid postcode format or phone number).
- Action: Inline error message is displayed next to the invalid field.
- Outcome: Submission is blocked until the information is corrected.

**4.a. No Payment Method Selected**

- Condition: The user does not select any payment method.
- Action: The system displays the message: "Please select a payment method."
- Outcome: User must choose a method to proceed.

**6.a. Payment Fails**

- Condition: The payment gateway returns an error (e.g., card declined, network failure).
- Action: The system shows the error: "Payment failed. Please check your payment details."
- Outcome: User can correct details and retry.

**7.a. Insufficient Inventory**

- Condition: One or more items in the cart are no longer in stock.
- Action: The system displays the message: "One or more items are out of stock."
- Outcome: User must adjust the cart before proceeding.

**8.a. Confirmation Email Fails**

- Condition: Email fails to send due to server error.
- Action: The system logs the failure and displays a warning: "Email confirmation could not be sent."
- Outcome: Order is still placed successfully, but user may not receive an email.

### Scenario Table

| **ID** | **Scenario Name**                     | **Description**                                                                 |
|------------|----------------------------------------|-----------------------------------------------------------------------------|
| S2-01       | Successful checkout               | All steps completed successfully → Order placed and confirmation shown.    |
| S2-02       | User not logged in                | Redirected to login page.                                                  |
| S2-03       | Cart is empty                     | Error message shown; cannot proceed.                                       |
| S2-04       | Missing shipping info             | One or more fields empty → Inline errors shown.                            |
| S2-05       | Invalid shipping info             | Incorrect format (e.g., invalid postcode) → Validation error.              |
| S2-06       | No payment method selected        | Error shown; form not submitted.                                           |
| S2-07       | Payment processing failure        | Payment declined → Error shown to user.                                    |
| S2-08       | Insufficient inventory            | One or more items unavailable → Error shown.                               |
| S2-09       | Email confirmation fails          | Order still placed → Email not sent; admin warned.                         |

# Use of AI Tools in Test Case Design

## AI Tool Used

- **Tool Name:** ChatGPT (OpenAI GPT-4o)
- **Access Platform:** ChatGPT Desktop Application


## Prompts Used

### For Test Case Generation (Feature S1: Customer Registration)

```plaintext
Write test cases for the feature: Customer Registration, including normal 
and edge cases, in structured table format with ID, Title, Preconditions, 
Inputs, Steps, Expected Result.
```

### For Test Case Generation (Feature S2: Checkout - UC02)

```plaintext
Generate structured test cases for Checkout feature (UC02) including valid 
checkout, invalid shipping info, missing payment method, etc.
Also include test cases for payment via Bank Transfer, Credit Card, Gift 
Card, and Buy Now Pay Later.
```

### For Bug Report Generation

```plaintext
From the failed test cases above, write bug reports in the following format: 
Defect ID, Defect Title, Description, Steps to Reproduce, Expected Result, 
Actual Result, Scenario ID, Severity, Priority.
```


## Validation and Refinement Process

1. **Cross-checked AI-generated test cases** with the actual UI behavior of the system under test (registration and checkout flow).
2. **Updated test data** in the AI-generated cases to match real input constraints (e.g., minimum password length, numeric-only fields).
3. **Manually verified** edge cases (e.g., SQL injection, emoji input, non-numeric quantities) to ensure they reflect realistic risks and conditions.
4. **Filtered redundant test cases** and rewrote ambiguous ones for clarity and testability.
5. For each **failing test case**, we validated system behavior and used that outcome to generate a corresponding bug report.


## Origin of Test Cases

| Source        | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| **AI-generated** | Core functional, boundary, and edge test cases for Customer Registration and Checkout were initially generated using ChatGPT. |
| **Manually created** | Some test inputs (e.g., product-specific names, address formats, and payment method flows) were refined or added manually based on actual system requirements and observed behavior. |
| **Bug Reports** | All bug reports for failed test cases were generated using ChatGPT after human validation of failure points. |

\pagebreak

# Self-Evaluation

| **Criteria**                | **Self-Evaluation** | **Notes**                                                                 |
|----------------------------|---------------------|---------------------------------------------------------------------------|
| **At least 2 Scenario Selection**    | 1.0 / 1.0           | Selected two relevant and realistic user scenarios from The Toolshop system. |
| **Scenario Testing**        | 2.0 / 2.0           | Clearly described scenarios and applied scenario-based thinking.         |
| **Use of AI Tools**         | 1.0 / 1.0           | Stated tool, prompts used, validation process, and usage scope.|
| **Test Execution**          | 0.5 / 0.5           | Executed all designed test cases locally and documented results.         |
| **Bug Reporting**           | 0.5 / 0.5           | Reported bugs with full reproduction steps and severity analysis.        |
| **Scenario Testing Report** | 1.0 / 1.0           | Report is clear and traceable     |
