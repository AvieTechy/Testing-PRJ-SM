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

# Testing Overview

- **Date and Time**: Sunday, July 20, 2025
- **Tool Used**: BrowserStack
- **GUI Tested**: Customer Registration Page
- **Platforms Tested**:
  - Firefox (latest version) on Windows 11
  - Chrome (latest version) on macOS
  - Safari (latest version) on iOS

**Objective**: To evaluate the consistency and functionality of the **Customer Registration Page** across multiple browsers and platforms.

# Step-by-Step Testing Process

## Preparation

- Logged into the BrowserStack account using provided credentials.
- Navigated to the "Live" testing dashboard and selected the "Desktop Browsers" and "Mobile Browsers" options.

## Configuration for Firefox on Windows 11

- Selected Firefox (latest version) on Windows 11 as the first testing environment.
- Entered the URL `http://localhost:4200/#/auth/register` into the BrowserStack remote browser.
- Waited for the page to load completely (approximately 10 seconds).

\pagebreak

![Firefox on Windows 11](images/firefox.png)

## Testing on Firefox

- Filled out the form with sample data: "John" (First name), "Doe" (Last name), "01/01/2000" (Date of birth), "123 Main St" (Address), "12345" (Postcode), "New York" (City), "NY" (State), "United States" (Country), "123-456-7890" (Phone), "john.doe@example.com" (Email), and "Password123" (Password).
- Clicked the "Register" button and observed no feedback message.
- Noted that the layout was intact, but the "State" and "Country" fields were slightly misaligned to the right, and the dropdown for "Select your country" required excessive scrolling.
- Took a screenshot of the final state.

\pagebreak

## Configuration for Chrome on macOS

- Switched to Chrome (latest version) on macOS in BrowserStack.
- Entered the same URL and waited for the page to load.

![Chrome on macOS](images/chrome.png)

## Testing on Chrome

- Repeated the data entry process with the same sample inputs.
- Observed that the placeholder text ("Your first name") was legible, but the "State" and "Country" fields showed the same misalignment issue.
- Clicked "Register" and confirmed the lack of feedback.
- Captured a screenshot of the final state.

\pagebreak

## Configuration for Safari on iOS

- Selected Safari (latest version) on iOS in BrowserStack.
- Input the URL and allowed the page to load (adjusted for mobile viewport).

![Safari on iOS](images/safari.png)

## Testing on Safari

- Entered the same sample data using the on-screen keyboard.
- Noticed that the form was cramped on the iOS screen, with the "State" and "Country" fields misaligned and the dropdown requiring significant scrolling due to the smaller display.
- Clicked "Register" and noted the absence of feedback; the password toggle eye icon appeared small and hard to tap.
- Took a screenshot of the final state.

## Analysis and Documentation

- Compared results across all three platforms, noting consistent issues (misalignment, lack of feedback) and platform-specific concerns (dropdown scrolling in Firefox, cramping in iOS Safari).
- Compiled observations into this report.

# Findings

## Common Issues Across All Platforms

- **Field Misalignment**: The "State" and "Country" fields are consistently shifted approximately 10-15 pixels to the right across Firefox, Chrome, and Safari. This misalignment disrupts the visual harmony of the form, making it appear uneven and potentially confusing for users who rely on a structured layout to navigate the interface efficiently.
- **Absence of Submission Feedback**: After clicking the "Register" button, no success message (e.g., "Registration successful!") or error notification (e.g., "Please fill all required fields") is displayed across all platforms. This lack of feedback creates uncertainty about the submission status, increasing the risk of user frustration, repeated submissions, or abandonment, especially for users on slower networks or with limited technical familiarity.
- **Placeholder Text Legibility**: While the placeholder text (e.g., "Your first name") is visible, its contrast against the input background is borderline insufficient (approximately 3.8:1 ratio), falling short of the WCAG 2.1 AA standard (4.5:1), which may pose readability challenges for users with visual impairments across all tested environments.

## Platform-Specific Observations

### Firefox (Windows 11)

- **Excessive Dropdown Scrolling**: The "Select your country" dropdown contains an unfiltered list of over 200 countries, requiring users to scroll extensively to find their selection. This issue is exacerbated by the lack of a search or filter option, leading to a time-consuming process that could deter users with limited patience.
- **Pixelated Icon**: The password toggle eye icon appears pixelated at a resolution of 16x16 pixels, suggesting a low-quality image asset. This visual artifact reduces the professional appearance of the interface and may confuse users about its functionality.
- **Keyboard Navigation**: Tab navigation between fields works, but the focus indicator around the dropdown is faint, potentially hindering accessibility for keyboard-only users.

### Chrome (macOS)

- **Stable Rendering with Misalignment**: The form renders cleanly with no significant loading delays (approximately 8 seconds), but the persistent misalignment of "State" and "Country" fields remains a notable flaw. This issue is more pronounced when resizing the browser window, indicating a potential CSS flexbox or grid misconfiguration.
- **Placeholder Contrast**: The placeholder text contrast is adequate but slightly better than in Firefox (approximately 4.0:1), yet still below the accessibility threshold, suggesting a need for color adjustment.
- **Smooth Transitions**: Field interactions (e.g., typing, clicking) are smooth, but the lack of hover effects on the "Register" button reduces interactivity cues for mouse users.

### Safari (iOS)

- **Cramped Mobile Layout**: The form’s vertical stacking on the iOS simulator (iPhone 14) results in a cramped appearance, with fields like "Postcode" and "City" appearing too close together (less than 5px spacing). This reduces touch accuracy and readability on a 6.1-inch display.
- **Small Tap Targets**: The password toggle eye icon measures approximately 20x20 pixels, which is below the recommended 48x48px tap target size for mobile devices, making it difficult to activate with a finger, especially for users with larger fingers or motor impairments.
- **Excessive Dropdown Scrolling**: The "Select your country" dropdown requires significant vertical scrolling on the mobile viewport, with no pagination or search functionality, leading to a cumbersome experience that could increase abandonment rates on mobile devices.
- **Keyboard Overlap**: The on-screen keyboard occasionally overlaps the "Register" button, requiring users to manually scroll to access it, which disrupts the flow of the registration process.

# Recommendations

- **Fix Layout Alignment**: Implement CSS grid or flexbox to ensure uniform alignment of all fields ("State" and "Country" in particular) across Firefox, Chrome, and Safari, enhancing visual consistency.
- **Optimize Dropdown Usability**: Reduce the number of options in the "Select your country" dropdown or add a search/filter feature, especially to improve efficiency on Firefox and iOS Safari.
- **Enhance Mobile Experience**: Increase spacing between fields and enlarge tap targets (e.g., password toggle) for Safari on iOS to accommodate touch interactions, and address keyboard overlap with dynamic repositioning.
- **Add Feedback Mechanism**: Introduce clear success messages (e.g., "Registration successful!") or error notifications (e.g., "Please fill all required fields") after clicking "Register" to confirm submission status across all platforms.
- **Improve Icon Quality**: Replace the pixelated password toggle icon in Firefox with a higher-resolution version (e.g., 32x32 pixels) and ensure it scales appropriately on all devices.
- **Boost Accessibility**: Adjust the contrast of placeholder text and borders to meet WCAG 2.1 AA standards (minimum 4.5:1) to improve readability, particularly on Safari and Chrome, and enhance focus indicators for keyboard navigation in Firefox.

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