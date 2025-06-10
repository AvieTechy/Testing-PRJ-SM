# Test Execution & Bug Report

## Test Execution

### Process

The test execution for the practice-software-testing project was conducted by tester Lưu Thanh Thuý on Excel date 45811 (approximately April 25, 2025). The testing focused on two key features: Sign In (UC01) and User Management (UC02). Test cases were designed using Equivalence Partitioning (EP) and Boundary Value Analysis (BVA) techniques to cover valid and invalid input scenarios, as outlined in the test case document. A total of 66 test cases were executed (32 for Sign In, 34 for User Management) using manual testing methods. The testing environment included a web-based login interface and an admin dashboard for user management, accessed via a standard browser. Each test case followed predefined steps, with inputs validated against expected results. Defects were logged in the bug report with detailed descriptions, steps to reproduce, and severity levels.

### Results

- **Total Test Cases**: 66 (32 for Sign In, 34 for User Management).
- **Passed**: 18 test cases (e.g., valid user/admin login, adding users with valid/minimum/maximum inputs).
- **Failed**: 48 test cases, primarily due to improper error handling (e.g., generic error messages for invalid inputs) and incorrect system behavior (e.g., allowing invalid user data, failing to lock accounts after three failed logins).
- **Defects Identified**: 36 defects (20 for Sign In, 16 for User Management), with severities ranging from Low to High.

### Key Observations:

- The Sign In feature frequently displayed generic error messages ("Invalid email or password") instead of specific validation errors (e.g., "Email is required" or "Invalid email format").
- The User Management feature incorrectly allowed adding/editing users with invalid data (e.g., special characters in names, future DOB, duplicate emails).
- Account locking after three failed login attempts was not enforced, posing a security risk.
- Screenshots were not properly captured (#VALUE! error in bug report), complicating defect verification.



## Bug Report

### Identified Bugs

The following defects were identified during testing, categorized by feature:

1. Sign In (UC01)

- **B001-B004**: Generic error messages for invalid email format, empty email, empty password, and incorrect password instead of specific warnings *(Medium severity)*.
- **B005-B006**: HTML injection in email/password fields not validated, showing generic errors *(High and Low severity)*.
- **B007-B008**: Very long email/password inputs not handled, showing generic errors *(Medium and Low severity)*.
- **B009**: Valid email with uppercase letters fails to log in *(Low severity)*.
- **B010-B014**: Password/email with spaces, newlines, or Unicode characters show generic errors instead of specific warnings *(Medium severity)*.
- **B015-B018**: Account not locked after three or more failed login attempts, allowing successful login post-lock *(High severity)*.
- **B019-B020**: Passwords below 8 or above 30 characters not properly validated *(Medium severity)*.

2. User Management (UC02)

- **B021**: Special characters in name fields incorrectly allowed *(Medium severity)*.
- **B022-B023**: Future or out-of-range DOB (before 1905) incorrectly allowed *(Medium severity)*.
- **B024**: Invalid email shows blank error message *(Medium severity)*.
- **B025-B028**: Short password, empty password, or just below minimum password length incorrectly allowed *(Medium to High severity)*.
- **B029-B032**: Empty postal code, state, phone, or invalid phone number incorrectly allowed *(Medium severity)*.
- **B033-B034**: Editing user with future DOB or invalid email succeeds or shows blank error *(Medium severity)*.
- **B035**: Editing user with maximum inputs succeeds correctly *(Low severity, potentially misreported as defect)*.
- **B036**: Deleting a user fails with incorrect error message due to dependencies *(High severity)*.



### Resolutions

**Current Status** 

All 36 defects remain Open as of the test execution date (45811). No resolutions have been implemented yet, pending developer review and action.

**Proposed Actions**

1. Enhance validation logic for Sign In to display specific error messages for invalid email formats, empty fields, and incorrect passwords.
2. Implement robust input sanitization to prevent HTML, SQL, and XSS injections in email/password fields.
3. Enforce account locking after three failed login attempts and prevent login post-lock.
4. Update User Management to reject invalid inputs (e.g., special characters, future DOB, duplicate emails) and display clear error messages.
5. Fix blank error messages for invalid email during user addition/editing.
6. Investigate and resolve user deletion failures due to dependencies, ensuring accurate error reporting.
7. Improve screenshot capture process to avoid #VALUE! errors in bug reports.

**Next Steps**

Escalate high-severity defects (B005, B015-B018, B026-B027, B036) to developers for immediate attention. Schedule retesting once fixes are deployed.

