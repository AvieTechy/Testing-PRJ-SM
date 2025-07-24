# Group Information

Group ID: 07

| Member Name        | Student ID | Assigned Tables          | Status      |
|:-------------------------|:-----------|:---------------------------|:------|
| Cao Uyển Nhi       | 22127310   | Registration Page                  | Done |
| Lưu Thanh Thuý     | 22127410   | Checkout Page               | Done |
| Nguyễn Phước Minh Trí      | 22127424   | Category Page                | Done |
| Võ Lê Việt Tú      | 22127435   | Home Page              | Done |
| Trần Thị Cát Tường | 22127444   | Category Management Page                 | Done |

# Executive Summary

This report documents the results of cross-platform compatibility testing for the website's Homepage. The objective was to verify that the page renders and functions consistently across major web browsers on different operating systems. The test was executed on **Google Chrome** and **Microsoft Edge** on Windows 11, and on **Safari** on macOS Sequoia via BrowserStack. The primary finding is that the Homepage exhibits a high degree of consistency across all tested platforms. All visual and functional bugs previously identified, such as the broken logo and incorrect navigation links, were replicated uniformly on every browser. This indicates that these are core application bugs rather than platform-specific compatibility issues.

# Test Objective

To verify that the Homepage layout, visual elements, and basic functionalities are displayed and behave consistently across the following target environments:

- **Windows 11:** Google Chrome
- **Windows 11:** Microsoft Edge
- **macOS Sequoia:** Safari

# Step-by-Step Test Execution Procedure

The following methodical steps were taken to ensure thorough and consistent testing across each platform.

## Step 1: Establish Baseline on Primary Platform (Google Chrome on Windows 11)

The Homepage (`http://localhost:4200/#/`) was loaded in a clean browser session on Google Chrome. A visual and functional audit was performed, focusing on:

- **Overall Layout:** Verified header, body, and footer structure.
- **Visual Elements:** Inspected the logo, icons, and banners for correct rendering.
- **Typography:** Checked for font consistency and readability.
- **Navigation Functionality:** Tested all navigation links and dropdown menus.
- **Search Functionality:** Entered test queries in the search bar and verified results.
- **Filter Operations:** Applied various product filters and observed behavior.
- **Sort Operations:** Used the sort dropdown to change product ordering.
- **Interactive Elements:** Clicked dropdown lists in the navigation header and tested hover effects.

## Step 2: Replicate Test on Secondary Platform (Microsoft Edge on Windows 11)

- The same URL for the Homepage was loaded in Microsoft Edge.

- The exact audit procedure from Step 1 was repeated.

## Step 3: Replicate Test on Tertiary Platform (Safari on macOS)

- A remote testing session was initiated using BrowserStack, configured for the latest version of Safari on macOS Sequoia.

- The Homepage URL was loaded within the virtual environment.

- The exact audit procedure from Step 1 was repeated.

- The results from Safari were compared against the baseline. A screenshot was captured.

## Step 4: Analyze and Consolidate Findings

- The results and screenshots from all three platforms were collated.

- The analysis confirmed that all identified defects were present and identical in appearance and behavior across all environments.

## Step 5: Detailed Functional Testing

Additional interactive testing was performed on each platform to ensure comprehensive coverage:

- Search Functionality Testing
  - **Test Input:** Entered "hammer" in the search bar
  - **Expected Result:** Display relevant hammer products
  - **Actual Result:** Search works the same across all platforms

- Filter Operation Testing
  - **Test Action:** Applied category filter for "Power Tools"
  - **Expected Result:** Product grid updates to show only power tools
  - **Actual Result:** Filtering works correctly across all platforms

- Sort Functionality Testing
  - **Test Action:** Selected "Price: Low to High" from sort dropdown
  - **Expected Result:** Products reorder by ascending price
  - **Actual Result:** Sort functionality operates correctly despite label typo

- Navigation Dropdown Testing
  - **Test Action:** Clicked on "Categories" dropdown in header
  - **Expected Result:** Smooth dropdown expansion with category list
  - **Actual Result:** Animation timing slightly varies between browsers

- Filter Clear Testing
  - **Test Action:** Applied multiple filters then clicked "Clear All"
  - **Expected Result:** All filters reset, full product list displayed
  - **Actual Result:** Functionality works but button styling inconsistent

# Test Results & Observations

| Feature/Component | Expected Behavior | Observation Across All Platforms (Chrome, Edge, Safari) | Consistency Status |
|:------------------|:------------------|:--------------------------------------------------------|:-------------------|
| Overall Layout | Page structure is intact without overlapping or broken elements. | The layout is stable and consistent across all browsers. | Consistent |
| Website Logo | The logo is displayed clearly. | The logo is broken/fails to load. (Ref: Bug ID B003) | Consistent |
| 'Home' Link Navigation | Clicking 'Home' navigates to the homepage. | The link incorrectly navigates to the '/contact' page. (Ref: Bug ID B001) | Consistent |
| Nav Bar Hover Effect | Text color changes with sufficient contrast on hover. | The hover effect has low contrast. (Ref: Bug ID B002) | Consistent |
| Sort Dropdown Label | The label reads "Sort". | The label is misspelled as "Sorth". (Ref: Bug ID B004-Usability) | Consistent |

# Screenshot Evidence

The following screenshots confirm the consistent rendering of the Homepage, including its defects, across the tested platforms.

## Google Chrome on Windows 11

\begin{figure}[ht]
\centering
\includegraphics[width=0.8\textwidth]{./content/img/chrome1.png}
\caption{Homepage on Google Chrome (Windows 11)}
\end{figure}

\begin{figure}[ht]
\centering
\includegraphics[width=0.8\textwidth]{./content/img/chrome2.png}
\caption{Homepage on Google Chrome (Windows 11)}
\end{figure}

\pagebreak

## Microsoft Edge on Windows 11

\begin{figure}[ht]
\centering
\includegraphics[width=0.8\textwidth]{./content/img/edge1.png}
\caption{Homepage on Microsoft Edge (Windows 11)}
\end{figure}

\begin{figure}[ht]
\centering
\includegraphics[width=0.8\textwidth]{./content/img/edge2.png}
\caption{Homepage on Microsoft Edge (Windows 11)}
\end{figure}

\pagebreak

## Safari on macOS Sequoia (via BrowserStack)

\begin{figure}[ht]
\centering
\includegraphics[width=0.8\textwidth]{./content/img/safari1.png}
\caption{Homepage on Safari (MacOS Sequoia)}
\end{figure}

\begin{figure}[ht]
\centering
\includegraphics[width=0.8\textwidth]{./content/img/safari2.png}
\caption{Homepage on Safari (MacOS Sequoia)}
\end{figure}

\pagebreak

# Conclusion & Recommendation

The Homepage has successfully passed the cross-platform compatibility test, as it demonstrates consistent behavior and appearance across all targeted environments. The critical takeaway is that the identified defects are not cross-browser issues. They are rooted in the core application code. 

## Key Findings Summary:

### Consistent Issues (All Platforms):
- Broken logo display (Bug ID B003)
- Incorrect 'Home' link navigation (Bug ID B001) 
- Low contrast hover effects (Bug ID B002)
- Misspelled "Sorth" label (Bug ID B004-Usability)

### Platform-Specific Variations:
- Search input field styling varies slightly between browsers
- Dropdown animation timing is slower on Safari
- Filter button styling has minor inconsistencies

## Recommendations:

1. **Priority 1 (Critical Fixes):** Development efforts should focus on fixing the root cause of the reported bugs (B001, B002, B003, B004) within the main codebase.

2. **Priority 2 (Cross-Platform Consistency):** 
   - Standardize search input field styling across browsers
   - Optimize dropdown animations for consistent timing
   - Unify button styling for filter controls

3. **Priority 3 (Enhanced Testing):** No browser-specific fixes or CSS hacks are required for core functionality issues, as the problems are universal.

The interactive functionality (search, filter, sort, navigation dropdowns) works correctly across all platforms, with only minor styling and animation differences that don't impact core usability.