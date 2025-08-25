# Risks, Dependencies, Assumptions, and Constraints

## Risks

| Risk | Mitigation Strategy | Contingency (Risk is realized) |
|------|----------------------|--------------------------------|
| Sprint 5 build is unstable or inaccessible | Maintain a backup Docker image and pin a stable commit; run smoke test after each pull | Revert to stable build; run only critical smoke/regression tests; document untested areas |
| Test data is inadequate or inconsistent | Prepare seed scripts with product and user data; verify DB before execution | Redefine test data; refresh database; rerun impacted test cases |
| Submission deadline (25-Aug-2025, 11:09 AM +07) is too strict | Prioritize high-risk features (login, checkout, payment); parallelize team effort | Deliver partial coverage with explanation of gaps; include “not tested” list |
| Tool misconfiguration (Selenium, JMeter, Newman, Docker) | Share setup guide; validate environments in advance | Fall back to manual execution or alternative machines; attach raw logs/screenshots |
| Limited hardware resources (student laptops) | Use lightweight browsers; stagger JMeter runs with fewer users | Scale down load tests; report relative performance trends instead of absolute metrics |

## Dependencies

| Dependency | Potential Impact | Owners |
|------------|------------------|--------|
| Availability of Sprint 5 build on GitHub | Without build, no functional or regression tests can run | Development team / QA setup |
| Seeded database with test data | Test cases for checkout and invoices cannot execute without sample data | Test System Admin |
| Access to required tools (Postman, JMeter, Selenium, Docker) | Missing or misconfigured tools block test execution | Each assigned tester |
| Moodle submission portal availability | Final deliverables cannot be submitted | Course staff |

## Assumptions

| Assumption | Impact if incorrect | Owners |
|------------|----------------------|--------|
| The Toolshop application remains stable during testing | Test results may be invalid; retesting required | QA Team |
| All testers have required tools installed and configured | Setup delays, reduced test coverage | Each tester |
| Localhost (Docker) environment is representative of production | Performance results may not match real-world behavior | QA Team |
| Deliverables in Markdown/PDF are acceptable for submission | Reformatting may be required at the last minute | QA Team Lead |

## Constraints

| Constraint | Impact on Test Effort | Owners |
|------------|------------------------|--------|
| Strict deadline of 25-Aug-2025, 11:09 AM (+07) | Limited time for multiple test cycles; forces risk-based testing | Entire QA Team |
| Environment limited to localhost (no staging/production) | Cannot validate in production-like conditions | QA Team |
| Hardware constraints (student laptops, not servers) | Performance test results approximate only | QA Team |
| Group project workload sharing | Requires close coordination; delays by one member impact all | Entire QA Team |

\newpage