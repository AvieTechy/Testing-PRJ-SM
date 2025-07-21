# Cross-Platform GUI Testing Report

**Tested Page**: Categories Management – `/admin/categories`


## Objective

The goal of this test is to evaluate the visual consistency, responsiveness, and basic interactivity of the Categories Management screen across three major desktop browsers.

## Testing Environment & Setup

The application was running locally on `http://localhost:4200`, which is not publicly accessible by default. To enable external browser testing, **BrowserStack Live** was used in combination with **BrowserStack Local**.

**Local Testing Configuration:**

* Installed the **BrowserStack Local GUI** client.
* Retrieved and entered the Access Key from BrowserStack account settings.
* Launched a secure tunnel between BrowserStack and the local server.
* Successfully confirmed connection via BrowserStack’s debugging console (`status 200`).

![Successfully confirmed connection](images/0.png){ height=300px }

* Logged into the application using the following admin credentials:

  ```
  Email: admin@practicesoftwaretesting.com
  Password: welcome01
  ```

* Accessed the Categories Management screen using:

  ```
  http://localhost:4200/#/admin/categories
  ```

## Browsers Used

| Platform   | Browser         | Version   |
| ---------- | --------------- | --------- |
| Windows 11 | Google Chrome   | 140 (Dev) |
| Windows 11 | Microsoft Edge  | 138       |
| Windows 11 | Mozilla Firefox | 140       |

## Testing Methodology

Each browser session was accessed via BrowserStack Live. After logging into the app (admin credentials), the `/admin/categories` page was opened. The following interactions and elements were evaluated:

* Page load rendering and layout structure
* Table visibility and alignment
* Button appearance and hover behavior
* Search and reset controls
* Responsiveness (scroll, resizing)
* Font and color consistency

## Observations

### Chrome on Windows 11

* Page loaded successfully with proper spacing and layout.
* All rows and buttons rendered correctly.
* Colors (green, blue, red) were vivid and consistent.
* Table scroll behaved as expected.
* No alignment or overflow issues observed.

![Chrome](images/1.png){ height=300px }

### Edge on Windows 11

* Rendering was nearly identical to Chrome.
* Button hover effect on "Delete" appeared slightly delayed.
* Minor spacing inconsistency on the right edge of the “Add Category” button when window was resized.

![Edge](images/2.png){ height=300px }

### Firefox on Windows 11

* Page loaded fully without visible breaks.
* Text font rendering appeared slightly bolder than Chrome and Edge.
* Browser showed “Not Secure” warning due to localhost access (not a functional issue).
* Table alignment and buttons were intact.
* No hover issues observed, but slight lag in search field response on first input.

![Firefox](images/3.png){ height=300px }

## Summary of Findings

| Issue                                | Chrome | Edge           | Firefox            |
| ------------------------------------ | ------ | -------------- | ------------------ |
| Layout and spacing consistent        | Yes    | Mostly         | Yes                |
| Font and button rendering            | Yes    | Yes            | Slightly bold text |
| Hover effects responsive             | Yes    | Slight delay   | Yes                |
| Scrollbar behavior                   | Normal | Appeared early | Normal             |
| “Not Secure” warning (localhost)     | No     | No             | Yes                |
| Functional interaction (Edit/Delete) | Yes    | Yes            | Yes                |

## Recommendations

While the Categories Management page is mostly consistent across Chrome, Edge, and Firefox, a few improvements can enhance user experience and maintain cross-browser compatibility:

* **Hover Feedback Consistency**: Improve the responsiveness of hover states on action buttons (especially “Delete”) to ensure immediate visual feedback in all browsers.
* **Responsive Padding**: Apply consistent spacing rules (e.g., margin-right or padding-inline-end) to elements such as the “Add Category” button, particularly in Edge on window resize.
* **Scroll Behavior**: Fine-tune the scroll threshold or overflow detection to prevent unnecessary horizontal scrollbars on Edge when the layout fits within the screen.
* **Font Rendering Standardization**: Consider using standardized `font-weight`, `font-smoothing`, and web-safe fonts to avoid bold font differences between Firefox and other browsers.
* **Security Warning Mitigation**: Although not affecting functionality, developers may consider setting up HTTPS for local development using self-signed certificates to avoid “Not Secure” warnings in browsers like Firefox during usability testing.

## Conclusion

The Categories Management interface demonstrates strong consistency across modern desktop browsers, with only minor differences in visual behavior and responsiveness. Using tools like BrowserStack Live and Local Testing allows early detection of these subtle discrepancies before deployment. Overall, the interface performs reliably and remains fully functional across all tested environments.
