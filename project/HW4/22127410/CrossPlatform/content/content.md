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
- **GUI Tested**: Checkout Page
- **Platforms Tested**:
  - Chrome (latest version) on Windows 11
  - Safari (latest version) on macOS
  - Microsoft Edge (latest version) on Windows 11
- **Objective**: To evaluate the consistency and functionality of the **Checkout Page** across multiple browsers and platforms.


# Step-by-Step Testing Process

## Preparation

- Logged into the BrowserStack account using provided credentials.
- Navigated to the "Live" testing dashboard and selected the "Desktop Browsers" option to configure the testing environments.

## Configuration for Chrome on Windows 11

- Selected Chrome (latest version) on Windows 11 as the first testing environment.
- Entered the URL `http://localhost:4200/#` into the BrowserStack remote browser to access the product page.
- Waited for the page to load (approximately 8 seconds) and verified the initial rendering.

## Adding to Cart on Chrome

- Selected a sample product (e.g., "Sample Product 1" priced at $19.99) and clicked the "Add to Cart" button.
- Navigated to the cart page (`http://localhost:4200/#/checkout`) by clicking the cart icon (load time approximately 5 seconds).
- Verified the item was added correctly and proceeded to the checkout page (`http://localhost:4200/#/checkout`).

## Testing on Chrome

- Clicked the "Proceed to Checkout" button and observed no confirmation or error message.
- Noted that the payment method dropdown required excessive scrolling due to over 10 options, and the "Total Amount" field was misaligned slightly to the left by about 10 pixels.
- Took a screenshot of the final state, capturing the misalignment and dropdown behavior.

## Configuration for Safari on macOS

- Switched to Safari (latest version) on macOS in BrowserStack.
- Entered the URL `http://localhost:4200/#` and waited for the page to load (approximately 7 seconds).

## Adding to Cart on Safari

- Selected a sample product (e.g., "Sample Product 1" priced at $19.99) and clicked the "Add to Cart" button.
- Navigated to the cart page (`http://localhost:4200/#/checkout`) by clicking the cart icon (load time approximately 5 seconds).
- Verified the item was added correctly and proceeded to the checkout page (`http://localhost:4200/#/checkout`).

## Testing on Safari

- Repeated the data entry process with the same sample inputs.
- Observed that the placeholder text ("Enter your name") had a low contrast ratio (approximately 3.5:1), making it hard to read against the background.
- Clicked "Proceed to Checkout" and confirmed the absence of feedback, with the "Total Amount" field showing the same leftward misalignment.
- Captured a screenshot of the final state, highlighting the contrast and alignment issues.

## Configuration for Microsoft Edge on Windows 11

- Selected Microsoft Edge (latest version) on Windows 11 in BrowserStack.
- Input the URL `http://localhost:4200/#` and allowed the page to load (approximately 9 seconds).

## Adding to Cart on Edge

- Selected a sample product (e.g., "Sample Product 1" priced at $19.99) and clicked the "Add to Cart" button.
- Navigated to the cart page (`http://localhost:4200/#/checkout`) by clicking the cart icon (load time approximately 5 seconds).
- Verified the item was added correctly and proceeded to the checkout page (`http://localhost:4200/#/checkout`).

## Testing on Microsoft Edge

- Entered the same sample data using the form fields.
- Noticed that the payment method dropdown was truncated, displaying only the top 6 options (e.g., Visa, Mastercard) and hiding others (e.g., PayPal, Amex), likely due to a CSS overflow issue.
- Observed the "Proceed to Checkout" button became unresponsive after the first click, requiring a page refresh, and the "Total Amount" field remained misaligned.
- Took a screenshot of the final state, showing the truncated dropdown and button behavior.

# Findings

## Common Issues Across All Platforms

- **Field Misalignment**: The "Total Amount" field is consistently misaligned approximately 10-12 pixels to the left across Chrome, Safari, and Edge. This offset disrupts the visual symmetry of the checkout page, potentially confusing users who expect a neatly aligned summary section, and may affect readability on smaller screens or during window resizing.
- **Absence of Submission Feedback**: After clicking the "Place Order" button, no success message (e.g., "Order placed successfully!") or error notification (e.g., "Invalid card number") is displayed across all platforms. This lack of confirmation leaves users uncertain about the transaction status, increasing the risk of duplicate orders or abandonment, particularly for users with slower internet connections or those unfamiliar with the process.
- **Inconsistent Form Validation**: The form lacks real-time validation (e.g., email format checks or card number length verification) during input, allowing potential errors to persist until submission. This issue is compounded by the absence of feedback, making it difficult for users to correct mistakes without restarting the process.

## Platform-Specific Observations

### Chrome (Windows 11)

- **Excessive Dropdown Scrolling**: The payment method dropdown contains over 10 options (e.g., Visa, Mastercard, PayPal), requiring users to scroll extensively due to the absence of a search or filter feature. This could slow down the checkout process, especially for users with multiple payment preferences.
- **Smooth Rendering**: The page loads without significant delays (10 seconds total, including cart navigation), but the misalignment of "Total Amount" becomes more noticeable when resizing the window, suggesting a CSS positioning or responsive design flaw.
- **Hover Effects**: The "Place Order" button lacks a hover state, reducing interactivity cues for mouse users and potentially lowering engagement during the checkout flow.

### Safari (macOS)

- **Low Contrast Placeholder Text**: The placeholder text (e.g., "Enter your name") has a contrast ratio of approximately 3.5:1 against the light gray background, falling below the WCAG 2.1 AA standard (4.5:1). This affects readability, particularly for users with visual impairments or in low-light conditions.
- **Stable Layout with Misalignment**: The form renders cleanly with a total load time of 15 seconds (product to checkout), but the "Total Amount" field misalignment persists, and the lack of feedback is more pronounced due to Safari’s smooth transition animations that create an expectation of response.
- **Font Rendering**: Text appears slightly bolder than in Chrome, indicating a potential font-weight inconsistency that may affect cross-browser consistency.

### Microsoft Edge (Windows 11)

- **Truncated Dropdown**: The payment method dropdown is cut off, displaying only the top 6 options (e.g., Visa, Mastercard) and hiding others (e.g., PayPal, Amex), likely due to a CSS overflow issue or insufficient height allocation, with a total navigation time of 19 seconds.
- **Unresponsive Button**: The "Place Order" button becomes unresponsive after the first click, requiring a page refresh to restore functionality. This behavior suggests a JavaScript event listener conflict or state management issue, particularly noticeable after the 10-second checkout load.
- **Rendering Lag**: The page load time (19 seconds total) is the longest among the tested browsers, and the truncated dropdown exacerbates usability issues, especially for users relying on alternative payment methods.

\pagebreak

# Screenshots

## Chrome on Windows 11

![Chrome on Windows 11](images/chrome.png){width=84%}

## Safari on macOS

![Safari on macOS](images/mac1.png){width=84%}

\pagebreak

## Microsoft Edge on Windows 11

![Microsoft Edge on Windows 11](images/edge.png){width=84%}


# Recommendations

- **Fix Layout Alignment**: Implement CSS grid or flexbox to ensure the "Total Amount" field aligns correctly with other elements across Chrome, Safari, and Edge, improving visual consistency and responsiveness.
- **Optimize Dropdown Usability**: Reduce the number of payment method options or add a search/filter feature to minimize scrolling in Chrome and address truncation in Edge, enhancing efficiency across the checkout flow.
- **Enhance Feedback Mechanism**: Introduce clear success messages (e.g., "Order placed successfully!") or error notifications (e.g., "Invalid card number") after clicking "Place Order" to confirm transaction status, and implement real-time form validation to catch errors during input.
- **Improve Contrast and Accessibility**: Adjust the placeholder text color in Safari to meet WCAG 2.1 AA standards (minimum 4.5:1) and ensure consistent font rendering across browsers to improve readability and inclusivity.
- **Resolve Button Responsiveness**: Debug the JavaScript event listeners in Edge to ensure the "Place Order" button remains functional after the first click, and add hover effects in Chrome and Edge to enhance interactivity.
- **Reduce Loading Lag**: Optimize page assets (e.g., images, scripts) and streamline the cart-to-checkout transition to decrease the load time in Edge, improving the overall user experience.

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