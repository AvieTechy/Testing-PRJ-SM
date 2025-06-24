# Scenario Selection

## Methodology

The scenario selection process focused on identifying critical business flows that represent real-world user interactions with the system. Two key scenarios were selected based on their business impact and risk assessment:

1. **High-Risk User Management Scenario**: Profile update with password change
2. **Business-Critical Order Processing Scenario**: Complete order lifecycle management

## Selected Scenarios

### Scenario A: User Profile Management Crisis
**Business Context**: A user attempts to update their profile information and change their password in a single session, representing a common user workflow.

**Scenario Flow**:
1. User successfully logs into the system
2. User navigates to profile page and attempts to update personal information
3. User then attempts to change their password for security reasons
4. User expects to continue using the system with updated credentials

**Risk Assessment**: **CRITICAL** - Profile management is fundamental to user experience and system security.

### Scenario B: Order Lifecycle Management
**Business Context**: An administrator needs to process orders through their complete lifecycle, from initial fulfillment to completion, while handling exceptions.

**Scenario Flow**:
1. Administrator views all pending orders
2. Administrator processes a standard order through all status transitions
3. Administrator places a problematic order on hold for investigation
4. Administrator attempts to correct an incorrect status update
5. Administrator verifies completed orders are properly secured

**Risk Assessment**: **HIGH** - Order management directly impacts business revenue and customer satisfaction.

## Scenario Justification

These scenarios were selected because they:
- Cover end-to-end business processes
- Include both happy path and exception handling
- Test critical system integrations
- Represent high-frequency user activities
- Have direct business impact if they fail

The selection ensures comprehensive coverage of user management and business operations while focusing testing effort on the most critical system components.
