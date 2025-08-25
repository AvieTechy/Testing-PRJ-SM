# Entry and Exit Criteria

This section defines the conditions for initiating and concluding the testing phases of *The Toolshop* application. These criteria ensure that testing aligns with the project timeline and quality standards, reflecting the group assignment requirements.

## Test Plan

### Test Plan Entry Criteria

| **Criteria**                | **Description**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|
| **Test Environment Ready**  | Test platform (e.g., local setup with Chrome/Firefox) is fully configured and accessible. |
| **Requirements Defined**    | All functional and non-functional requirements from the Sprint 5 description are documented. |
| **Test Cases Prepared**     | Test cases for HW#02 to HW#07 (Domain, GUI, Automation, Performance, API) are drafted and reviewed. |
| **Team Coordination**       | Task distribution among group members is agreed upon and documented for HW#08.  |

### Test Plan Exit Criteria

| **Criteria**                | **Description**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|
| **Test Coverage Achieved**  | Minimum 90% coverage of identified test cases across all testing types.         |
| **Defects Resolved**        | Critical and major bugs (as per bug reports) are addressed or documented for deferral. |
| **Documentation Complete**  | Final report (HW#08) including Test Plan, Test Cases, Bug Reports, and Test Report is submitted. |
| **Approval Received**       | Review and approval from lecturers/TAs (Dr. Lam Quang Vu et al.) via Moodle.    |

### Suspension and Resumption Criteria

| **Criteria**                | **Description**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|
| **Suspension**              | Testing halts if critical system failures (e.g., server downtime) exceed 48 hours or if 50% of test cases fail repeatedly. |
| **Resumption**              | Resumes once the environment is restored, and a root cause analysis is documented, approved by the TA. |


## Test Cycles

### Test Cycle Entry Criteria

| **Criteria**                | **Description**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|
| **Build Availability**      | The Sprint 5 with known issues build is available in the repository[](https://github.com/testsmith-io/practice-software-testing/). |
| **Environment Setup**       | Test environment (e.g., Chrome/Firefox browsers, local server) is configured and validated by 11:04 AM +07, August 25, 2025. |
| **Test Cases Ready**        | Test cases for the current cycle (e.g., HW#02 Domain Testing) are reviewed and approved by the group and TAs. |
| **Resource Allocation**     | All team members (as per group assignment) are assigned tasks, and tools (e.g., Selenium, JMeter) are accessible. |

### Test Cycle Exit Criteria

| **Criteria**                | **Description**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|
| **Test Completion**         | All test cases for the cycle (e.g., HW#02) are executed, with results documented by the cycle deadline. |
| **Defect Reporting**        | All identified bugs are logged with severity/priority levels and reproduction steps in the HW#08 Bug Reports. |
| **Coverage Achieved**       | Minimum 85% test coverage for the cycle’s focus area (e.g., domain testing) is met. |
| **TA Review**               | Preliminary results are submitted to TAs (e.g., Dr. Lam Quang Vu) for feedback before cycle closure. |

### Test Cycle Abnormal Termination

| **Criteria**                | **Description**                                                                 |
|-----------------------------|---------------------------------------------------------------------------------|
| **Critical Failure**        | Testing is suspended if a critical system failure (e.g., server crash) persists for over 24 hours. |
| **Significant Defects**     | Cycle ends prematurely if 60% of test cases fail with major defects, requiring a build alteration. |
| **Resource Unavailability** | Termination occurs if key tools (e.g., JMeter) or team members are unavailable for 48+ hours. |
| **Build Alteration**        | The intended build candidate is altered if new bugs render the current version untestable, pending TA approval. |


\newpage