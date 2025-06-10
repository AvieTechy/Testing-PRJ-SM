# Test Execution & Bug Reporting

All 52 designed test cases were executed on a local deployment of **The Toolshop** application, specifically the **/sprint5-with-bugs** version.

- **Execution Summary:** The execution revealed several significant, high-impact defects in the application. Of the 52 test cases, a substantial number failed, primarily within the "My Profile" feature, indicating critical issues with user data management and security.
- **Detailed Results:** The complete execution results, including actual results and Pass/Fail status for each test case, are logged in the `22127435_Test cases.xlsx` file.
- **Bugs Found:** All failed test cases resulted in the identification of bugs. Four high-impact bugs were documented. Full details, including steps to reproduce, severity and priority are available in the bug report file: `22127435_Bug Report.xlsx`.

A summary of the critical bugs found is provided below:

| Bug ID | Summary | Priority | Severity |
| :--- | :--- | :--- | :--- |
| **B001** | First Name and Last Name fields are swapped on Profile page. | High | Major |
| **B002** | Updating any user profile field fails with a "Resource not found" error. | Highest | Blocker |
| **B003** | Successful password change action locks the user out of the account. | Highest | Critical |
| **B004** | Updating an order's status incorrectly updates all other orders with the same original status. | High | Major |

\pagebreak
