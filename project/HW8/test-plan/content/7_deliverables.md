# Deliverables

## Test Evaluation Summaries

The test evaluation summaries for *The Toolshop* application (Sprint 5 with known issues) will consist of concise reports detailing the outcomes of each test cycle, covering assignments HW#02 (Domain Testing) through HW#07 (API Testing). The content will include pass/fail rates, key functional and performance findings, and a qualitative assessment of test execution.

## Reporting on Test Coverage

Reports on test coverage will measure the extent of testing across all required types (Domain, GUI, Automation, Performance, API) for *The Toolshop*, as outlined in the project description. The content will include a detailed breakdown of tested features (e.g., login, catalog, checkout), the number of test cases executed versus planned, and a coverage percentage (targeting a minimum of 85%), presented in a narrative document with supporting charts. 

These reports will be generated after the completion of each HW assignment cycle (e.g., post-HW#02, HW#03) and consolidated into the HW#08 Final Report. The extent of testing will be recorded using manual logs, tracked with tools like Selenium for UI automation, JMeter for performance, and Postman/Newman for API tests, with the final report due by the submission deadline.

## Perceived Quality Reports

Perceived quality reports will assess the overall quality of *The Toolshop* based on test outcomes, focusing on usability, performance, and reliability. The content will include a narrative evaluation of user interface responsiveness, API robustness, and system stability under load, supplemented by an analysis of incident logs and change requests against test coverage data. 

These reports will be formatted as part of the Test Report section in the HW#08 Final Report, produced after each major testing phase (e.g., post-HW#04 GUI Testing, HW#06 Performance Testing) and finalized before submission. Quality will be measured through manual observations, automated test results from Selenium and JMeter, and feedback from group members, with the final report reviewed by Dr. Tran Duy Hoang by 11:09 AM +07 on the deadline.

## Incident Logs and Change Requests

Incident logs and change requests will document all issues encountered during testing of *The Toolshop*, such as functional defects (e.g., failed login attempts) and performance bottlenecks. The method involves recording incidents with severity levels, reproduction steps, and status in a structured format. Change requests will track suggested fixes or enhancements, linked to specific test cases. These will be managed using a shared spreadsheet or document, integrated into the HW#08 Bug Reports, and tracked with manual updates or a basic issue tracking tool (e.g., Excel or Google Sheets).

## Smoke Test Suite and Supporting Test Scripts

The smoke test suite will consist of a set of basic tests to verify the core functionalities of *The Toolshop*, including login, catalog browsing, and checkout processes, ensuring no critical regressions in subsequent Sprint 5 builds. Supporting test scripts will be developed using Selenium for UI testing and Newman for API testing (e.g., `/users/login`), designed to run quickly and confirm system stability. These assets will be documented and delivered as part of the HW#05 Automation Testing submission, with scripts maintained in the group repository, reviewed by MSc. Ho Tuan Thanh, and updated as needed until the final HW#08 submission.

## Additional Work Products

### Detailed Test Results

Detailed test results will comprise a collection of spreadsheets or a repository documenting the step-by-step outcomes of each test case executed during HW#02 to HW#07. These will include decisions and comments, maintained manually or via a test management tool if available. While useful for reference, they are optional deliverables and not the primary measure of success, to be included in the HW#08 Final Report as supporting data, reviewed by the group leader.

### Additional Automated Functional Test Scripts

Additional automated functional test scripts will include optional enhancements beyond HW#05, such as extra Selenium scripts for edge cases (e.g., payment failures) or Newman scripts for`/payment/check` API. These will be stored as source code files or in a repository, offering flexibility for future testing but not used to assess the Test Plan’s success. They will be contributed voluntarily by the automation team and submitted with HW#08 if completed, pending TA approval.

### Test Guidelines


Test guidelines will provide a comprehensive set of instructions for the *The Toolshop* testing effort, including test-idea catalogs (e.g., scenarios for HW#03), good practice guidance (e.g., bug reporting standards), test patterns (e.g., boundary testing), fault and failure models (e.g., server crashes), and automation design standards (e.g., Selenium best practices). These will be documented as a separate section in the HW#08 Test Plan, serving as a reference but not a success metric, drafted by the group.

### Traceability Matrices

Traceability matrices will map test cases (e.g., LOGIN-001) to requirements from the *The Toolshop* specification, ensuring all critical functionalities are tested. These will be created using MS Excel, showing relationships between test inputs, outputs, and verified requirements, and included in the HW#08 Final Report. While valuable for verification, they are an optional deliverable and not the primary measure of the Test Plan’s success, maintained by the group leader.

\newpage