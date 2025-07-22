# Group Information

Group ID: 07

| Member Name        | Student ID | Assigned Tables          | Status      |
|:-------------------------|:-----------|:---------------------------|:------|
| Cao Uyển Nhi       | 22127310   | Registration Page                  | Done |
| Lưu Thanh Thuý     | 22127410   | Checkout Page               | Done |
| Nguyễn Phước Minh Trí      | 22127424   | Category Page                | Done |
| Võ Lê Việt Tú      | 22127435   | Home Page              | Done |
| Trần Thị Cát Tường | 22127444   | Category Management Page                 | Done |

# Introduction

This report documents the use of a generative AI tool to assist in the GUI testing of the E-commerce Homepage / Product Listing Page. The primary objective was to leverage AI to analyze a static screenshot of the user interface, identify potential UI/UX issues, and validate these findings against a manually created testing checklist. This process aims to demonstrate a hybrid approach to quality assurance, combining structured manual testing with AI-driven visual evaluation.

# Tool & Prompt Details

- **Tool Used:** Gemini (Gemini 2.5 Pro model) by Google AI Studio.

- **Prompt Submitted:**

*'I’m conducting GUI testing for the homepage of a web application and would like your assistance with two tasks. First, please review and improve my existing GUI checklist by suggesting any missing elements or refinements based on usability principles, accessibility standards, and UI/UX best practices. Second, using the provided screenshot of the homepage and the (revised) checklist, examine the interface to identify any GUI-related issues such as layout misalignment, unclear or missing labels, inconsistent placeholder text, poor visual hierarchy, or accessibility problems like low color contrast, improper tab order, or missing alt text. Please clearly distinguish between the issues identified from my original checklist and those detected through your independent analysis, and include actionable suggestions for improvement where relevant.'*

- Input image:

![Screenshot of feature](./content/img/1.png){height=600px}

\pagebreak

# AI-Generated Issues and Observations

Based on an analysis of the provided screenshot and checklist, the following UI/UX issues were identified by the AI:

| Category | Issue Identified | AI-Generated Notes |
|:---------|:-----------------|:-------------------|
| Labeling & Typos | Spelling errors in key UI elements. | The terms "Sorth" and "Serch" are incorrect. They should be "Sort" and "Search". This damages credibility. |
| Navigation | Broken image for the website logo. | The logo in the header fails to load, negatively impacting brand identity and trust. |
| Navigation | Error message displayed as a menu item. | The text "User Data not found" in the navigation bar appears to be a back-end error, which is unprofessional and confusing for users. |
| Navigation | Inconsistent language in the navigation menu. | The menu uses English ("Home," "Categories") but includes German ("Kontakt"), which breaks language consistency. |
| Layout & Alignment | Inconsistent layout for "Out of stock" items. | The price for the "Out of stock" product is pushed to the right, breaking the vertical alignment of prices in the product grid. |
| Visual Consistency | Inconsistent product photography style. | Most product images have a clean, consistent background, but the "Thor Hammer" image is a stylistic outdoor shot, creating a visual disconnect. |
| Functionality | Broken "Home" link. | Confirmed from user checklist: The "Home" link in the header navigates to the wrong page (/contact), a critical navigational flaw. |
| Functionality | Incorrect sorting logic. | Confirmed from user checklist: The sorting functionality is inverted (e.g., High-to-Low sort shows Low-to-High), which is a severe functional bug. |

\pagebreak

# Validation & Refinement of AI Results

To ensure the reliability of the AI-generated findings, each issue was cross-validated against the manually created checklist and through direct visual inspection of the screenshot.

## Checklist Mapping and Validation

The AI's findings were directly mapped to the original checklist to confirm their validity:

  - **Spelling Errors ("Sorth," "Serch"):** This validates Checklist item #2.2.4, which notes that there are spelling errors in titles.
  - **Broken Logo:** This validates Checklist item #1.3.5, where the "Remarks" column states there is an image display error.
  - **Broken "Home" Link:** This validates Checklist item #1.1.1, which explicitly states that the "Home" link leads to the wrong destination.
  - **Incorrect Sorting Logic:** This validates Checklist item #1.3.13, which describes the inverted sorting behavior in detail.

## Manual Verification

The following issues, suggested by the AI, were manually verified by inspecting the screenshot:

  - **Error Message in Navigation:** The "User Data not found" text is clearly visible in the header, confirming a critical issue.
  - **Layout Misalignment:** The price on the "Out of stock" item is visibly misaligned compared to the other product cards in the grid.
  - **Language Inconsistency:** The term "Kontakt" is visibly present in the header, confirming the mix of English and German.

## Limitations of AI Analysis

The AI's analysis was limited by its reliance on a single, static screenshot. It could not:

  - Verify dynamic behaviors like hover states, dropdown menu functionality, or the responsiveness of the price range slider.
  - Confirm the destination of all links without the user's notes (e.g., the "Home" link issue).
  - Assess the website's performance or compatibility across different browsers (Checklist section 3.1).

# Test Case Sources: Manual vs. AI-Generated

This evaluation combined a manually created checklist with AI-driven analysis to provide comprehensive coverage.

## Manually Created Test Cases

The foundation of this test was the manually created GUI checklist. This checklist was developed prior to the AI analysis and included specific checkpoints that required functional knowledge of the application. The key issues identified solely through this manual checklist were:

  - **Functional Logic Flaws** (Checklist Item 1.3.13): The most severe issue identified was the inverted sorting logic. The checklist documents that sorting by "Price (High - Low)" incorrectly displays products from low to high, and vice versa. This is a critical functional bug that directly hinders the user's ability to find products and can only be discovered by performing the action and comparing the result against the expected outcome. An AI cannot infer this logical error from a single screenshot.
  - **Navigational Integrity** (Checklist Item 1.1.1): The manual test plan involved checking every primary navigation link. This led to the discovery that the "Home" link incorrectly redirects to the /contact page. This finding required understanding the intended site architecture and verifying the behavior of a specific user action, which is a core part of manual, exploratory testing.
  - **Detailed Usability Nuances** (Checklist Item 1.2.7): The manual checklist captured subtle but important usability issues. For instance, the remark for item 1.2.7 notes that the hover-state color change on navigation links is not distinct enough, making it difficult for users to receive clear visual feedback. This is a heuristic evaluation that assesses the quality of the user interaction, a dimension beyond simple visual correctness.
  - **Investigating Workarounds** (Checklist Item 1.1.2): The manual evaluation went beyond just finding bugs. After identifying the broken "Home" link, the checklist notes that the homepage is still accessible via the logo in the navbar. This demonstrates a deeper level of testing, where the tester not only finds a problem but also investigates its impact and potential workarounds for the user, providing a more complete picture of the application's state.

## AI-Generated Findings

While the AI confirmed many manual findings, it also identified several issues that were not explicitly noted in the checklist's "Remarks" column. These represent the value-add of the AI's visual analysis:

  - **Error Message as UI Element:** The AI flagged "User Data not found" in the navigation as a critical issue. While a human tester would spot this, the AI immediately categorized it as a high-priority defect.
  - **Language Inconsistency:** The identification of "Kontakt" as a language mismatch provided a specific example of inconsistency that might be overlooked in a broader check.
  - **Micro-Alignment Issues:** The AI specifically pointed out the price alignment problem on the "Out of stock" item, highlighting a subtle but important visual inconsistency in the product grid.