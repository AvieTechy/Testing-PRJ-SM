# AI-Powered Software Testing Tools

## Tool Descriptions

### [BrowserStack Test Management](https://www.browserstack.com/test-management)

**Provider:** BrowserStack

BrowserStack offers a cloud-based test management suite with an integrated AI-powered test case generator. It was selected for this evaluation due to its robust NLP capabilities, CI/CD integration, and enterprise-grade test analytics.

**Main features:**

- **Natural language processing (NLP)**: Translates plain-English feature descriptions into comprehensive test cases.
- **Cross-browser testing**: Enables tests across 3000+ devices and browsers.
- **Testoptimization**: Suggests critical path coverage and reduces redundant tests.
- **Analytics**: Provides AI-based reports and test insights.

**AI capabilities:**

- Automatically detects gaps in coverage.
- Suggests relevant test scenarios based on product requirements.

### [TestingTools.AI](https://www.testingtools.ai/)

**Provider:** Independent platform

This lightweight tool converts user stories into detailed test cases and is ideal for Agile teams that prioritize manual testing. It was chosen for its simplicity, export versatility, and prompt-style input.

**Main features:**

- **Plain english input**: Converts user stories or requirements into test cases.
- **Export options**: CSV, Excel, Markdown, PDF.
- **Templates**: Offers functional, edge case, and regression templates.
- **Immediate output**: No login or setup required.

**AI capabilities:**

- AI parses user input and outputs full test cases (steps + expected result).
- Edge case suggestions based on common QA scenarios.

### [AITestCaseGenerator (Jira Plugin)](https://www.aitestcasegenerator.com/)

**Provider:** Embedded within Jira ecosystem

Integrated with Jira, this tool enables seamless AI-driven test case generation for existing issues. Selected for its native workflow support and traceability.

**Main features:**

- **Jira native**: Works inside Jira tickets (Stories, Tasks, Bugs).
- **OpenAI-Powered**: Utilizes GPT to generate precise test cases.
- **Editable outputs**: Allows QA to refine results before saving.
- **Traceability matrix**: Maps test cases back to their requirements.

**AI capabilities:**

- Context-aware suggestions inside Jira.
- Prompt-less generation based on Jira issue context.

## Test case generation process

**Note:** BrowserStack uses a **prompt-based** approach while TestingTools.AI and AITestCaseGenerator require structured **title + description** inputs.

### Feature 1: User Sign In (Role: User)

**User Story:**
*As a user, I want to sign in with my email and password so I can access my personal dashboard.*

**Prompt Used (for BrowserStack):**
"Generate a detailed test suite for the 'User Sign In' feature of a web application. Include positive and negative test cases. Cover valid login, invalid credentials, empty fields, SQL injection, and edge cases."

1. BrowserStack

- Pasted prompt into feature description.
- AI generated **35 test cases**.
- **Coverage:** Valid login, input validation, SQL injection, load testing, and cross-platform compatibility.

![Exported from BrowserStack](brow_1.png){width=450px}

2. TestingTools.AI

- Title: "User Sign In"
- Description: Full user story + constraints (e.g., min 6-char password, email format)
- Generated **10 test cases**.
- **Coverage:** Valid login, invalid credentials, empty fields, and email format. However, it’s missing non-functional tests like SQL injection, performance, and usability, which were covered by BrowserStack’s AI.

\pagebreak

![Exported from TestingTools.AI](tool_1.png){width=450px}

3. AITestCaseGenerator

- Jira issue created → clicked "Generate Test Cases"
- **5 test cases** generated.
- Cover basic login flows: valid, invalid, and empty fields. Missing coverage for security, performance, and edge cases like SQL injection.

![Exported from AITestCaseGenerator](jira_1.png){width=450px}

### Feature 2: User Management (Role: Admin)

**User Story:**
*As an admin, I want to create, view, update, and delete users to manage access control.*

**Prompt Used (BrowserStack):**
"Generate CRUD test cases for admin role. Include valid inputs, invalid inputs, duplication handling, role restrictions, and delete confirmations."

1. BrowserStack:

- Resulted in **33 test cases** across 8 scenarios.
- **Coverage:** Coverage includes create, read, update, delete (CRUD) flows with both valid and invalid inputs, duplicate handling, deletion confirmation, and role-based permission boundaries — offering strong validation, security, and access control testing.

![Exported from BrowserStack](brow_2.png){width=450px}

2. TestingTools.AI:

- Title: "User Management (Admin)"
- Description: Detailed CRUD description + validation rules.
- **12 test cases** exported.
- Included user creation well, including valid/invalid inputs and duplicate checks. However, it lacks update, delete, role permission, and audit log test cases.

![Exported from TestingTools.AI](tool_2.png){width=450px}

3. AITestCaseGenerator:

- Jira ticket with CRUD admin story.
- AI returned **8 test cases** cover core CRUD flows with valid/invalid inputs and existing/non-existing users. Missing role-based access control and audit logging.

![Exported from AITestCaseGenerator](jira_2.png){width=450px}

### Feature 3: Filter and Search (Role: Guest)

**User Story:** As a guest (unauthenticated) user, I should be able to:
- Use a search bar to input keywords related to item names or descriptions.
- Apply filter options such as category, price range, rating, and availability.
- Combine multiple filters to narrow down results.
- See real-time updates of the search results without full page reload.
- Receive feedback if no results match the criteria.
- Perform these actions on both desktop and mobile interfaces.

**Prompt (BrowserStack):**
"Test cases for filtering and searching items: include keyword search, category filter, empty results, and combination of filters."

1. BrowserStack:

- **37 test cases** generated.
- The test coverage is comprehensive, including keyword and category filters, combined filter logic, empty results handling, performance under load, resource usage, security validation, usability, accessibility, and cross-platform consistency.

![Exported from BrowserStack](brow_3.png){width=450px}

2. TestingTools.AI:

- Title: "Filter & Search"
- Description: Included search by name/category, no login required.
- **13 test cases**, covers basic search and single-filter use cases well for guests. However, it lacks tests for combined filters, mobile responsiveness, and edge cases like special characters.

![Exported from TestingTools.AI](tool_3.png){width=450px}

3. AITestCaseGenerator:

- **10 test cases** generated covering full filter & search flow, including keyword, all filter types, combined filters, responsiveness, and platform behavior.

![Exported from AITestCaseGenerator](jira_3.png){width=450px}

## Coverage summary


| Feature               | Tool                | TC | Coverage Summary                                                                 |
|-----------------------|------------------------------|:---------------------:|----------------------------------------------------------------------------------|
| **User Sign In**      | **BrowserStack**     | 35           | Excellent coverage: valid/invalid input, empty fields, SQL injection, performance, cross-platform |
|                       | **TestingTools.AI**  | 10           | Covers functional flows (valid/invalid login, empty fields), lacks security & performance |
|                       | **AITestCaseGen**    | 5            | Covers basic login flows; missing advanced and non-functional tests              |
| **User Management**   | **BrowserStack**     | 33           | Strong CRUD coverage including duplicates, validation, delete confirm, role boundaries |
|                       | **TestingTools.AI**  | 15           | Focused on user creation; lacks update/delete, role permissions, and audit log   |
|                       | **AITestCaseGen**    | 8            | Covers CRUD basics; lacks access control and logging scenarios                   |
| **Filter & Search**   | **BrowserStack**     | 37           | Comprehensive: filters, combined filters, performance, UX, accessibility         |
|                       | **TestingTools.AI**  | 13           | Good for single-filter search; missing combined filters and mobile UX            |
|                       | **AITestCaseGen**    | 10           | Well-balanced coverage: keyword, all filters, UI responsiveness                  |

## Conclusion and analysis

Each tool demonstrates distinct strengths suited to different QA needs:

- **BrowserStack** offers the most comprehensive coverage across all three features. Its prompt-based AI is capable of generating functional, non-functional, and UI-focused test cases with minimal setup. Ideal for teams looking for depth and automation readiness.
- **TestingTools.AI** is best for fast, manual test generation. It provides detailed, exportable test cases from structured user stories, but lacks advanced scenarios like performance or security testing.
- **AITestCaseGenerator** integrates seamlessly with Jira workflows. While it produces fewer test cases, its strength lies in traceability and ease of collaboration within existing Agile pipelines.

## Issues encountered

### BrowserStack

- Steps and expected results were not viewable until test cases were saved to the repository.
- Occasionally slow when generating large test suites (35+ cases).
- No direct export to CSV without saving and navigating to the repository.

### TestingTools.AI

- No login required, but interface lacks customization for test ID formatting or grouping.
- Edge cases (e.g., mobile responsiveness, special characters) not always suggested unless explicitly stated in the description.
- Limited support for non-functional test categories (e.g., performance, security).

### AITestCaseGenerator (Jira Plugin)

- Generated fewer test cases (around 10) unless description was very detailed.
- Lacked depth in advanced scenarios like audit logs or cross-platform testing.
- Requires a Jira environment with plugin access – not ideal for standalone use.
