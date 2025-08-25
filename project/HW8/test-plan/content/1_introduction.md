# Introduction

## Purpose

The purpose of this Test Plan is to define the strategy and scope of testing The Toolshop application (Sprint 5 with known issues). It ensures a structured approach to verifying functionality, performance, and quality, aligning with the requirements of the **CSC13003 – Software Testing course**.

**Key objectives:**

- Verify that core e-commerce workflows (browse, add to cart, checkout, payment, invoice) function correctly.
- Validate backend APIs for correctness, error handling, and robustness.
- Evaluate GUI usability and adherence to validation rules.
- Identify and document defects with severity and priority levels.
- Provide measurable insights on quality risks and coverage.
- Deliver professional test documentation as required by CS423 course outcomes.

## Scope

**In-Scope**

- Functional testing of authentication (sign-up, sign-in), catalog browsing, cart management, order processing, and payment workflows.
- GUI validation (input forms, navigation menus, layout consistency, responsiveness on supported browsers like Chrome and Firefox).
- API testing (`/users/login`, `/payment/check`, `/invoices`) to ensure data integrity and API contract compliance.
- Automation testing (Selenium for UI, Postman/Newman for API) to enhance efficiency and repeatability.
- Performance testing (load, stress, spike) with JMeter to assess scalability and stability.
- Bug reporting, regression testing after fixes, and a final quality assessment report.

**Out of Scope**

- Security penetration testing beyond basic SQL injection and XSS validation checks.
- Localization testing (focused on English only, no multi-language support testing).
- Mobile application or native app testing (web-based application only).
- Production deployment testing (no live server or CI/CD pipeline validation).

## Intended Audience

- QA Team (students responsible for execution and documentation)
- Lecturers/TAs (evaluators and mentors)
- Developers (recipients of bug reports and test insights)

## Document Terminology and Acronyms

- SUT: System Under Test (The Toolshop)
- GUI: Graphical User Interface
- API: Application Programming Interface
- JMX: JMeter test script
- CI/CD: Continuous Integration / Deployment

## References

- Project Repo: [Practice Software Testing – Sprint5-with-bugs](https://github.com/testsmith-io/practice-software-testing/)
- CS423 – CSC13003 assignment description

## Document Structure

This Test Plan follows the Rational Unified Process structure: defining mission, scope, approach, deliverables, workflow, and risks.

\newpage
