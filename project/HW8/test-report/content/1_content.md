# Objectives of the Report

This report consolidates the results of testing activities for *The Toolshop* (Sprint 5 with Bugs). The objectives are:

- Verify that implemented features meet the specified requirements.
- Identify, document, and classify defects based on severity and module.
- Measure the effectiveness of the testing effort using defined metrics.
- Provide insights, lessons, and recommendations for future development and testing.

# Application Overview

## General Description

*The Toolshop* is a training-oriented e-commerce application with intentionally seeded bugs in Sprint 5. It enables users to register, log in, browse products, manage shopping carts, perform checkout, process payments, and generate invoices. This sprint focused on enhancing payment processing and invoice generation, with known defects introduced for learning purposes.

## Technologies Used

| Component | Technology |
| --- | ----- |
| Frontend | Angular 16.2.0 |
| Backend | Laravel 10.0 (PHP 8.1) |
| Database | MySQL 8.0.28 |
| Deployment | Docker 20.10.17 (local) |

## Main Modules

- User authentication and management
- Product catalog browsing and details
- Shopping cart operations
- Checkout and payment
- Invoice generation
- Admin module (user management, export/report features)

# Test Scope

## In Scope

- User login/logout functionality
- Cart operations (add, update, remove items)
- Checkout and payment workflows (including error scenarios)
- Invoice generation after successful checkout
- Core APIs: `/users/login`, `/users`, `/payment/check`, `/invoices`,...
- GUI validation: input fields, form submissions, error messages
- Load and spike performance testing using JMeter (50–200 users)

## Out of Scope

- Advanced penetration testing (e.g., SQL injection, XSS beyond basic payloads)
- Mobile device/responsive compatibility testing
- Third-party live payment gateway integration (simulated payment only)
- Localization (English only tested)

## Not Tested

- Admin module “export CSV” feature (not implemented in Sprint 5)
- Endurance test (8-hour simulation), aborted after 3 hours due to hardware limitations

# Types of Testing Performed

## Functional Testing

- Verified login (TC-001), cart add/remove (TC-005), checkout (TC-010), and invoice generation (TC-015).
- Example: TC-010 (Checkout with valid payment) passed; TC-011 (Checkout with expired card) failed due to API crash.

## GUI Testing

- Checked layout consistency, form validation, and error messages across login, cart, and checkout pages.
- Example: TC-020 (Validate checkout form) identified layout glitch on mobile view (Bug #130).

## API Testing

- Used Postman/Newman to test `/users/login`, `/users`, `/payment/check`, and `/invoices`.
- Example: TC-030 (POST /payment/check with invalid token) returned 500 error (Bug #124).

## Automation Testing

- Selenium WebDriver scripts for login (TC-040) and checkout (TC-041); Newman collection run in GitHub Actions CI.
- Example: TC-041 passed with 100% script coverage.

## Performance Testing

- JMeter load tests with 50–100 users (stable); spike test with 200 users showed 500 errors.
- Example: TC-050 (200-user spike) failed after 5 minutes.

# Test Environment and Tools

## Test Environment

| Environment Component | Details |
| --- | ------- |
| Deployment | Docker Compose (Laravel + MySQL) |
| Client machines | Windows 10/11 (4–8 GB RAM), Ubuntu 20.04 |
| Network | Wi-Fi 50 Mbps+ (shared) |
| Browsers | Chrome 126, Firefox 128, Edge 126 |

## Tools Used

| Tool | Purpose |
| --- | ------- |
| Postman/Newman | API functional and regression testing |
| Selenium | GUI automation testing |
| JMeter | Load, stress, spike performance testing |
| GitHub Actions | CI/CD automation |
| Google Sheets | Test case and defect tracking |

# Lessons Learned

- Early seed data preparation prevented delays in checkout testing.
- Consistent bug logging (ID, severity, steps) improved defect tracking efficiency.
- Hardware constraints limited performance testing; stronger machines are required.
- Automation reduced regression testing time by 40% near the deadline.

# Recommendations

- Resolve critical checkout and payment bugs before Sprint 6.
- Test Admin module functions (CSV export, role management) in future sprints.
- Enhance validation rules to minimize user errors.
- Upgrade to dedicated servers or better hardware for reliable performance testing.

# Exit Criteria

- At least 90% of test cases executed (achieved 99%).
- All Critical bugs identified and logged.
- Regression cycle completed after major fixes (100% coverage).
- Test Report prepared and submitted by August 25, 2025.

# Conclusion

Testing for *The Toolshop (Sprint 5 with Bugs)* was completed on **25-Aug-2025** with execution coverage of 98% and 18 defects logged.

**Strengths**

- Broad coverage of functional and API testing.
- High-value defect detection in checkout/payment workflows.
- Automation and CI integration improved efficiency.

**Weaknesses**

- Critical payment-related defects remain unresolved.
- Admin module incomplete and minimally tested.
- Performance testing limited by local hardware capacity.

Overall, the application meets most core requirements but cannot be considered production-ready due to unresolved checkout and payment issues. This report will serve as the foundation for defect resolution and improved testing practices in Sprint 6 and beyond.