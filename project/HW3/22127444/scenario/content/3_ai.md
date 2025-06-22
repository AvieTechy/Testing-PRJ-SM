# Use of AI Tool

## Tool name

ChatGPT provided by OpenAI.

## Prompt used:

```plaintext
You are a professional software tester. Based on the feature description 
and the scenario table below, generate **detailed manual test cases** in 
QA-standard format and **output them in a format suitable for Excel.

Feature: [Feature name]

Basic Flow:
[Basic Flow]

Alternate Flows:
[Alternate Flows]

Scenario Table: 
[Scenario Table] 

For each test case, include the following columns:

* Test Case ID (e.g., TC01)
* Title
* Preconditions (if any)
* Inputs (Test Data)
* Test Steps
* Expected Result
* Actual Result (leave blank)
* Result (Pass/Fail – leave blank)

```

## AI-generated vs Manually Refined Test Cases

* **AI-generated test cases**:
  The AI tool generated **one basic test case per scenario**, focusing on the general validation logic. For example:

  * A single test case was created to cover all cases where First Name, Last Name, or Email were missing — grouped as one.
  * The AI also used generic descriptions such as “invalid slug” or “invalid file” without specifying the exact nature of the invalid input (e.g., containing special characters, uppercase letters, or empty value).
  * Each test case only addressed **a high-level violation** of the expected constraints and did not explore detailed boundary or alternate conditions.

* **Manually created & refined test cases**:
  I reviewed the AI-generated test cases and made the following manual improvements:

  * **Split generalized validations** into **separate, specific test cases**.
    For example:

    * I created distinct test cases for missing First Name, missing Last Name, and missing Email — instead of grouping them.
    * For the "invalid slug" case, I created different test cases for each invalid condition: containing spaces, uppercase letters, or being empty.
  * **Added test cases that were missing** in the AI results:

    * The valid/happy-path scenario where the form is correctly submitted.
    * Edge cases involving multiple simultaneous validation failures (e.g., invalid email + short message + no subject).
    * Backend/server-related failures and message feedback upon submission.

These manually created cases ensured broader test coverage, more accurate mapping to real-world behavior, and better alignment with scenario testing goals.


\pagebreak