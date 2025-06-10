# Use of AI Tools

**Tools Used:** ChatGPT

**Purpose:**

An AI tool was employed to generate a list of test cases based on manually constructed **Equivalence Partitioning (EP)** and **Boundary Value Analysis (BVA)** tables for the *Category Management* feature.

This approach helped:

- Accelerate the test case creation process.
- Ensure full coverage of valid/invalid partitions and boundary values.

**Prompt Used to Generate Test Cases:**

```text
I have manually created EP and BVA tables for a feature called [feature
 name]. Below is the detailed input constraints, followed by the EP and 
 BVA tables.

Please generate at least 40 high-quality test cases using both EP and 
BVA logic. Cover both positive and negative cases, including field-level
 and logic-level scenarios (e.g., invalid parent ID, duplicate slugs, 
 invalid deletions).

For each test case, provide:
- Test Case ID
- Title
- Preconditions (if any)
- Input values
- Test steps
- Expected result
- Type (EP or BVA)

[Inputs and Constraints]

[EP and BVA tables]
```

The full EP and BVA tables (as shown in Part 2 of the report) were directly pasted into the prompt. This provided ChatGPT with a complete understanding of input constraints, value ranges, and test boundaries, resulting in a high-quality, logic-driven test case list.

**Review and Refinement Process:**

- Each test case was reviewed to verify coverage of all identified EP classes and BVA points.
- Titles, test steps, and expected outcomes were adjusted where necessary to improve clarity and consistency.
- Redundant or low-value cases were removed to keep the final set concise and executable.

**Test Case Categorization:**

- **AI-generated**: The initial test case set was produced directly from the provided prompt and tables.
- **Manually refined**: Selected cases were edited for logic accuracy, completeness, and formatting quality.

**Reusability:**

The prompt is designed to be reusable for any web-based feature or form. By supplying well-structured EP and BVA tables along with clear input constraints, this method can consistently generate 30–40 high-quality test cases in a single session while maintaining test logic and coverage control.

\pagebreak