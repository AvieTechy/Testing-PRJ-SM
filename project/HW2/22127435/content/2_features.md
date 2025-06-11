# Feature 1: MyProfile

## Update profile

### Inputs

- **First Name**:
  - Length: Minimum 2 characters, maximum 50 characters.
  - Characters: Alphabetic, hyphens (-), and apostrophes (') allowed.
  - No numbers or special symbols (e.g., @, #, $).
  - Required field.
  - Leading/trailing whitespace should be trimmed.

- **Last Name**:
  - Length: Minimum 2 characters, maximum 50 characters.
  - Characters: Alphabetic, hyphens (-), and apostrophes (') allowed.
  - No numbers or special symbols.
  - Required field.
  - Leading/trailing whitespace should be trimmed.

- **Email**:
  - Must follow standard email format (e.g., `local-part@domain.extension`).
  - Length: Minimum 6 characters, maximum 254 characters.
  - Required field.
  - Must be unique within the system.
  - Changing the email may trigger a re-verification process.

- **Phone**:
  - Length: Minimum 7 effective digits, maximum 15 effective digits.
  - Characters: Digits, and optionally `+`, `(`, `)`, `-`, and spaces.
  - System should normalize the input.
  - Optional field.

- **Address**:
  - Length: Minimum 5 characters, maximum 100 characters.
  - Characters: Alphanumeric, spaces, and common punctuation (., , -, #, /).
  - Optional field (unless required for a specific context like shipping).

- **Postcode**:
  - Format is highly dependent on the selected Country.
  - Characters: Alphanumeric, spaces, or hyphens, depending on the country.
  - Length: Varies by country (e.g., 3-10 characters).
  - Optional, but often linked with Address and City.

- **City**:
  - Length: Minimum 2 characters, maximum 50 characters.
  - Characters: Alphabetic, spaces, and hyphens.
  - May be validated against a known list for the given Country/Postcode.
  - Optional, but often linked with Address.

- **State**:
  - Length: Minimum 2 characters, maximum 50 characters.
  - Characters: Alphabetic and spaces.
  - May be validated against a known list for the given Country.
  - Optional, but often required for specific countries (e.g., US, Canada).

- **Country**:
  - Must be a valid country name or code from a predefined list.
  - Characters: Alphabetic and spaces.
  - Required field, may have a default or be auto-detected.

### Equivalence Partitioning

- **Valid**:
  - **First/Last Name**: Updating to a name with 2-50 alphabetic characters, including hyphens or apostrophes (e.g., "Mary-Anne", "O'Connell").
  - **Email**: Updating to a correctly formatted, unique email address within the length constraints (6-254 characters) (e.g., "test_user-1@domain.co.uk").
  - **Phone**: Updating to an entry with 7-15 effective digits, with or without formatting characters (e.g., "+1 (123) 456-7890"), or clearing the field.
  - **Address**: Updating to an alphanumeric string of 5-100 characters, or clearing the field.
  - **Postcode/City/State/Country**: Updating to a valid combination for a real-world location (e.g., Postcode: "10115", City: "Berlin", State: "Berlin", Country: "Germany"), or clearing optional fields.

- **Invalid**:
  - **First/Last Name**: Attempting to save with a name that is too short (1 char), too long (>50 chars), empty, only whitespace, or contains invalid characters like numbers or symbols (@#$).
  - **Email**: Attempting to save with an email that is missing "@" or the domain part, contains spaces, is empty, too short (<6 chars), or too long (>254 chars).
  - **Phone**: Attempting to save with too few (<7) or too many (>15) effective digits, or with letters.
  - **Address**: Attempting to save with an address that is too short (<5 chars) or too long (>100 chars), if a hard rule is enforced.
  - **Postcode**: Attempting to save an invalid format for the selected country (e.g., "ABCDE" for Austria which expects 4 digits).
  - **City/State**: Attempting to save with a value containing numbers or a non-existent value for the selected country.
  - **Country**: Attempting to save a misspelled or non-existent country name (e.g., "Austriia", "Atlantis").

### Boundary Value Analysis

- **First Name Length**:
  - 1 character (invalid, min-1).
  - 2 characters (valid, min).
  - 50 characters (valid, max).
  - 51 characters (invalid, max+1).
  - Empty string (invalid, as field is required).

- **Email Length & Format**:
  - 5 characters (invalid, min-1, e.g., `a@b.c`).
  - 6 characters (valid, min, e.g., `a@b.io`).
  - 254 characters (valid, max).
  - 255 characters (invalid, max+1).
  - Empty string (invalid).
  - Missing local part (e.g., `@domain.com`, invalid).
  - Missing "@" symbol (e.g., `userdomain.com`, invalid).
  - Missing Top-Level Domain (e.g., `user@domain`, invalid).

- **Phone Effective Digit Length**:
  - 6 digits (invalid, min-1).
  - 7 digits (valid, min).
  - 15 digits (valid, max).
  - 16 digits (invalid, max+1).

- **Address Length**:
  - 4 characters (invalid, min-1).
  - 5 characters (valid, min).
  - 100 characters (valid, max).
  - 101 characters (invalid, max+1).

- **Postcode (example for Austria: 4 digits)**:
  - 3 digits, e.g., `123` (invalid, too short).
  - 4 digits, e.g., `1234` (valid).
  - 5 digits, e.g., `12345` (invalid, too long).
  - Non-digit string, e.g., `ABCD` (invalid, wrong type).

- **City/State Length (assuming min 2, max 50)**:
  - 1 character (invalid, min-1).
  - 2 characters (valid, min).
  - 50 characters (valid, max).
  - 51 characters (invalid, max+1).

## Change Password

### Inputs

- **Current Password**:
  - Must not be empty.
  - Must match the user's currently stored password.

- **New Password**:
  - Length: Must be at least 8 characters long (and may have a max length, e.g., 64).
  - Case: Must contain at least one uppercase letter (A-Z) and one lowercase letter (a-z).
  - Numeric: Must include at least one number (0-9).
  - Special Symbol: Must have at least one special symbol (e.g., @, #, $, !).
  - Must not be the same as the "Current Password".

- **Confirm New Password**:
  - Must not be empty if "New Password" is filled.
  - Must exactly match the value in the "New Password" field.

- **Show/Hide Password Toggles**:
  - A UI interaction that toggles the text visibility in the associated password field.

### Equivalence Partitioning

- **Valid**:
  - Correct current password, a new password that meets all complexity rules (length, case, number, symbol), and a confirmation password that perfectly matches the new one.

- **Invalid**:
  - Current password field is empty.
  - Current password entered is incorrect.
  - New password is the same as the current password.
  - New password is empty.
  - New password is too short (less than 8 characters).
  - New password is missing an uppercase letter.
  - New password is missing a lowercase letter.
  - New password is missing a number.
  - New password is missing a special symbol.
  - New password exceeds the maximum length (e.g., >64 characters).
  - Confirm New Password field is empty when New Password is not.
  - Confirm New Password does not match the New Password.

### Boundary Value Analysis

- **New Password Length (Min: 8, Max: 64)**:
  - 7 characters (invalid, min-1).
  - 8 characters (valid, min).
  - 9 characters (valid, min+1).
  - 63 characters (valid, max-1).
  - 64 characters (valid, max).
  - 65 characters (invalid, max+1).

- **Password Complexity Rules (testing one rule at a time while others are met)**:
  - 0 uppercase letters (invalid).
  - 1 uppercase letter (valid).
  - 0 lowercase letters (invalid).
  - 1 lowercase letter (valid).
  - 0 numbers (invalid).
  - 1 number (valid).
  - 0 special symbols (invalid).
  - 1 special symbol (valid).

# Feature 2: Order Management

## Order Listing & Search

### Inputs

- **Search Text Field**:
  - Accepts alphanumeric and special characters.
  - Searches across multiple order fields (e.g., Invoice Number, Billing Address, Status).
  - May have a maximum length (e.g., 255 characters).

- **Search Button**:
  - Triggers the filtering of the order list based on the search term.

- **Reset Button**:
  - Clears the search field and restores the full, unfiltered list of orders.

- **Edit Button**:
  - Navigates the user to the detail page for a specific order.

### Equivalence Partitioning

- **Valid**:
  - Search term is a full, existing Invoice Number (e.g., "INV-2022000002") → one result shown.
  - Search term is a partial, existing Billing Address (e.g., "Midway Road") → one or more matching results shown.
  - Search term is an existing Status (e.g., "COMPLETED") → all orders with that status are shown.
  - Search term is case-insensitive (e.g., searching "completed" finds "COMPLETED").

- **Invalid**:
  - Search term does not exist in any record (e.g., "NonExistentOrder123") → no results shown / "not found" message.
  - Search term consists only of special characters not expected in data (e.g., "!@#$%^") → likely no results shown.

### Boundary Value Analysis

- **Search Field Length (Max: 255)**:
  - Empty string (should show all orders, same as reset).
  - Single character (valid, may return many results).
  - 255 characters (valid, max).
  - 256 characters (invalid, should be prevented or truncated).

## Order Detail Management

### Inputs

- **Status Dropdown**:
  - A predefined, non-editable list of options.
  - User must select an option from the list.

- **Update Status Button**:
  - Submits the selected status change to the system.

- **Back Link**:
  - Navigates the user back to the main order list page.

### Equivalence Partitioning

- **Valid**:
  - Changing the status from its current value to a different valid value.
  - Clicking "Update Status" without changing the value (e.g., current status is "COMPLETED", select "COMPLETED" again and update).

- **Invalid**:
  - Attempting to update with a non-existent status (requires API or DOM manipulation to test, should be rejected by the backend).
  - Attempting to update with a null or empty selection (if possible, should result in a validation error).

### Boundary Value Analysis

- For a dropdown with a discrete set of text-based options, traditional numeric BVA is not directly applicable. Equivalence Partitioning is more relevant.
- Testing the **first** and **last** items in the dropdown list can be considered a form of BVA to ensure the range of options is handled correctly, but it is functionally similar to testing any other valid option.