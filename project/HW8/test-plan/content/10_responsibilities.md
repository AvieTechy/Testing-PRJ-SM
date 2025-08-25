# Responsibilities, Staffing, and Training Needs

## People and Roles

| Role               | Responsibilities                                                                 | Assigned To / Notes                               |
|--------------------|-----------------------------------------------------------------------------------|--------------------------------------------------|
| Test Manager       | Oversees the entire test effort, approves the Test Plan, manages risks, reviews deliverables, ensures deadlines are met. | Group leader (QA coordinator) |
| Test Analysts      | Design test cases for functional, scenario-based, GUI, and API testing; ensure coverage of requirements. | Assigned students per HW#02–HW#04 |
| Manual Testers     | Execute test cases manually, log defects, retest after fixes, validate usability issues. | All group members contribute |
| Automation Engineer| Develops and maintains Selenium scripts (UI) and Postman/Newman collections (API); integrates automation into CI/CD pipeline. | Member with coding experience |
| Performance Engineer| Designs and executes JMeter scenarios for load, stress, and spike tests; analyzes performance results. | Member responsible for HW#06 |
| Test System Admin  | Sets up and maintains test environment (Docker, databases, browsers, configurations). | Shared responsibility across group |
| Developers (supporting role)| Provide builds, fix defects, clarify requirements. | Not in QA team scope, but interacts with testers |

## Staffing and Training Needs

| Area                  | Training / Knowledge Needed                                                  | Plan / Approach                                    |
|-----------------------|-------------------------------------------------------------------------------|---------------------------------------------------|
| Selenium Automation   | Writing and running WebDriver scripts for UI regression testing              | Short internal workshop; practice on login/logout flows |
| Postman/Newman        | Creating collections, writing assertions, integrating into GitHub Actions     | Hands-on sessions during HW#07; group peer support |
| JMeter                | Setting up thread groups, simulating load, analyzing reports                 | Instructor tutorials + online docs; dry run before HW#06 submission |
| Docker Environment    | Running Laravel + MySQL using Docker Compose                                 | One member documents setup guide for the group     |
| Defect Management     | Using GitHub Issues or spreadsheets for bug tracking                         | Standardize defect logging format across group     |
| Test Design           | Applying Boundary Value Analysis, Equivalence Partitioning, Scenario Testing | Already practiced in HW#02 and HW#03; guidelines shared in Test Plan |

\newpage