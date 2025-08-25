# Testing Workflow

The workflow ensures a structured approach to testing, aligning with the HW#02 to HW#08 assignment requirements and reflecting the current date and time (11:15 AM +07, Monday, August 25, 2025).

1. **Analyze Requirements**
    
- Conduct a thorough review of the *The Toolshop* project requirements, including the Sprint 5 description from the repository[](https://github.com/testsmith-io/practice-software-testing/).
- Identify key functionalities (e.g., login, catalog, checkout) and non-functional aspects (e.g., performance, usability) as outlined in HW#02 to HW#07.
- Collaborate with group members to clarify ambiguities with TAs (e.g., Dr. Lam Quang Vu) and document findings for the HW#08 Test Plan.

2. **Design Test Cases**

- Develop test cases for each testing type (Domain, GUI, Automation, Performance, API) based on identified requirements.  
- Include positive, negative, and edge cases (e.g., invalid login credentials, bulk order processing) with clear inputs, expected outputs, and criteria, as per HW#03 guidelines.  
- Review and refine test cases within the group, ensuring coverage of known bugs.

3. **Setup Environment**

- Configure the test environment using local setups with Chrome and Firefox browsers, as specified for *The Toolshop*.  
- Install and validate tools (e.g., Selenium, JMeter, Postman) required for HW#05 and HW#06, ensuring compatibility with the Sprint 5 build.  
- Verify network stability and server access by 11:15 AM +07, August 25, 2025, and document setup details for HW#08 submission.

4. **Execute Manual Tests**

- Perform manual testing of core workflows (e.g., user registration, payment processing) as outlined in HW#02 and HW#04.
- Record step-by-step results (e.g., OK, NOK) for test cases like LOGIN-001 and CHECKOUT-001, noting any deviations or bugs.
- Involve all group members, with testing scheduled to start on Tuesday, August 26, 2025, and progress tracked daily.

5. **Run Automation**

- Execute automated test scripts developed for HW#05, using Selenium for UI (e.g., navigation testing) and Newman for API (e.g., /users/login).
- Validate script functionality against the Sprint 5 build, addressing any failures (e.g., timing issues) with adjustments.
- Schedule automation runs weekly, with results integrated into the HW#08 Final Report by the submission deadline.

6. **Run Performance Tests**

- Conduct performance testing as per HW#06 using JMeter to simulate loads (e.g., 100 concurrent users on checkout) and measure response times.
- Perform stress and volume tests to identify breaking points, focusing on catalog browsing and payment APIs.

7. **Log Defects**

- Record all identified defects (e.g., UI misalignment, API timeouts) with severity (Critical, Major, Minor), reproduction steps, and screenshots in a shared document.
- Assign bug IDs and link them to specific test cases.
- Update logs daily during testing, with a consolidated Bug Report submitted as part of HW#08.

8. **Retest and Regression**
   
- Retest fixed defects to verify resolutions, scheduled after developer feedback, starting Monday, September 1, 2025.
- Conduct regression testing using the smoke test suite and additional scripts to ensure no new issues arise, covering all HW#02 to HW#07 scopes.
- Document retest outcomes and regression results, integrating them into the HW#08 Test Case Summary.

9. **Summarize in Reports**

- Compile all testing data into a comprehensive HW#08 Final Report, including Test Plan, Test Cases, Test Case Summary, Bug Reports, and Test Report.
- Include metrics (e.g., 85% test coverage), qualitative assessments, and stakeholder recommendations, reviewed by Dr. Tran Duy Hoang.
- Finalize and submit the report via Moodle by 11:15 AM +07 on the project deadline, ensuring TA approval.

\newpage