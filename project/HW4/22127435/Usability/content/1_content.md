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

This report outlines the findings from a usability study of the search and filter functionality on a tool e-commerce website. The study was conducted with 7 participants using a Google Forms survey to evaluate the feature's effectiveness, efficiency, and overall user satisfaction. The analysis reveals that while the fundamental filtering options are logically grouped, significant usability barriers prevent a smooth and intuitive user journey. The most critical issues are the unconventional placement of the search bar and the lack of clear feedback after a filter is applied.

# Introduction
## Background
The interface under review is a product listing page (PLP) for an online tool store. A key component of this page is the left-hand sidebar, which provides users with tools to sort, search, and filter the product grid. The usability of this feature is critical for product discovery and directly impacts user success and conversion rates.

## Goals & Objectives

The primary objectives of this usability test were to:

  - Evaluate the intuitiveness and ease of use of the **search and filter** controls.
  - Identify specific user pain points, areas of confusion, and friction.
  - Assess whether users can efficiently and confidently narrow down product listings to find what they need.
  - Collect actionable data to inform design improvements.

## Methodology

  - **Platform:** A survey was designed and distributed using **Google Forms**.
  - **Stimulus:** Participants were shown a static image of the product listing page.
  - **Process:** The survey consisted of a mix of task-based scenarios, rating scales, and open-ended questions to gather both quantitative and qualitative feedback.

## Participant Profile

  - **Number of Participants:** 7
  - **Profile:** The participants were a mix of individuals with varying degrees of familiarity with online shopping, from frequent users to occasional buyers. This diverse sample helps ensure the findings are representative of a broad user base.

# Survey Design & Questions

The survey was structured to guide participants through evaluating the interface, from initial impressions to detailed interactions.

## Initial Impression & Understanding

1. At first glance, what is the main purpose of the area on the left side of the screen?
2. On a scale of 1 (Very Confusing) to 5 (Very Clear), how easy is it to understand all the options available in the left sidebar?

## Task-Based Scenarios

3. **(Category Filter)** Imagine you need a "Hammer". Describe the exact steps you would take.
4. **(Price & Category Filter)** You want to find "Pliers" that cost less than $20. How would you accomplish this?
5. **(Search Function)** You are looking for a "spanner", which is not listed as a category. How would you find it using this page?
6. **(Interaction Expectation)** After you check the box for "Hand Saw", what do you expect to happen on the screen?

## Specific Component Evaluation

7. Where would you normally expect to find a "Search" bar on a website like this?
8. Does the placement of the "Search" section on this page meet your expectations? (Yes / No / Somewhat)
9. What is the difference between the "Sorth" dropdown at the top and the "Filters" section below it? Is this distinction clear?
10. Do you see any issues or potential problems with the list of checkboxes under "By category"?

## Qualitative & Overall Feedback

11. What is the most confusing or frustrating part of this sidebar?
12. Is there any information or filter option you feel is missing?
13. What single change would you make to improve this section?
14. On a scale of 1 (Not Confident) to 5 (Very Confident), how confident are you that you could find any specific tool you needed using these options?

# Key Findings

- **Positive:**

  - Filter categories (By category, By brand) are intuitive and well-understood.
  - Checkboxes are a familiar and effective mechanism for selection.
  - The price range slider is generally clear and perceived as useful.

- **Negative (Usability Concerns):**

  - **Poor Discoverability of Search:** The search bar's location within the sidebar is non-standard and easily overlooked.
  - **Interaction Ambiguity:** Users are unsure if filters apply instantly or require a separate action, creating confusion and uncertainty.
  - **Lack of Scalability:** The current flat-list design will become cluttered and difficult to use as more filter options are added.
  - **Minor UI Issues:** A typo in a primary heading ("Sorth") and the close proximity of Sort and Filter controls detract from the professionalism and clarity of the interface.

# Analysis of Findings

The feedback was aggregated and analyzed to identify recurring themes.

## Positive Feedback

  - **Logical Grouping:** All 7 participants correctly identified the purpose of the "By category" and "By brand" filters. The hierarchical structure was considered logical.
  - **Familiar Controls:** The use of checkboxes for multi-select and a slider for a range was universally understood. 6 of 7 participants found the price slider intuitive.

## Usability Issues Identified

### Concern 1: Poor Discoverability of the Search Bar (High Severity)

- **Finding:** In response to the task of finding a "spanner" (Question 5), 5 out of 7 participants stated they "looked at the top of the page" before eventually finding the search bar in the sidebar. When directly asked (Question 7), all 7 participants stated they expect a search bar in the header.

- **Impact:** Hiding a primary navigation tool like search violates a core web convention (Jakob's Law). This leads to user frustration, increased task time, and a risk of site abandonment if users believe search functionality is missing.

### Concern 2: Ambiguous Interaction Model (High Severity)

- **Finding:** When asked what happens after clicking a checkbox (Question 6), the results were split: 4 expected an automatic update, while 3 expected to find an "Apply" button. This 50/50 split indicates a fundamentally ambiguous design.

- **Impact:** This ambiguity forces users to guess, leading to a hesitant and inefficient interaction. Users may not trust that their selections have been registered, potentially causing them to repeat actions or misinterpret the results.

### Concern 3: Non-Scalable UI Design (Medium Severity)

- **Finding:** 4 participants, when prompted about potential issues with the checkbox list (Question 10), noted that the list could become "very long" and "hard to scan" if more tool categories or brands were added.

- **Impact:** The current design is not future-proof. As the store's inventory grows, the usability of the filter section will degrade, increasing cognitive load and making it tedious for users to find the options they need.

### Concern 4: Minor UI/UX Inconsistencies (Low Severity)

- **Finding:**
- 5 out of 7 participants noticed the typo "Sorth" instead of "Sort".
- 3 participants expressed slight confusion about the difference between "Sort" and "Filter", suggesting the visual hierarchy could be clearer.

- **Impact:** While minor, issues like typos and a lack of clear visual distinction between different controls can erode user trust and give the impression of a low-quality or poorly maintained website.

# Recommendations

The following recommendations are prioritized based on their potential impact on usability:

| Recommendation | Rationale & Benefit | Priority |
|:---------------|:-------------------|:---------|
| Relocate Search to Global Header | Aligns with universal user expectations, ensuring the search function is immediately visible and accessible from anywhere on the page. Drastically reduces time-to-task for search-first users. | High |
| Add "Apply Filters" & "Clear All" Buttons | Eliminates interaction ambiguity. The "Apply" button provides a clear confirmation step, giving users control. The "Clear All" link offers a simple way to reset the form, which is a common user need. | High |
| Implement Collapsible Accordion Filters | Makes the design scalable and reduces visual clutter. Users can focus on one category of filters at a time without being overwhelmed by a long, scrolling list. This improves scannability and reduces cognitive load. | Medium |
| Correct Typos and Refine Visual Hierarchy | Fix "Sorth" to "Sort". Add slightly more spacing or a faint dividing line between the Sort dropdown and the main Filters block to visually reinforce their distinct functions. This improves polish and professionalism. | Low |

# Conclusion
The current search and filter feature, while containing the necessary components, fails to provide a seamless user experience. The identified issues—particularly the misplaced search bar and the ambiguous interaction model—present significant barriers to efficient product discovery.
By implementing the high-priority recommendations, the design team can resolve the most critical usability flaws. Further adopting the medium and low-priority suggestions will create a robust, scalable, and user-friendly filtering system that builds user confidence and directly supports business goals.