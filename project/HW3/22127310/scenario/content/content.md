# Scenario Definition

## Feature S1: Customer Registration

### Description

The Customer Registration feature allows new users to create an account by filling out a registration form. The system validates the provided information, checks for duplicate email and phone number entries, and stores the new account in the database if all checks pass.

The registration form includes the following required fields:

- First Name
- Last Name
- Date of Birth
- Address
- Postcode
- City
- State
- Country
- Phone Number
- Email Address
- Password

### Basic Flow

1. The user navigates to the Customer Registration page.
2. The user fills in all required fields with valid values.
3. The user clicks the “Register” button.
4. The system performs client-side and server-side validation.
5. The system checks whether the email address and phone number already exist in the database.
6. If validation passes and there are no duplicates:
   - The account is stored in the database.
   - The system displays: **“Account created successfully.”**

### Alternate Flows

- 2.a. Required field is empty → Inline error shown; form submission is blocked.
- 2.b. First or Last Name exceeds 120 characters → Error shown.
- 2.c. Date of Birth indicates user is under 18 → Error: *"You must be at least 18 years old to register."*
- 2.d. Postcode format is invalid → Inline error shown.
- 2.e. Phone number is invalid → Error shown.
- 2.f. Email address format is invalid → Error shown.
- 2.g. Password is too weak (e.g., < 8 characters, lacks complexity) → Error shown.
- 5.a. Email already exists → Error: *"Email address is already in use."*
- 5.b. Phone number already exists → Error: *"Phone number is already in use."*
- 6.a. System/database failure during storage → Error: *"Unable to create account. Please try again later."*

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


## Feature S2: Checkout Process

### Description

The Checkout feature enables a logged-in user to complete a purchase. The system validates the shopping cart contents, shipping information, and payment details. If all information is valid, it processes the payment, updates inventory, sends a confirmation email, and displays a success message.

### Basic Flow

1. The user (already logged in) navigates to the Checkout page.
2. The user reviews their cart contents (items, quantities, total price).
3. The user enters or confirms shipping information:
   - Address, Postcode, City, State, Country, Phone Number
4. The user selects a payment method (e.g., Credit Card, PayPal).
5. The user clicks the “Confirm Order” button.
6. The system processes the payment.
7. The system updates the inventory based on the purchased items.
8. The system sends a confirmation email to the user.
9. The system displays: **“Order placed successfully.”**

### Alternate Flows

- 1.a. User is not logged in → Redirect to login with message: *"Please log in to proceed with checkout."*
- 2.a. Cart is empty → Error: *"Your cart is empty. Add items to proceed."*
- 3.a. Missing shipping information → Inline error; submission blocked.
- 3.b. Invalid shipping information → Error shown immediately.
- 4.a. No payment method selected → Error: *"Please select a payment method."*
- 6.a. Payment fails (e.g., card declined) → Error: *"Payment failed. Please check your payment details."*
- 7.a. Insufficient inventory → Error: *"One or more items are out of stock."*
- 8.a. Email sending fails → Order is placed; system logs warning: *"Email confirmation could not be sent."*

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
