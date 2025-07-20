# Group Information

Group ID: 07

| Member Name        | Student ID | Screen          | Status      |
|:-------------------------|:-----------|:---------------------------|:------|
| Cao Uyển Nhi       | 22127310   |  Customer Registration Page | Done |
| Lưu Thanh Thuý     | 22127410   | Checkout Page                   | Done |
| Nguyễn Phước Minh Trí      | 22127424   | - Product Image   | Done |
| Võ Lê Việt Tú      | 22127435   | - Product                | Done |
| Trần Thị Cát Tường | 22127444   | - User                  | Done |

# Introduction

**GUI (Graphical User Interface) testing** is essential to ensure a web application’s interface is user-friendly, accessible, and functionally accurate. Traditionally, GUI testing is performed manually using a detailed checklist of test cases that evaluate layout, labels, input fields, color contrast, tab order, and compliance with accessibility standards. However, as software grows more complex and development cycles shorten, incorporating **Generative AI** tools into the GUI testing process can greatly improve speed and coverage.

In this report, we utilized ChatGPT (GPT-4.0), a leading generative AI model assist in identifying UI/UX issues on a checkout page of a demo web application. We provided:

- A screenshot of the checkout page UI.
- A GUI test checklist (Excel file with 67 entries).

![Checkout Page](images/image.png)

# Tool and Prompt Used

## Tool Used

- Tool name: ChatGPT by OpenAI
- Platform: ChatGPT Desktop App (OpenAI)
- Model version: GPT-4.0

## Prompt Used

*I’m reviewing the checkout page of a web application and have attached a screenshot along with a test case checklist—please help identify any UI/UX issues such as missing labels, alignment problems, placeholder inconsistencies, accessibility violations (e.g., tab order, contrast, screen reader compatibility), or any deviations from standard design patterns.*

# AI-Generated Observations

| **Category**          | **Issue**                                                                 | **AI Suggestion**                                                                 |
|-------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **Data Calculation**  | Total prices for individual items show `$0.00`, despite valid quantity and unit price. | Compute total = Quantity × Price per item.                                       |
| **Labeling**          | “Total” header appears twice: once for item price, once for action column. | Rename or clarify column headers (e.g., use “Actions” instead).                  |
| **Input Fields**      | Quantity input fields lack visible or semantic labels.                    | Add `aria-label` for accessibility (e.g., “Quantity for Pliers”).               |
| **Visual Alignment**  | Red “X” buttons are not perfectly aligned with text rows.                 | Adjust button positioning for cleaner vertical alignment.                        |
| **Button Placement**  | “Proceed to checkout” button is misaligned with the table layout.         | Align button with table width or center it horizontally.                        |
| **Contrast Issues**   | Gray text used in step indicators and table headers may have low contrast. | Use higher-contrast colors to meet WCAG standards.                              |
| **Icon-Only Actions** | Red delete button uses icon only; problematic for accessibility.          | Add tooltip or text label (e.g., `title="Remove item"`).                        |
| **Broken Image**      | Logo image at the top-left appears broken or missing.                    | Verify image path or add fallback alt text.                                     |
| **Spelling**          | "Contakt" in top navigation is a typo.                                    | Correct to “Contact”.                                                           |

\pagebreak

# Validation of AI Results Against Checklist

| **Checklist Item**        | **Matched Observation**                             | **AI Result Status** |
|---------------------------|-----------------------------------------------------|------------------------|
| Item 10 – Total calculation logic  | Incorrect per-item total = `$0.00`              |  Validated            |
| Item 18 – Label accessibility      | Quantity field lacks ARIA or labels             | Validated            |
| Item 24 – Layout alignment         | Misaligned delete button                        | Validated            |
| Item 31 – Spelling                 | "Contakt" typo in header                        | Validated            |
| Item 40 – Placeholder/field hints | No hint text or contextual labels               | Validated            |
| Item 47 – Button layout            | “Checkout” button misaligned                    | Validated            |
| Item 53 – Contrast ratio           | Gray text may violate accessibility contrast    | Validated            |

Each issue was confirmed through manual inspection to ensure that the AI did not raise any false positives. The combination of AI feedback and checklist validation proved efficient in surfacing key usability problems early.


# Conclusion

Integrating ChatGPT into GUI testing workflows provides a practical and scalable way to identify visual and structural UI issues early in the development cycle. By combining AI-based review with checklist validation, we achieved both speed and accuracy in uncovering critical interface defects. This experiment demonstrates that AI is an effective co-pilot in GUI evaluation, especially when guided by structured human input.


# Self-Assessment

| Criteria | Outcomes | Grade | Self-Assessed |
|:----------:|--------------------------------------------------------------------------------|:-------:|:----------------------:|
| **1**    | **Checklist of one GUI**| | | 
||Created and applied a comprehensive checklist to evaluate GUI elements such as alignment, contrast, tab order, and placeholder usage. | **30** | **30** |
| **2**    | **AI tools** |||
||Used ChatGPT and contrast checkers to assess accessibility and usability of the GUI. Verified tool suggestions with manual checks. | **20** | **20** |
| **3**    | **User survey and feedback** | **30** | **30** |
| 3.1      | Questions (10) |||
||Designed clear and concise questions focusing on GUI usability, clarity, and aesthetics | 10 | 10 |
| 3.2      | Feedback (7) |||
||Collected detailed user feedback; majority pointed out form alignment and button visibility issues. | 10 | 10 |
| 3.3      | Report |||
||Synthesized findings into a structured report with charts and direct quotes, highlighting top UX concerns. | 10 | 10 |
| **4**    | **BrowserStack** |||
||Used BrowserStack to test GUI across multiple browsers (Chrome, Safari, Firefox). Logged compatibility issues. | **30** | **30** |
| **5**    | **Bug report** | **30** | **30** |
| 5.1      | GUI |||
||Reported visual inconsistencies such as misaligned labels and buttons. Included screenshots. | 10 | 10 |
| 5.2      | Usability |||
||Identified issues in button feedback and navigation flow. Suggested improvements. | 10 | 10 |
| 5.3      | Cross-platform |||
||Tested on Android, iOS, Windows. Noted layout shifts and font inconsistencies. | 10 | 10 |
|| **Total** | **140** | **140** |