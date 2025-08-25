# Outline of Planned Tests

## Test Inclusions

This section details the core testing activities that will be conducted as part of the project. These tests align with the learning outcomes specified in the course, focusing on various testing types such as domain testing, scenario-based testing, GUI testing, automation testing, performance testing, and API testing. The tests will be applied to key features of **"The Toolshop"** application (from the `/sprint5-with-bugs` folder in the repository), ensuring comprehensive coverage of functional and non-functional aspects.

**Functional Testing:** This will cover essential user workflows and business logic to verify that the application behaves as expected under normal conditions. Specific areas include:

- **Authentication:**
  - **Sign Up:** Verifying new user registration, including form validation, email uniqueness checks, password requirements, and successful account creation.
  - **Sign In:** Testing login with valid/invalid credentials, session establishment, role-based access, and logout functionality.
- **Profile Management:** Ensuring users can update personal details (e.g., name, address, email) and change passwords, with validation for old/new password matching and strength checks.
- **Product Browsing and Catalog:**
  - **Catalog:** Checking product listing, search functionality, filtering by attributes (e.g., price, brand), pagination, and detailed product views.
  - **Categories:** Verifying category navigation, sub-categories, product assignment to categories, and dynamic updates.
- **Shopping Cart and Checkout:**
  - **Cart Management:** Testing adding/removing/updating items, quantity adjustments, persistence across sessions, and total calculations including discounts or taxes.
  - **Checkout:** Validating the end-to-end order placement process, including shipping details, payment simulation, invoice generation, order confirmation, and handling of incomplete checkouts.
- **Contact:** Ensuring submission of inquiries, validation of input fields (e.g., email, message), and confirmation of receipt (e.g., via email or on-screen message).
- **Admin Features:**
  - **Category Management:** Testing creation, editing, deletion of categories, assignment of products, and hierarchy management for admins.
  - **User Management:** Verifying admin abilities to view, edit, delete user accounts, manage roles, and handle user-related data.
  - **Order Management:** Checking order viewing, status updates (e.g., processing, shipped, canceled), refund processing, and integration with invoices.

**GUI Testing:** Focused on the user interface to ensure usability, consistency, and responsiveness. Key elements to test:

- **Navigation:** Checking menu structures, links, breadcrumbs, and page transitions for intuitive flow and absence of dead ends across all pages, including admin dashboards.
- **Input validation:** Testing form fields for proper error messages, data type enforcement (e.g., email formats, numeric limits), and prevention of invalid submissions in features like sign up, profile updates, and contact forms.

**API Testing:** Targeting backend endpoints to validate data exchange, security, and reliability. Specific APIs under test:

- `/users/login`: Verifying authentication responses, token generation, and handling of edge cases like expired sessions or invalid credentials.
- `/payment/check`: Ensuring payment status checks, validation of transaction details, and integration with simulated payment gateways.
- `/invoices`: Testing invoice retrieval, generation, and formatting, including error scenarios for invalid invoice IDs.

**Automation Testing:** Implementing scripted tests for repeatability and efficiency. Tools and scopes:

- **Selenium for UI automation:** Automating browser interactions for end-to-end scenarios like login-to-checkout flows, including cross-browser testing on Chrome and Firefox.
- **Newman for API automation:** Running Postman collections to automate API calls, assertions on response codes, payloads, and performance metrics.

**Performance Testing:** Assessing the application's scalability and stability under varying loads. Using JMeter for:

- **Load testing:** Simulating multiple concurrent users to measure response times and throughput during peak usage, such as simultaneous checkouts or catalog browsing.
- **Spike testing:** Evaluating system behavior under sudden traffic surges, such as rapid increases in checkout requests or admin order updates.
- **Stress testing:** Pushing the application beyond normal limits to identify breaking points, resource leaks, and recovery mechanisms.

## Other Candidates for Potential Inclusion

These are additional testing areas that may be incorporated if time and resources permit, or if initial testing reveals related issues. They extend beyond the core requirements but could enhance overall quality:

- **Cross-browser Testing:** Extending GUI and functional tests to less common browsers like Safari, Chrome and Firefox to ensure compatibility, focusing on rendering differences, JavaScript execution, and CSS inconsistencies.
- **Accessibility Validation:** Using tools like WAVE or axe to check compliance with WCAG standards, including screen reader compatibility, keyboard navigation, color contrast, and alt text for images.

## Test Exclusions

To maintain focus on the project's scope and deadlines, the following areas will not be tested. These exclusions are based on the assignment guidelines, which emphasize specific testing types without requiring advanced security or platform-specific validations:

- **Security Penetration Testing:** No in-depth vulnerability scanning, ethical hacking, or tests for SQL injection, XSS, or other exploits, as this falls outside the course's core testing types.
- **Mobile App Testing:** The application is web-based; no testing on mobile devices, responsive designs beyond basic GUI checks, or native app features.
- **Production Deployment Testing:** No verification of live server configurations, CI/CD pipelines, or real-world hosting environments, as the focus is on the development sprint with known bugs.

\newpage