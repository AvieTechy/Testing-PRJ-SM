# AI Tool Usage

## Qase

# AI Tool Usage

## Qase

An overview of Qase.io:

*   **Tool:** Qase.io
*   **AI Feature:** Generates test cases using description prompts.
*   **URL:** [https://qase.io](https://qase.io)

## Prompt sử dụng

1.

Title
```text
Generate test cases for Sign Up
```
Description
```text
The Sign Up form includes the following fields:

- Full name (required)
- Email (required, must be valid format)
- Password (min 8 characters, at least 1 special character)
- Confirm password (must match Password)
- Agree to terms (checkbox)

Please generate test cases to validate:

- Valid and invalid inputs for all fields
- Email format validation
- Password mismatch
- Boundary tests for password length
- Missing required fields
```

2.

```text
Generate test cases for Checkout and Payment
```
Description
```text
The checkout process includes:

- Adding items to cart
- Proceeding to checkout as guest or logged-in user
- Entering shipping information
- Selecting payment method (Credit Card, PayPal)
- Validating required fields and format
- Handling failed payment or missing info

Generate test cases covering:

- Success and failure flows
- Required field validations
- Format validations
- Boundary values for price/quantity
- Cancel or back behavior
```

3.

```text
Generate test cases for Admin – Product Management
```

```text
The Admin panel allows managing products:

- Add new product (name, category, price, stock, image)
- Edit existing product
- Delete product
- Search and filter product list

Please generate test cases for:

- Valid/invalid input on add/edit forms
- Field validation (required, data types)
- Deleting confirmation flow
- Search and filter functionality
- Permission/access for admin only
```

## Result

# Manual domain test design


# Comparative analysis

# Bugs reported

# Self-assessment

| Criteria | Outcomes                  | Percent | Grade | Self-Assessed Grade |
| :------- | :------------------------ | :------ | :---- | :------------------ |
| 1        | AI tools                  | 40%     | 10    | 4                   |
| 2        | Manual Domain Test Design | 40%     | 10    | 4                   |
| 3        | Comparison and Analysis   | 20%     | 10    | 2                   |
|          | **Total**                 | 100%    |       | 10                  |
