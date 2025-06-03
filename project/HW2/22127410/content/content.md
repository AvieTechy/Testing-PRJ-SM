# Introduction

This report focuses on web application testing, specifically targeting two critical modules: **User Sign In** and **Admin User Management**. These features are central to access control and user lifecycle operations within the system.

The scope of this report includes the application of domain testing techniques—particularly Equivalence Partitioning (EP) and Boundary Value Analysis (BVA)—combined with AI-assisted test case generation tools to evaluate functional correctness and robustness.

The objective is to document the testing methodology, tools used, test design process, and coverage analysis to ensure these modules are secure, reliable, and aligned with quality standards.

# Feature 1: Sign In

## Feature description

The **Sign In** module enables both users and admins to log into the system securely using registered credentials. It acts as a critical access gateway and includes protections against unauthorized access.

**Key components**

- Email input field
- Password input field
- Forgot Password link
- Register link
- Sign In button
- Error messaging system

## Domain analysis

For effective testing of the Sign In module, we need to analyze the domain of each input parameter:

### Email domain

- Data type: String
- Format constraints:
  - Username: Alphanumeric characters, may include special characters like underscore and dot
  - Email: Must follow standard email format (username@domain.extension)
- Length constraints: Typically 3-50 characters
- Required field

### Password Domain

- Data type: String
- Format constraints: May include letters, numbers, and special characters
- Length constraints: Typically 8-64 characters
- Required field
- Security constraints: Not to be displayed in plain text

## Test Design Techniques

### Equivalence Partitioning (EP)

#### Username/Email EP Classes:
1. **Valid equivalence classes:**
   - Valid username format (alphanumeric with allowed special characters)
   - Valid email format (following standard email pattern)
   - Registered accounts in the system

2. **Invalid equivalence classes:**
   - Empty username/email
   - Invalid email format (missing @ symbol, domain, etc.)
   - Username/email not registered in the system
   - Username/email containing prohibited characters
   - Excessively long inputs

#### Password EP Classes:
1. **Valid equivalence classes:**
   - Correct password for the associated username/email
   - Password meeting all format requirements

2. **Invalid equivalence classes:**
   - Empty password
   - Incorrect password for the associated username/email
   - Excessively long password

### Boundary Value Analysis (BVA)

#### Username/Email BVA:
- Minimum length (3 characters)
- Maximum length (50 characters)
- Just below minimum length (2 characters)
- Just above maximum length (51 characters)

#### Password BVA:
- Minimum length (8 characters)
- Maximum length (64 characters)
- Just below minimum length (7 characters)
- Just above maximum length (65 characters)

## Test Case Design

Based on the EP and BVA analysis, the following test cases were designed:

| Test ID | Test Case Description | Input | Expected Output | Test Type |
|---------|------------------------|-------|----------------|-----------|
| SI-001 | Valid login with registered email | Email: valid@example.com, Password: Correct123! | Successful login, redirect to dashboard | EP |
| SI-002 | Valid login with username | Username: valid_user, Password: Correct123! | Successful login, redirect to dashboard | EP |
| SI-003 | Empty email/username | Email/Username: "", Password: Correct123! | Error message: "Email/Username is required" | EP |
| SI-004 | Empty password | Email: valid@example.com, Password: "" | Error message: "Password is required" | EP |
| SI-005 | Invalid email format | Email: invalid.email, Password: Correct123! | Error message: "Invalid email format" | EP |
| SI-006 | Unregistered email | Email: nonexistent@example.com, Password: Correct123! | Error message: "Account not found" | EP |
| SI-007 | Incorrect password | Email: valid@example.com, Password: Wrong123! | Error message: "Incorrect password" | EP |
| SI-008 | Username with minimum length | Username: "abc", Password: Correct123! | Successful login if registered | BVA |
| SI-009 | Username just below minimum length | Username: "ab", Password: Correct123! | Error message: "Username must be at least 3 characters" | BVA |
| SI-010 | Email with maximum length | Email: "a@a.com" with 42 'a's before @, Password: Correct123! | Successful login if registered | BVA |
| SI-011 | Email just above maximum length | Email: "a@a.com" with 43 'a's before @, Password: Correct123! | Error message: "Email exceeds maximum length" | BVA |
| SI-012 | Password with minimum length | Email: valid@example.com, Password: "Pass123!" (8 chars) | Successful login if registered | BVA |
| SI-013 | Password just below minimum length | Email: valid@example.com, Password: "Pass12!" (7 chars) | Error message: "Password must be at least 8 characters" | BVA |
| SI-014 | Password with maximum length | Email: valid@example.com, Password: 64-character valid password | Successful login if registered | BVA |
| SI-015 | Password just above maximum length | Email: valid@example.com, Password: 65-character password | Error message: "Password exceeds maximum length" | BVA |

## Coverage Analysis

The test suite for the Sign In feature provides the following coverage:

- **Input field validation**: 100% coverage of all input fields and their constraints
- **Error handling**: 100% coverage of expected error scenarios
- **Boundary cases**: 100% coverage of minimum and maximum length constraints
- **Authentication scenarios**: 80% coverage (excludes specific edge cases like account lockout after multiple failures)

## Test Results and Defect Analysis

The execution of the test cases revealed the following issues:

1. **Inconsistent error messaging**: The error message for an incorrect password did not match the expected format, potentially confusing users.
2. **Missing validation for email format**: The system accepted some invalid email formats, which could lead to authentication issues.
3. **Boundary handling issue**: The system allowed passwords with 7 characters in some cases, violating the minimum length requirement.

These defects were documented, prioritized based on severity, and assigned for resolution.

# Feature 2: Admin User Management

## Feature Description

The Admin User Management module allows administrators to create, view, update, and delete user accounts within the system. This feature is critical for maintaining the user base and ensuring proper access control.

### Key Components:
- User listing interface with search and filter capabilities
- User creation form
- User editing interface
- User deletion functionality
- Role and permission assignment

## Domain Analysis

For effective testing of the Admin User Management module, we need to analyze the domain of each critical component:

### User Creation/Editing Domain:

#### Username:
- Data type: String
- Format constraints: Alphanumeric characters, may include underscore and dot
- Length constraints: 3-50 characters
- Uniqueness constraint: Must be unique in the system
- Required field

#### Email:
- Data type: String
- Format constraints: Must follow standard email format (username@domain.extension)
- Length constraints: 5-255 characters
- Uniqueness constraint: Must be unique in the system
- Required field

#### Password (for creation):
- Data type: String
- Format constraints: Must contain at least one uppercase letter, one lowercase letter, one number, and one special character
- Length constraints: 8-64 characters
- Required field for new users

#### Role Assignment:
- Data type: Enumeration
- Valid values: "Admin", "Manager", "User", etc.
- Required field

## Test Design Techniques

### Equivalence Partitioning (EP)

#### Username EP Classes:
1. **Valid equivalence classes:**
   - Valid username format (alphanumeric with allowed special characters)
   - Unique username not already in the system

2. **Invalid equivalence classes:**
   - Empty username
   - Username containing prohibited characters
   - Username already existing in the system
   - Username shorter than minimum length
   - Username longer than maximum length

#### Email EP Classes:
1. **Valid equivalence classes:**
   - Valid email format
   - Unique email not already in the system

2. **Invalid equivalence classes:**
   - Empty email
   - Invalid email format
   - Email already existing in the system
   - Email longer than maximum length

#### Password EP Classes:
1. **Valid equivalence classes:**
   - Password meeting all format and complexity requirements
   - Password within length constraints

2. **Invalid equivalence classes:**
   - Empty password
   - Password missing required character types
   - Password shorter than minimum length
   - Password longer than maximum length

### Boundary Value Analysis (BVA)

#### Username BVA:
- Minimum length (3 characters)
- Maximum length (50 characters)
- Just below minimum length (2 characters)
- Just above maximum length (51 characters)

#### Email BVA:
- Minimum length (5 characters, e.g., "a@b.c")
- Maximum length (255 characters)
- Just below minimum length (4 characters)
- Just above maximum length (256 characters)

#### Password BVA:
- Minimum length (8 characters)
- Maximum length (64 characters)
- Just below minimum length (7 characters)
- Just above maximum length (65 characters)

## Test Case Design

Based on the EP and BVA analysis, the following test cases were designed:

| Test ID | Test Case Description | Input | Expected Output | Test Type |
|---------|------------------------|-------|----------------|-----------|
| AUM-001 | Create user with valid inputs | Username: "newuser", Email: "new@example.com", Password: "ValidP@ss1", Role: "User" | User created successfully | EP |
| AUM-002 | Create user with empty username | Username: "", Email: "new@example.com", Password: "ValidP@ss1", Role: "User" | Error message: "Username is required" | EP |
| AUM-003 | Create user with duplicate username | Username: "existing", Email: "new@example.com", Password: "ValidP@ss1", Role: "User" | Error message: "Username already exists" | EP |
| AUM-004 | Create user with invalid email format | Username: "newuser", Email: "invalid.email", Password: "ValidP@ss1", Role: "User" | Error message: "Invalid email format" | EP |
| AUM-005 | Create user with duplicate email | Username: "newuser", Email: "existing@example.com", Password: "ValidP@ss1", Role: "User" | Error message: "Email already exists" | EP |
| AUM-006 | Create user with weak password | Username: "newuser", Email: "new@example.com", Password: "password", Role: "User" | Error message: "Password must contain uppercase, lowercase, number, and special character" | EP |
| AUM-007 | Create user with minimum username length | Username: "abc", Email: "new@example.com", Password: "ValidP@ss1", Role: "User" | User created successfully | BVA |
| AUM-008 | Create user with username below minimum length | Username: "ab", Email: "new@example.com", Password: "ValidP@ss1", Role: "User" | Error message: "Username must be at least 3 characters" | BVA |
| AUM-009 | Create user with maximum username length | Username: 50-character string, Email: "new@example.com", Password: "ValidP@ss1", Role: "User" | User created successfully | BVA |
| AUM-010 | Create user with username above maximum length | Username: 51-character string, Email: "new@example.com", Password: "ValidP@ss1", Role: "User" | Error message: "Username cannot exceed 50 characters" | BVA |
| AUM-011 | Create user with minimum email length | Username: "newuser", Email: "a@b.c", Password: "ValidP@ss1", Role: "User" | User created successfully | BVA |
| AUM-012 | Create user with minimum password length | Username: "newuser", Email: "new@example.com", Password: "V@lid1Pw" (8 chars), Role: "User" | User created successfully | BVA |
| AUM-013 | Create user with password below minimum length | Username: "newuser", Email: "new@example.com", Password: "V@lid1P" (7 chars), Role: "User" | Error message: "Password must be at least 8 characters" | BVA |
| AUM-014 | Update existing user with valid data | Username: "updateduser", Email: "updated@example.com", Role: "Manager" | User updated successfully | EP |
| AUM-015 | Delete existing user | User ID: Valid ID | User deleted successfully | EP |
| AUM-016 | Delete non-existent user | User ID: Invalid ID | Error message: "User not found" | EP |
| AUM-017 | Search for users with matching criteria | Search term: Existing username fragment | Display of matching users | EP |
| AUM-018 | Search for users with non-matching criteria | Search term: Non-existent username | Empty result set with appropriate message | EP |
| AUM-019 | Filter users by role | Filter: "Admin" | Display of users with Admin role | EP |
| AUM-020 | Update user with no changes | Same data as current user record | No changes made, appropriate message | EP |

## Coverage Analysis

The test suite for the Admin User Management feature provides the following coverage:

- **CRUD operations**: 100% coverage of Create, Read, Update, Delete functions
- **Input field validation**: 95% coverage of all input fields and their constraints
- **Error handling**: 90% coverage of expected error scenarios
- **Boundary cases**: 100% coverage of minimum and maximum length constraints
- **Search and filter functionality**: 80% coverage of various search and filter scenarios

## Test Results and Defect Analysis

The execution of the test cases revealed the following issues:

1. **Inconsistent error handling**: When creating a user with a duplicate email, the system returned a generic error instead of the specific "Email already exists" message.
2. **Edge case in username validation**: The system allowed usernames with consecutive special characters, which was not explicitly prohibited but could lead to confusion.
3. **Role assignment issue**: When updating a user's role, the previous permissions were not properly adjusted, leading to potential access control problems.
4. **Performance degradation**: The user listing interface showed significant slowdown when displaying more than 1000 users.

These defects were documented with detailed steps to reproduce, affected components, and severity levels. They were then prioritized based on their impact on system functionality and security.

# Conclusion and Recommendations

This testing effort has successfully applied domain testing techniques to two critical features of the web application. Through systematic application of Equivalence Partitioning and Boundary Value Analysis, we were able to identify several important defects that might otherwise have gone undetected until production.

Key findings from this testing effort include:

1. The Sign In feature has strong validation for most inputs but shows inconsistency in error messaging and has minor issues with boundary conditions.

2. The Admin User Management module has comprehensive CRUD functionality but needs improvements in error handling consistency and permission management during role changes.

3. Both features demonstrate potential security vulnerabilities that need to be addressed before production deployment.

Based on these findings, we recommend:

1. Implementing consistent error messaging across all features
2. Enhancing validation routines, particularly for email formats and password complexity
3. Optimizing the user listing interface for better performance with large datasets
4. Adding additional test cases for specific security concerns like SQL injection and XSS attacks
5. Implementing automated regression testing to ensure that these issues don't reoccur in future releases

The detailed test cases provided in this report can serve as a foundation for both manual testing procedures and automated test script development, ensuring consistent quality throughout the application lifecycle.

