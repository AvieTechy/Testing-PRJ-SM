# Feature 1: Sign In

## Inputs

- **Email**:
  - Valid email format (e.g., "user@domain.com").
  - Registered in the system.
  - Maximum 100 characters.
  - No newlines, HTML, SQL, XSS payloads, or Unicode characters.
  - Leading/trailing spaces are trimmed.
  - Case-sensitive (e.g., "CUSTOMER@PRACTICESOFTWARETESTING.COM" treated differently).
- **Password**:
  - Minimum 8 characters, maximum 30 characters.
  - No spaces, newlines, HTML, SQL, XSS payloads, or Unicode characters.
  - Must match the registered password for the email.

## Equivalence Partitioning

- **Valid**:
  - Registered user email with correct password (e.g., "customer@practicesoftwaretesting.com", "welcome01" → user dashboard).
  - Registered admin email with correct password (e.g., "admin@practicesoftwaretesting.com", "welcome01" → admin dashboard).
  - Email with leading/trailing spaces (e.g., " customer@practicesoftwaretesting.com " → trimmed, user dashboard).

- **Invalid**:
  - Invalid email format (e.g., "customerpracticesoftwaretesting.com").
  - Empty email or password.
  - Incorrect password for registered email (e.g., "customer@practicesoftwaretesting.com", "welcome02").
  - Unregistered email (e.g., "customer12@practicesoftwaretesting.com").
  - HTML injection in email or password (e.g., "<script>alert(1)</script>").
  - SQL injection in email or password (e.g., "' OR 1=1 --'").
  - XSS payload in email or password (e.g., "<img src=x onerror=alert(1)>").
  - Email or password with newlines (e.g., "customer\\n@practicesoftwaretesting.com").
  - Email or password with Unicode characters (e.g., "cüstomer@practicesoftwaretesting.com").
  - Email exceeding maximum length (e.g., 101+ characters).
  - Password with spaces (e.g., "welcome01  ").
  - Three or more consecutive failed login attempts (locks account).

## Boundary Value Analysis

- **Email Length**:
  - 1 character (invalid, e.g., "a").
  - Valid email at maximum length (100 characters, valid if registered).
  - 101 characters (invalid).

- **Password Length**:
  - 8 characters (valid, e.g., "Abcd1234").
  - 7 characters (invalid).
  - 30 characters (valid).
  - 31 characters (invalid).

- **Login Attempts**:
  - 2 failed attempts (valid, can still login with correct credentials).
  - 3 failed attempts (invalid, account locked).
  - 4th attempt after lock (invalid, remains locked even with correct credentials).

# Feature 2: User Management

## Inputs

- **First Name**: Non-empty string, maximum 50 characters, no special characters (e.g., "#", "$"), no emojis.
- **Last Name**: Non-empty string, maximum 50 characters, no special characters, no emojis.
- **Date of Birth (DOB)**: Valid date, not in the future, not before 1905.
- **Country**: Selected from a predefined list (e.g., "USA", "Zimbabwe").
- **Email**: Valid format, unique, maximum 100 characters, no newlines or spaces.
- **Password**: Minimum 8 characters, maximum 50 characters.
- **Phone Number**: Numeric, minimum 10 digits, maximum 15 digits.
- **Address**: Includes street (non-empty), city (non-empty), state (non-empty), postal code (non-empty), country (selected).
- **Postal Code**: Non-empty, valid format (not specified, but tested as required).
- **State**: Non-empty string.
- **Enabled Status**: Checkbox to enable/disable user account (for editing).

## Equivalence Partitioning

- **Valid**:
  - All fields filled with valid data (e.g., First Name: "Jane", Last Name: "Doe", DOB: "01/01/1990", Country: "USA", Email: "jane@test.com", Password: "Password123", Phone: "1234567890", Address: complete).
  - Minimum valid inputs (e.g., First Name: "A", Last Name: "B", Email: "a@b.c", DOB: "04/06/2007").
  - Maximum valid inputs (e.g., First Name and Last Name: 50 characters, Email: 100 characters, Password: 50 characters).
  - Edit user with valid updates (e.g., change First Name to "John").
  - Edit user with no changes.
  - Delete existing user (if not restricted by dependencies).

- **Invalid**:
  - Empty First Name, Last Name, DOB, Country, Email, Password, Phone, Address, City, State, or Postal Code.
  - Special characters in First Name or Last Name (e.g., "Ja#ne").
  - Future DOB (e.g., "05/06/2025").
  - DOB before 1905 (e.g., "01/01/1900").
  - Invalid email format (e.g., "jane@").
  - Duplicate email (e.g., "jane@test.com" already registered).
  - Password less than 8 characters (e.g., "1").
  - Invalid phone number (e.g., "abc", 9 digits, or 16 digits).
  - No payment method selected.
  - Edit user with invalid email, future DOB, or empty required fields.
  - Delete user with dependencies (e.g., user linked to other records).

## Boundary Value Analysis

- **First Name/Last Name**:
  - 1 character (valid, e.g., "A").
  - 50 characters (valid).
  - 51 characters (invalid).

- **Email Length**:
  - Valid email at maximum length (100 characters, valid if unique).
  - 101 characters (invalid).

- **Password Length**:
  - 8 characters (valid).
  - 7 characters (invalid).
  - 50 characters (valid).
  - 51 characters (invalid).

- **Phone Number**:
  - 10 digits (valid, e.g., "1234567890").
  - 9 digits (invalid).
  - 15 digits (valid, e.g., "+123456789012345").
  - 16 digits (invalid).

- **DOB**:
  - 04/06/1905 (valid).
  - 04/05/1905 (invalid, too old).
  - Current date (invalid, future DOB).
  - One day before current date (invalid, too young).
