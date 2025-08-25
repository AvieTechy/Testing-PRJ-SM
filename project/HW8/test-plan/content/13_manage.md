# Management Process and Procedures

## Measuring and Assessing the Extent of Testing

The extent of testing for *The Toolshop* will be measured by:

- Percentage of test cases executed vs. planned (target ≥ 85%).
- Pass/Fail ratio across functional, GUI, API, automation, and performance tests.
- Defect density (number of defects per module or per 100 test cases).
- Performance KPIs such as average response time and error rate from JMeter runs.

Assessment will occur at the end of each test cycle and be consolidated into the Final Test Report.

## Assessing the Deliverables of this Test Plan

Deliverables (Test Plan, Test Cases, Test Case Summary, Bug Reports, Test Report) will be assessed based on:

- Completeness: coverage of all required testing types (HW#02–HW#07).
- Accuracy: consistency between test results and documented defects.
- Quality: clarity, structure, and compliance with course requirements.
- Timeliness: submitted before the official deadline (25-Aug-2025, 11:09 AM +07).

Peer review within the team and final review by the Test Manager will ensure quality before submission.

## Problem Reporting, Escalation, and Issue Resolution

- **Reporting**: All defects will be logged in GitHub Issues or a shared spreadsheet with severity (Critical, Major, Minor), status, and reproduction steps.
- **Escalation**: Blocker issues (e.g., build inaccessible, database crash) will be escalated immediately to the Test Manager.
- **Resolution**: Developers or environment owners will address issues; QA team retests to confirm closure.  
- All escalated items will be documented in the Incident Log.

## Managing Test Cycles

- Each cycle (manual, API, automation, performance) will start only after entry criteria are met (stable build, seeded DB).
- At the end of each cycle, the QA team will:
  - Summarize executed cases, defects, and coverage.
  - Conduct a bug triage session to prioritize fixes.
  - Decide whether to continue, repeat, or terminate the cycle.
- Regression cycle will run before final submission using smoke and automated tests.

## Traceability Strategies

Traceability will be ensured by:

- Linking requirements (from assignment description) → Test Cases → Bugs.
- Maintaining a Traceability Matrix in Excel or Google Sheets.
- Using unique IDs (e.g., LOGIN-001 for test cases, BUG-001 for defects) to enable cross-referencing.
- Ensuring all high-priority requirements (login, checkout, payment) are covered by at least one test case.

## Approval and Signoff

- Draft deliverables will be peer-reviewed within the QA team.
- The Test Manager (QA Team Lead) will provide internal signoff before submission.
- Final approval lies with the course instructor and TAs upon grading.
- Once signed off, the Test Plan and supporting deliverables will be considered baseline for HW#08 submission.

\newpage