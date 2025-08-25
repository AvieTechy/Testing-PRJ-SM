# Test Approach

This section outlines the methodologies and techniques to be employed in testing *The Toolshop* application during the CSC13003 – Software Testing course. The approach is tailored to meet the learning outcomes and assignment requirements, ensuring comprehensive coverage of functional, performance, and quality aspects.

## Initial Test-Idea Catalogs and other reference sources

The initial test ideas are derived from the project description, the *Test Plan Template*, and the CS423 course guidelines. Additional reference sources include the [*Practice Software Testing* repository](https://github.com/testsmith-io/practice-software-testing/) and the Sprint 5 with known issues folder. These resources guide the identification of test scenarios and techniques.

## Testing Techniques and Types

### Data and Database Integrity Testing

| **Aspect**                | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Objective**             | Ensure data accuracy, consistency, and integrity across the database.           |
| **Techniques**            | Validate data input/output, check for duplicates, and verify referential integrity. |
| **Tools**                 | SQL queries, database management tools.                                        |
| **Focus Areas**           | User data, product catalog, order history, payment records.                    |

### Function Testing

| **Aspect**                | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Objective**             | Verify that individual functions (e.g., login, checkout) perform as expected.   |
| **Techniques**            | Black-box testing, equivalence partitioning, boundary value analysis.          |
| **Tools**                 | Manual testing, Selenium for automation.                                       |
| **Focus Areas**           | Authentication, cart management, payment processing, invoice generation.       |

### Business Cycle Testing

| **Aspect**                | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Objective**             | Validate end-to-end business processes (e.g., order-to-delivery).               |
| **Techniques**            | Scenario-based testing, workflow analysis.                                     |
| **Tools**                 | Postman for API workflows, manual validation.                                  |
| **Focus Areas**           | User registration to order completion, payment reconciliation.                 |

### User Interface Testing

| **Aspect**                | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Objective**             | Ensure the Angular UI is user-friendly, responsive, and visually consistent.    |
| **Techniques**            | GUI testing, cross-browser testing (Chrome, Firefox).                          |
| **Tools**                 | Selenium, manual inspection tools (e.g., browser developer tools).             |
| **Focus Areas**           | Navigation, input validation, layout consistency.                              |

### Performance Profiling

| **Aspect**                | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Objective**             | Assess the application's performance under normal conditions.                  |
| **Techniques**            | Benchmarking, response time measurement.                                       |
| **Tools**                 | JMeter, browser performance tools.                                            |
| **Focus Areas**           | Page load times, API response times, concurrent user actions.                  |

### Load Testing

| **Aspect**                | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Objective**             | Evaluate system behavior under expected user loads.                            |
| **Techniques**            | Simulated user load testing.                                                   |
| **Tools**                 | JMeter, LoadRunner.                                                            |
| **Focus Areas**           | Checkout process with 100 concurrent users, catalog browsing.                  |

### Stress Testing

| **Aspect**                | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Objective**             | Determine the system's breaking point under extreme conditions.                |
| **Techniques**            | Overload testing, failure injection.                                           |
| **Tools**                 | JMeter, custom scripts.                                                        |
| **Focus Areas**           | Server response under 500+ concurrent users, payment failures.                 |

### Volume Testing

| **Aspect**                | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Objective**             | Test system performance with large data volumes.                               |
| **Techniques**            | Data volume scaling, stress on database.                                       |
| **Tools**                 | JMeter, database load simulators.                                              |
| **Focus Areas**           | 10,000 product catalog, 1,000 simultaneous orders.                             |

### Security and Access Control Testing

| **Aspect**                | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Objective**             | Ensure secure access and protect against basic vulnerabilities.                |
| **Techniques**            | Role-based testing, basic SQLi/XSS checks.                                     |
| **Tools**                 | OWASP ZAP, manual security testing.                                            |
| **Focus Areas**           | User authentication, admin access, payment data protection.                    |

### Failover and Recovery Testing

| **Aspect**                | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Objective**             | Verify system recovery after failures (e.g., server crash).                    |
| **Techniques**            | Simulated outages, backup restoration.                                         |
| **Tools**                 | Custom failover scripts, server monitoring tools.                              |
| **Focus Areas**           | Database recovery, session persistence post-failure.                           |

### Configuration Testing

| **Aspect**                | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Objective**             | Test application behavior across different configurations.                     |
| **Techniques**            | Configuration variation testing.                                               |
| **Tools**                 | Virtual machines, configuration management tools.                              |
| **Focus Areas**           | Browser versions, OS compatibility (Windows, Linux).                           |

### Installation Testing

| **Aspect**                | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Objective**             | Ensure smooth installation and uninstallation of the application.              |
| **Techniques**            | Installation validation, rollback testing.                                     |
| **Tools**                 | Installer logs, manual verification.                                           |
| **Focus Areas**           | Web server setup, dependency installation (e.g., Laravel, Angular).            |

\newpage