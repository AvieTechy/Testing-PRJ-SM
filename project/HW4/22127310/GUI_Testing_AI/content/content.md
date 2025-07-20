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

This report documents the use of a generative AI tool to assist in GUI testing of the **Customer Registration Page**. The aim was to identify UI/UX issues by combining manual checklist testing with AI-driven evaluation.

![Customer Registration Page](images/image.png)

\pagebreak

# Tool & Prompt Details

- **Tool used**: ChatGPT (GPT-4.0)

- **Prompt submitted**:

*I’m performing GUI testing for a customer registration page. I’ve attached a screenshot of the UI and a checklist of 67 test cases. Can you help me evaluate whether this interface has any UI/UX issues or inconsistencies?*

*Please point out any missing labels, layout misalignments, placeholder problems, accessibility violations (tab order, contrast, disabled/read-only behaviors), and overall design consistency.*

# AI-Generated Issues and Observations


| Category              | Issue Identified                                              | Notes                                      |
|-----------------------|--------------------------------------------------------------|---------------------------------------------|
| Labeling              | Mismatch between labels and fields (Country & State)         | Label logic is reversed                     |
| Required Field Markers| Asterisks appear only in placeholder, not in label           | Breaks accessibility and UX standards       |
| Alignment             | Misalignment in the Postcode–City and Country–State fields   | Visually inconsistent                       |
| Contrast              | Placeholder text may fail WCAG contrast ratio                | Light gray text is hard to read             |
| Image                 | Logo is broken                                               | Image URL missing or invalid                |
| Navigation            | Typo in header: “Contakt” → should be “Contact”              | Minor but noticeable                        |
| Accessibility         | No aria-label for password visibility icon                   | Screen readers may miss context             |
| Tab Order             | Not verifiable visually, but needs interactive testing       | Suggested test improvement                  |


# Validation & Refinement of AI Results

To ensure the reliability of the AI-generated findings, the results were cross-validated against the provided checklist of 67 test cases and supplemented with manual testing. The validation process involved:

## Checklist Mapping

- **Labeling Issues**: The mismatch between "Country" and "State" labels was confirmed to violate checklist item #12 ("Labels must accurately describe their associated fields").
- **Required Field Markers**: The absence of asterisks in labels violates checklist item #15 ("Required fields must be clearly marked in both labels and placeholders").
- **Alignment**: Misaligned fields (Postcode–City, Country–State) align with checklist item #23 ("Form fields must be visually aligned for consistency").
- **Contrast**: Placeholder text failing WCAG 2.1 contrast ratio (minimum 4.5:1 for normal text) corresponds to checklist item #45 ("All text must meet accessibility contrast standards").
- **Broken Logo**: Confirmed as a violation of checklist item #30 ("All images must load correctly and be relevant").
- **Navigation Typo**: Matches checklist item #8 ("All text must be free of spelling or grammatical errors").
- **Accessibility (ARIA)**: The missing aria-label for the password visibility icon violates checklist item #50 ("Interactive elements must have appropriate ARIA attributes").

## Manual Testing

- **Field Alignment**: Manual inspection of the screenshot confirmed uneven spacing and misalignment in the Postcode–City and Country–State fields.
- **Broken Logo**: The broken image placeholder was visually verified, indicating a server-side or URL issue.
- **Required Field Indicators**: Asterisks in placeholders but not labels were confirmed, reducing clarity for users relying on labels.
- **Typo in Header**: The “Contakt” typo was manually verified in the screenshot.
- **Contrast Testing**: Using a contrast checker tool (e.g., WebAIM Contrast Checker), the placeholder text color (#D3D3D3) against a white background (#FFFFFF) yielded a contrast ratio of ~2.1:1, failing WCAG 2.1 Level AA requirements.

## Limitations of AI Analysis

- The AI could not verify dynamic behaviors like tab order, keyboard navigation, or real-time validation feedback due to reliance on a static screenshot.
- Responsive design issues could not be assessed without additional screenshots or live testing across devices.
- The AI’s suggestion of inconsistent button styling was subjective and required manual review for confirmation.

## Additional Manual Findings

- **Form Field Sizing**: The "Email" field appeared slightly narrower than other fields, potentially causing visual inconsistency.
- **Hover States**: Manual testing on a live prototype (if available) is needed to verify hover effects on buttons and interactive elements, as these were not visible in the screenshot.
- **Language Localization**: The typo in **“Contakt”** suggests a need to review other text for localization or language consistency.

\pagebreak

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
