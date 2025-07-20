# Group Information

Group ID: 07

| Member Name        | Student ID | Assigned Tables          | Status      |
|:-------------------------|:-----------|:---------------------------|:------|
| Cao Uyển Nhi       | 22127310   | Registration                   | Done |
| Lưu Thanh Thuý     | 22127410   | Checkout                | Done |
| Nguyễn Phước Minh Trí      | 22127424   | - Product Image                | Done |
|                    |            | - Personal Access Token                | Done |
| Võ Lê Việt Tú      | 22127435   | - Product                | Done |
|                    |            | - Favorites                | Done |
| Trần Thị Cát Tường | 22127444   | - User                  | Done |
|                    |            | - Contact Requests      | Done |


# Introduction

Usability testing is an essential step in evaluating how intuitive and user-friendly an interface is for end users. In this task, we focused on the **Checkout Page** of a web-based e-commerce application, which consists of four steps: **Cart → Sign In → Address → Payment**

The goal was to identify usability concerns from a user perspective by conducting a structured survey. I created a Google Form containing 12 questions across two sections: demographic info and interface experience. The survey was distributed to 7 participants, and the collected feedback was analyzed to detect pain points, confusion, or design improvement opportunities.

# Survey Details

## Overview

- **Platform**: Google Forms
- **Feature Tested**: Checkout Page (UI and interaction flow)
- **Participants**: 7
- **Survey Structure**: 
  - Section 1: Demographic information (age, device used, online shopping experience)
  - Section 2: Interface experience (clarity, navigation, accessibility, and suggestions)

## Participant Profile

- Total Participants: 7
- Age Range: 20–28
- Devices Used: Laptop (3), Mobile (3), Tablet (1)
- Experience with Online Shopping (rated on a scale of 1–5):
  - 2 users: 2/5 (minimal experience)
  - 3 users: 3/5 (moderate experience)
  - 2 users: 4–5/5 (high experience)

## Sample Questions

1. How old are you?
2. What device did you use to test the interface?
3. Rate your familiarity with online shopping (1–5).
4. How clear was each step in the checkout process?
5. Were you able to understand and interact with quantity/price controls?
6. Did the system provide useful feedback at each step?
7. Were you confused at any point? If yes, where?
8. Identify any typos or broken elements you encountered.
9. Rate the visual layout and alignment throughout (1–5).
10. How well did the page support accessibility (contrast, labels, icons)?
11. What improvements would you suggest?
12. Would you feel confident completing a real purchase?


# Step-by-Step Analysis

## Step 1: Cart

**Description**: The Cart page displays the user's selected products, including names, quantities, prices, and total cost, with a visual progress indicator to track checkout progress.

![Cart](images/1.png)

**Strengths**:

- Clear and organized layout of product names, quantities, and prices.
- Visual progress indicator provides a sense of orientation within the checkout flow.
- Intuitive controls for adjusting quantities (e.g., +/– buttons).

**Problems Identified**:

- **Incorrect Subtotal Calculation**: Each product’s total is displayed as `$00.00`, despite valid quantity and price inputs, undermining user trust in the system.
- **Duplicate Column Headers**: The “Total” column header appears twice, creating ambiguity about whether it refers to cost or actions (e.g., remove item).
- **Accessibility Issue**: The red “X” buttons for removing items lack tooltips or ARIA labels, violating WCAG (Web Content Accessibility Guidelines) standards.
- **Broken Logo Image**: The header logo fails to load, reducing the page’s professionalism and credibility.
- **Spelling Error**: The navigation menu contains a typo (“Contakt” instead of “Contact”), which detracts from the interface’s polish.

## Step 2: Sign In

**Description**: The Sign In page allows users to authenticate or proceed as a guest, with a progress indicator to show the current step.

![Next step: Sign In](images/2.png)

![After Sign In successfully](images/3.png)

**Strengths**:

- Clear messaging for authenticated users, confirming successful sign-in.
- Consistent styling with other pages, maintaining a cohesive look.

**Problems Identified**:

- **Progress Indicator Misalignment**: The progress indicator incorrectly highlights “Cart” instead of “Sign In,” confusing users about their current position in the process.
- **Conflicting Navigation Signals**: The navigation bar simultaneously displays “Sign In” and “User Data not found,” creating confusion about the user’s authentication status.

## Step 3: Address Page

**Description**: The Address page collects billing and shipping information through a form, with a button to proceed to the next step.

![Address Page](images/4.png)

**Strengths**:

- Minimalist form design with consistent styling, reducing visual clutter.
- Clear input fields for address details.

**Problems Identified**:

- **Typographical Error**: The page title reads “Billing Adress” instead of “Billing Address.”
- **Unlabeled Submit Button**: The submit button is a plain green rectangle without text or an icon, making its purpose unclear.
- **Placeholder/Debug Text**: A field contains the text “missing value,” likely a remnant of development, which confuses users.
- **Lack of Validation**: No required field markers or real-time validation feedback, leading to potential errors during submission.

## Step 4: Payment Page

**Description**: The Payment page allows users to select a payment method and enter payment details, finalizing the checkout process.

![Final step: Payment](images/5.png)

**Strengths**:

- Clear dropdown menu listing available payment methods (e.g., Credit Card, PayPal).
- Consistent visual design aligns with previous steps.

**Problems Identified**:

- **Invalid Test Entry**: The dropdown includes an erroneous option, “Errror 304 - Missing Payment Gateway,” indicating incomplete development or testing.
- **Static Payment Form**: The form does not dynamically update based on the selected payment method (e.g., no credit card fields appear when “Credit Card” is chosen).
- **Navigation Limitation**: No “Back” or “Edit” buttons to return to previous steps, forcing users to restart if corrections are needed.
- **Poor Layout**: The dropdown menu has insufficient padding and misaligned elements, impacting readability and aesthetics.

# Participant Feedback Highlights

| **Feedback Theme**      | **User Comments**                                                                 |
|----------------------------|------------------------------------------------------------------------------------|
| Trust & Confidence      | “I didn’t trust the checkout when the prices didn’t update properly.”            |
| Visual Hierarchy        | “The total line was okay, but the layout felt off.”                              |
| Language & Clarity      | “Did you mean Contact? I saw ‘Contakt’ on the menu.”                             |
| Guidance & Flow         | “I wasn't sure I finished the Sign In step.”                                     |
| Accessibility & Icons   | “I didn’t know what the red cross button did.”                                   |
| Professionalism         | “Some parts look like placeholder content.”                                      |


# Consolidated Usability Issues

| **Area**              | **Issue**                                                    | **Recommendation**                               |
|--------------------------|--------------------------------------------------------------|---------------------------------------------------|
| Calculation Logic      | Totals per item = $0.00                                     | Fix subtotal formula (price × quantity)          |
| Icon Accessibility     | Red “X” button lacks tooltip or label                       | Add tooltips/aria-labels                         |
| Typography             | Spelling: “Contakt”, “Adress”, “Errror”                     | Proofread and correct                            |
| Step Indicator Logic   | Highlight does not change with actual progress              | Update progress indicator dynamically            |
| Layout Consistency     | Button and dropdown misalignment                            | Align elements using CSS grid/flex layout        |
| Validation Messaging   | No field validation on Address step                         | Add inline error messages + required indicators  |
| Navigation Gaps        | No "Back" button from Payment step                          | Add backward navigation for correction flexibility |

# Recommendations for Improvement

To address the identified usability issues and enhance the overall checkout experience, the following recommendations are proposed:

**Fix Subtotal Calculation Logic**:

- Ensure the Cart page accurately calculates and displays per-item subtotals (price × quantity).
- Test calculations across edge cases (e.g., zero quantity, high quantities).

**Correct Typographical Errors**:

- Proofread and correct all text, including “Contakt” → “Contact,” “Adress” → “Address,” and “Errror” → “Error.”
- Implement a content review process to prevent future typos.

**Enhance Accessibility**:

- Add tooltips and ARIA labels to interactive elements (e.g., red “X” buttons).
- Ensure sufficient color contrast for text and icons per WCAG 2.1 guidelines.
- Test with screen readers (e.g., NVDA, VoiceOver) to verify compatibility.

**Improve Navigation and Flow**:

- Implement a dynamic progress indicator that accurately reflects the current step.
- Add “Back” and “Edit” buttons on all steps to allow users to revise inputs without restarting.
- Resolve conflicting navigation signals (e.g., “Sign In” vs. “User Data not found”).

**Enhance Form Functionality**:

- Add real-time validation and required field markers on the Address page.
- Implement dynamic rendering of payment forms based on the selected payment method (e.g., credit card fields for “Credit Card”).
- Label the submit button clearly (e.g., “Proceed to Payment”).

**Polish Visual Design**:

- Fix the broken logo image in the header to enhance credibility.
- Adjust padding and alignment for dropdowns and buttons using CSS grid or flexbox.
- Remove placeholder or debug text (e.g., “missing value,” “Errror 304”).

**Conduct Cross-Platform Testing**:

- Use tools like BrowserStack to ensure consistent rendering across browsers (Chrome, Safari, Firefox) and devices (laptop, mobile, tablet).
- Address layout shifts and font inconsistencies reported on mobile devices.

# Conclusion

The **checkout flow** of the e-commerce application is logically structured, with clear steps and a consistent visual design. However, critical usability issues—such as incorrect subtotal calculations, typographical errors, accessibility shortcomings, and navigation gaps—significantly hinder the user experience. These issues reduce trust, increase confusion, and risk higher cart abandonment rates, particularly for users with limited online shopping experience or those relying on assistive technologies.

By implementing the recommended improvements, including fixing calculation logic, enhancing accessibility, and refining navigation, the checkout process can become more intuitive, inclusive, and trustworthy. These changes will improve user satisfaction, support a wider range of devices and user needs, and align the interface with industry-standard UX practices.

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