# Introduction

## Document Overview

This document reports the results of testing activities for *The Toolshop* (Sprint 5 with Bugs). Testing was executed before **25-Aug-2025**, covering functional, GUI, API, automation, and performance aspects.

## Abbreviations and Glossary

- **SUT**: System Under Test
- **GUI**: Graphical User Interface
- **API**: Application Programming Interface
- **TC**: Test Case
- **BR**: Bug Report
- **OK**: Test passed
- **NOK**: Test failed
- **POK**: Partial OK (some steps failed)
- **NR**: Not Run
- **NC**: Not Completed

## References

- [R1] Test Plan – The Toolshop (Sprint 5 with Bugs), Version 1.0, 24-Aug-2025
- [R2] Assignment Description – CS423 CSC13003, HW#08
- [STD1] IEEE 829 Standard for Software Test Documentation

## Conventions
- Test decisions are limited to: **OK, NOK, POK, NR, NC**.
- Bugs are tracked in **GitHub Issues** with IDs (e.g., BUG-101).


# Overview of Test Results

## Tests Log

Testing was executed on a **localhost Docker environment** (Laravel backend, Angular frontend, MySQL DB).

## Overall Assessment

- **Functional coverage**: ~99% executed, 62% OK.
- **GUI testing**: Found layout/validation issues, 2 critical user flow bugs.
- **API testing**: 85% OK, 2 NOK for error handling in `/payment/check`.
- **Automation**: Selenium + Newman regression suites executed successfully.
- **Performance**: Stable up to 100 VUs, failures observed at 200 VUs (spike).

## Impact of Test Environment

Tests were limited by:

- Student laptops (hardware bottleneck in JMeter tests).
- Network variations affecting response time.
- Localhost environment only (no staging/production simulation).

# Detailed Test Results

## Summary Table

| Test ID    | Description                         | Requirement | Decision | Comments / Bug ID |
|------------|-------------------------------------|-------------|----------|-------------------|
| LOGIN-001  | Login with valid credentials        | REQ-001     | OK       | Works as expected |
| LOGIN-002  | Login with invalid password         | REQ-001     | OK       | Error message displayed |
| LOGIN-003  | Login with empty fields             | REQ-001     | NOK      | No validation shown (BUG-102) |
| CART-001   | Add item to cart                    | REQ-007     | OK       | Item added correctly |
| CART-003   | Remove item from cart               | REQ-008     | POK      | Item removed, but total not updated until refresh (BUG-110) |
| CHECKOUT-005 | Checkout with expired card        | REQ-010     | NOK      | Payment API crashed (BUG-123) |
| INVOICE-002 | Generate invoice after purchase    | REQ-015     | OK       | Invoice created but formatting minor (BUG-130) |
| ADMIN-007  | Export user list to CSV             | REQ-020     | NR       | Feature not implemented |
| PERF-010   | 8-hour endurance test               | REQ-030     | NC       | Aborted after 3 hours (hardware limit) |

## Examples

### OK Test

- **Test ID:** LOGIN-001
- **Description:** Login with valid credentials
- **Decision:** OK
- **Comments:** Successful login, session established

### NOK Test

- **Test ID:** CHECKOUT-005
- **Description:** Checkout with expired credit card
- **Decision:** NOK
- **Comments:** Payment API crashed – Bug BUG-123

### Partial OK Test

- **Test ID:** CART-003
- **Description:** Remove item from cart
- **Decision:** POK
- **Comments:** Item removed, total not updated until refresh (Bug BUG-110)

### Not Run Test

- **Test ID:** ADMIN-007
- **Description:** Export user list to CSV
- **Decision:** NR
- **Comments:** Not implemented in Sprint 5

### Not Completed Test

- **Test ID:** PERF-010
- **Description:** 8-hour endurance test
- **Decision:** NC
- **Comments:** Aborted due to laptop overheating after 3 hours