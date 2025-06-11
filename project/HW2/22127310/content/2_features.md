# Feature 1: Sign Up

This section outlines the first key feature of our system: the user sign-up process. To ensure this feature works correctly, we first need to define the information users will provide.

## Inputs

The table below lists all the information fields a user needs to fill out during registration, along with the specific rules or constraints for each field. These constraints help ensure data quality and system security.

| Field             | Constraints                                                                                                |
|-------------------|-----------------------------------------------------------------------------|
| **First Name**    | Must not be empty, can have up to 50 characters. Emojis or special symbols that are not standard characters are not allowed. |
| **Last Name**     | Must not be empty, can have up to 50 characters. Emojis or special symbols that are not standard characters are not allowed. |
| **Email**         | Needs to be a valid email address format (e.g., user@example.com). Each email must be unique in the system. It should not contain newline characters or spaces at the beginning or end. |
| **Password**      | Must be at least 10 characters long and no more than 40 characters. It needs to include at least one uppercase letter, one lowercase letter, one number, and one special symbol (e.g., !, @, #). |
| **Phone Number**  | Should only contain numbers. It must be at least 10 digits long and no more than 15 digits.                 |
| **Date of Birth (DOB)** | Must be a valid date. The date cannot be in the future. Users must be at least 16 years old, and the birth year cannot be earlier than 1900. |
| **Address**       | This is a composite field including street, city, state, country, and a postal code. The postal code must be exactly 6 digits. |
| **City**          | Must not be empty. It should not contain any numbers.                                                      |
| **State**         | Must not be empty.                                                                                         |
| **Country**       | A country must be selected from the provided options.                                                      |
| **Postal Code**   | Must be exactly 6 digits long and contain only numbers. Leading zeros are allowed (e.g., "001234").          |

## Equivalence Partitioning

To test the sign-up feature effectively, we use a technique called Equivalence Partitioning. This involves dividing the possible inputs into groups, or partitions, where the system is expected to behave similarly for all inputs within a group. We define partitions for both valid (correct) and invalid (incorrect) data.

- **Valid Partition**: This represents a scenario where a user provides acceptable data for all fields.
    - Example: All fields are filled with data that meets their respective constraints (e.g., a valid name, a correctly formatted and unique email, a strong password of appropriate length, a valid phone number, an acceptable date of birth, and a complete address with a 6-digit postal code).

- **Invalid Partitions**: These represent scenarios where at least one piece of data is incorrect or missing. Testing these helps ensure the system handles errors gracefully.
    - First Name, Last Name, Email, Password, Phone, City, State, or Country field is left empty.
    - Email address is not in a valid format (e.g., "user@", contains a newline character, or has leading/trailing spaces).
    - Email address provided is already registered in the system (duplicate email).
    - Password does not meet the complexity requirements (e.g., missing an uppercase letter, a lowercase letter, a number, or a special symbol).
    - Password is too short (less than 10 characters) or too long (more than 40 characters).
    - Phone Number contains non-numeric characters or has an incorrect length (e.g., 9 digits or 16 digits).
    - Date of Birth is a future date or a date before the year 1900.
    - Postal Code does not consist of exactly 6 digits or contains non-numeric characters.
    - City name includes numbers.
    - First Name or Last Name includes emojis or is longer than 50 characters.

## Boundary Value Analysis

Another important testing technique we use is Boundary Value Analysis. This focuses on testing the values at the edges (or boundaries) of the allowed input ranges, as errors often occur at these points.

- **First Name/Last Name**:
    - 1 character (this is a valid length, e.g., "A")
    - 50 characters (this is the maximum valid length)
    - 51 characters (this should be invalid, as it exceeds the maximum length)

- **Password**:
    - 10 characters (this is the minimum valid length)
    - 9 characters (this should be invalid, as it's too short)
    - 40 characters (this is the maximum valid length)
    - 41 characters (this should be invalid, as it's too long)

- **Phone Number**:
    - 10 digits (this is the minimum valid length)
    - 9 digits (this should be invalid, as it's too short)
    - 15 digits (this is the maximum valid length)
    - 16 digits (this should be invalid, as it's too long)

- **Postal Code**:
    - 6 digits (this is the only valid length, e.g., "123456", "001234")
    - 5 digits (this should be invalid)
    - 7 digits (this should be invalid)

- **Date of Birth (DOB)**:
    - A date that makes the user exactly 16 years old (e.g., if today is June 4, 2025, then June 4, 2009, is valid).
    - A date that makes the user less than 16 years old (this should be invalid).
    - January 1, 1900 (this should be invalid, as it's too old according to the rules).

# Feature 2: Checkout

This section describes the second major feature: the product checkout process. Similar to the sign-up feature, we begin by defining the necessary inputs and their constraints.

## Inputs

The table below details the information and selections a user must provide to complete a purchase. Defining these clearly is crucial for a smooth and error-free checkout experience.

| Field                   | Constraints                                                                                                |
|-------------------------|--------------------------------------------------------------------|
| **Cart**                | The shopping cart must have at least one item. For each item, the quantity must be between 1 and 10 (inclusive). |
| **Billing Address**     | Requires street, city, state, postal code, and country information.                                        |
| **Payment Method**      | User can choose from: Cash on Delivery, Bank Transfer, Credit Card, Gift Card, or Buy Now Pay Later.        |
| **Bank Transfer Details** | If "Bank Transfer" is selected, the user must provide: Bank Name (only letters and spaces allowed), Account Name, and Account Number (must be numeric, between 8 and 34 digits long). |
| **User Authentication** | The user must be logged into their account to proceed with the checkout.                                   |

## Equivalence Partitioning

For the checkout feature, we again apply Equivalence Partitioning to group test inputs. This helps us cover various scenarios efficiently.

- **Valid Partitions**: These represent successful checkout attempts.
    - Scenario 1: The cart contains between 1 and 10 items, a complete and valid billing address is provided (street, city, state, postal code, country), and a valid payment method is selected (e.g., "Cash on Delivery").
    - Scenario 2: If "Bank Transfer" is chosen as the payment method, all bank details (Bank Name, Account Name, Account Number) must be valid according to their rules.
    - Scenario 3: A user who is already logged in should be able to proceed directly to providing billing information.

- **Invalid Partitions**: These cover situations where the checkout process should fail or prompt for corrections.
    - The shopping cart is empty.
    - The quantity for an item in the cart is invalid (e.g., 0, a negative number, not a number, or greater than 10).
    - One or more required fields in the billing address are missing (e.g., street, city, state, postal code, or country).
    - The billing address contains invalid data (e.g., numbers in the city field, or other fields left empty).
    - No payment method is selected by the user.
    - "Bank Transfer" is selected, but the provided bank details are invalid (e.g., Bank Name is empty or contains numbers, Account Number is not numeric or is too short/long).
    - A guest user (not logged in) attempts to checkout (the system should redirect them to a sign-in or sign-up page).
    - The payment method fields shown do not match the selected payment method (e.g., Credit Card is chosen, but fields for Bank Transfer details are displayed).

## Boundary Value Analysis

We also use Boundary Value Analysis for the checkout feature, focusing on the limits of acceptable input values.

- **Cart Quantity** (for a single item type):
    - 1 item (this is the minimum valid quantity)
    - 0 items (this should be invalid)
    - 10 items (this is the maximum valid quantity)
    - 11 items (this should be invalid, as it exceeds the maximum)

- **Account Number (for Bank Transfer)**:
    - 8 digits (this is the minimum valid length)
    - 7 digits (this should be invalid, as it's too short)
    - 34 digits (this is the maximum valid length)
    - 35 digits (this should be invalid, as it's too long)

- **Billing Address Fields** (examples for specific fields):
    - Street: 1 character (considered valid, e.g., "A")
    - City: 1 character (considered valid, e.g., "B")
    - Postal Code: 6 digits (this is the required valid length)
    - Postal Code: 5 digits (invalid) or 7 digits (invalid)
