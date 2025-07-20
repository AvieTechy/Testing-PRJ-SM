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

Usability testing is a vital process to assess the effectiveness, efficiency, and satisfaction of a user interface. This report focuses on the **Customer Registration Page** of a web-based application, designed to collect essential user information for account creation. The page includes fields for personal details, contact information, and security credentials, culminating in a "Register" button to submit the form.

![Customer registration](images/image.png)

The evaluation involved conducting a structured survey with 7 participants to identify usability issues from a user perspective. The survey, created using Google Forms, comprised 12 questions across demographic and interface experience sections. Feedback was analyzed to highlight pain points, areas of confusion, and opportunities for design enhancement. This report summarizes the findings and provides recommendations to improve the registration process.

# Survey Details

## Overview
- **Platform**: Google Forms
- **Feature Tested**: Customer Registration Page (UI and interaction flow)
- **Participants**: 7
- **Survey Structure**: 
  - Section 1: Demographic details (age, device used, online registration experience)
  - Section 2: Interface experience (clarity, navigation, accessibility, and suggestions)

## Participants
- **Total Participants**: 7
- **Age Range**: 18–21 years old
- **Devices Used**:
  - Laptop: 3 participants
  - Mobile: 4 participants
- **Experience with Online Registration** (rated on a scale of 1–5):
  - 2 users: 2/5 (minimal experience)
  - 3 users: 3/5 (moderate experience)
  - 2 users: 4–5/5 (high experience)

## Sample Survey Questions

- How old are you?
- What device did you use to test the interface?
- Rate your familiarity with online registration (1–5).
- How clear were the instructions for filling out the form?
- Were you able to easily input data into all fields?
- Did the form provide useful feedback (e.g., error messages) when submitting?
- Were you confused at any point? If yes, where?
- Did you notice any typos, broken elements, or layout issues?
- Rate the visual layout and alignment of the registration page (1–5).
- How well did the page support accessibility (e.g., contrast, labels)?
- What improvements would you suggest for the registration process?
- Would you feel confident registering on this platform?

# Detailed Evaluation

**Description**: This single-page form collects user data including first name, last name, date of birth, address, postcode, city, state, country, phone, email, and password, with a "Register" button to submit.

**Positive Aspects**:

- **Clean Design**: The form employs a minimalist aesthetic with consistent styling, using a white background, gray input borders, and a blue "Register" button, which enhances readability and visual appeal.
- **Required Field Indicators**: Asterisks (*) next to field labels (e.g., "First name *") clearly denote mandatory fields, aiding users in understanding essential inputs.
- **Intuitive Placement**: The "Register" button is positioned at the form’s bottom center, making it easily accessible and logically concluding the input process.
- **Responsive Layout**: The design adapts reasonably well to different screen sizes, maintaining legibility on laptops, mobiles, and tablets, though minor adjustments are needed (as noted below).
- **Visibility Toggle**: A small eye icon next to the password field allows users to toggle password visibility, offering a convenient feature for verifying input accuracy.

**Identified Issues**:

- **Ambiguous Placeholder Text**: Fields such as "Your first name," "Your address," and "Your postcode" use placeholder text that resembles pre-filled data. This ambiguity can lead users to assume the fields are auto-populated, resulting in hesitation or incorrect submissions, particularly for less experienced users.
- **Inadequate Date Input Support**: The "Date of birth" field displays a "dd/mm/yyyy" placeholder without a date picker or additional guidance. This lack of support increases the likelihood of formatting errors (e.g., "mm/dd/yyyy" vs. "dd/mm/yyyy"), especially for users unfamiliar with the expected format, and may frustrate those seeking a more interactive solution.
- **Dropdown Usability Gap**: The "Select your country" dropdown lacks a default or placeholder option (e.g., "Please select a country"), requiring users to manually scroll and select an option. This adds an unnecessary step and may confuse users expecting a pre-set value, particularly on mobile devices where dropdown navigation can be cumbersome.
- **Unlabeled Password Toggle**: The eye icon for toggling password visibility lacks a tooltip or label (e.g., "Show/Hide Password"). This omission leaves users uncertain about its function, potentially deterring them from using it, and poses an accessibility challenge for screen reader users who need explicit descriptions.
- **Layout Misalignment**: The "State" and "Select your country" fields are slightly misaligned with other inputs, appearing shifted to the right. This inconsistency disrupts the visual flow, making the form appear uneven and potentially confusing users, especially on smaller screens where alignment issues are more pronounced.
- **Absence of Submission Feedback**: After clicking the "Register" button, no success message (e.g., "Registration successful") or error notification (e.g., "Please fill all required fields") is displayed. This lack of feedback leaves users unsure whether the submission was processed, increasing anxiety and the risk of duplicate submissions, particularly critical for users on slower networks or devices.
- **Mobile Responsiveness Limitation**: On mobile devices, the form’s vertical stacking works, but the narrow screen width causes some fields (e.g., "Postcode" and "City") to feel cramped, and the dropdown menu requires excessive scrolling, impacting usability for mobile users.
- **Contrast and Accessibility Concern**: While the text is legible, the gray placeholder text and input borders have a contrast ratio slightly below the WCAG 2.1 AA standard (4.5:1 for normal text), which may affect users with visual impairments, especially in low-light conditions.


# User Feedback Summary

The table below highlights key feedback themes with sample comments:

| **Theme**                | **User Remarks**                                                               |
|--------------------------|--------------------------------------------------------------------------------|
| **Clarity Issues**       | “I thought ‘Your first name’ was already filled in—what should I enter?”       |
| **Input Difficulties**   | “The date field needs a calendar or better instructions.”                     |
| **Design Consistency**   | “The country and state fields don’t match the layout of other fields.”         |
| **Accessibility Concerns**| “The eye icon on the password didn’t explain if it shows or hides it.”         |
| **Feedback Gaps**        | “I clicked Register but got no confirmation—did it work?”                      |
| **Trust Factors**        | “The lack of feedback made me question if the form was secure.”                |

# Summary of Usability Problems

The following table outlines key issues, their effects, and proposed fixes:

| **Category**             | **Problem**                                           | **Effect**                                          | **Suggested Action**                              |
|--------------------------|-------------------------------------------------------|----------------------------------------------------|---------------------------------------------------|
| **Placeholder Clarity**  | Ambiguous text (e.g., "Your first name")              | Confuses users about input requirements            | Use examples or instructional text                |
| **Date Entry**           | No date picker or format guide for "dd/mm/yyyy"       | Leads to input errors and frustration              | Add a date picker or format example               |
| **Dropdown Navigation**  | No default option in country selection                | Increases effort to complete the field             | Include a default (e.g., "Choose a country")      |
| **Password Toggle**      | Unlabeled eye icon for password visibility            | Users unsure of its function                       | Add a tooltip (e.g., "Toggle password visibility")|
| **Layout Alignment**     | Misaligned "State" and "Country" fields               | Disrupts visual harmony                            | Use CSS grid/flexbox for uniform alignment        |
| **Submission Feedback**  | No response after clicking "Register"                 | Leaves users uncertain about success               | Implement success/error messages                  |
| **Mobile Usability**     | Cramped fields and excessive dropdown scrolling       | Reduces efficiency on mobile devices               | Optimize spacing and dropdown behavior            |
| **Accessibility**        | Suboptimal contrast for placeholders and borders      | Challenges users with visual impairments           | Increase contrast to meet WCAG 2.1 AA standards   |

# Improvement Recommendations

To address the usability challenges and enhance the registration experience, consider the following:

**Refine Placeholder Text**:

- Replace placeholders with clear examples (e.g., "John" for "Your first name").
- Use a lighter color or italicized font to differentiate placeholders from user input.

**Enhance Date Input**:

- Integrate a date picker for "Date of birth" to simplify selection and reduce errors.
- Add a format hint (e.g., "dd/mm/yyyy: 20/07/2025") if a picker is not feasible.

**Improve Dropdown Functionality**:

- Set a placeholder option in "Select your country" (e.g., "Please select").
- Ensure the dropdown is optimized for mobile with a larger touch target and keyboard navigation support.

**Clarify Password Toggle**:

- Add a tooltip to the visibility toggle (e.g., "Show/Hide Password").
- Include an ARIA label for screen reader compatibility (e.g., `aria-label="Toggle password visibility"`).

**Correct Layout Issues**:

- Align all fields consistently using CSS grid or flexbox.
- Test and adjust responsiveness to ensure uniform alignment across devices.

**Add Feedback System**:

- Display a success message (e.g., "Account created successfully!") or error alert (e.g., "Missing required fields") post-submission.
- Use a modal or prominent banner for feedback visibility.

**Optimize Mobile Experience**:

- Increase spacing between fields on mobile to prevent crowding.
- Limit dropdown options or implement a search feature for "Select your country."

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