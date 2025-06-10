# Equivalence Partitioning and Boundary Value Analysis Design Process

## Feature 1: Contact

### Inputs and Constraints

The Contact form includes the following fields, with variations depending on user authentication status, all constraints were identified through manual interaction with the web UI and observing real-time validation errors on the form:

- **If the user is logged in:**
  - **Subject**: dropdown selection, required, must select a valid (non-default) option.
  - **Message**: required textarea, must be between 50 and 250 characters.
  - **Attachment**: optional, only `.txt`, `.pdf`, or `.jpg` files allowed, size $\leq$ 500KB.

![Contact function interface for user](images/feature1_user.png){ height=280px }

- **If the user is a guest (not logged in):**
  - **First Name**: required text input, max length 120 characters.
  - **Last Name**: required text input, max length 120 characters.
  - **Email**: required, max length 120 characters, must be in valid email format (e.g., name@example.com).
  - **Subject**: dropdown selection, required, must select a valid (non-default) option.
  - **Message**: required textarea, must be between 50 and 250 characters.
  - **Attachment**: optional, only `.txt`, `.pdf`, or `.jpg` files allowed, size $\leq$ 500KB.

![Contact function interface for guest](images/feature1_guest.png){ height=280px }

### Equivalence Partitioning (EP)

| Field      | Valid Partition                                       | Invalid Partition                                      |
|---------------------|----------------------------------------------|--------------------------------------------------------|
| First Name | Non-empty, $\leq$ 120 characters                           | Empty, > 120 characters                                |
| Last Name  | Non-empty, $\leq$ 120 characters                           | Empty, > 120 characters                                |
| Email      | Valid email format (e.g. `a@b.com`)                   | Missing `@`, missing domain, empty, malformed format, > 120 characters   |
| Subject    | A valid selected option (not default/empty)           | Not selected (empty/default value)                     |
| Message    | Non-empty, $\geq$ 50 and $\leq$ 250 characters                  | Empty, < 50 characters, > 250 characters               |
| Attachment | `.txt`, `.pdf`, `.jpg`, file size $\leq$ 500KB             | Wrong type (e.g. `.docx`, `.exe`), size > 500KB        |

### Boundary Value Analysis (BVA)

| Field      | Valid Values                                   | Invalid Values                       |
| -------------- | ---------------------------------------------- | ------------------------------------ |
| First Name | Length: 1, 120                                 | Length: 0, 121                       |
| Last Name  | Length: 1, 120                                 | Length: 0, 121                       |
| Email      | Format: `a@b.com`, `a@b.c`; Length: 1, 120                     | Format: `a.com`, `a@`, `a@b`, `a@b..com`; Length: 0, 121 |
| Subject    | A selected option from dropdown                | Default (empty), not in list         |
| Message    | Length: 50, 250                                | Length: 0, 49, 251                   |
| Attachment | Type: `.txt`, `.pdf`, `.jpg`; Size: 0KB, 500KB | Type: `.docx`, `.exe`; Size: 501KB   |

## Feature 2: Category Management

### Inputs and Constraints

Category Management allows admin to perform the following operations, all constraints were identified through manual interaction with the web UI and observing real-time validation errors on the form:

1. **Add Category**

![Add category function interface for admin](images/feature2_add.png){ height=280px }

- **Parent Id** (Dropdown):
  - Optional.
  - Must be the `id` of an existing category.
  - Cannot be the same as the new category’s own `id` (if known).
  
- **Name** (Text):
  - Required.
  - Maximum length: 120 characters.
  - Cannot be the same as an existing category.

- **Slug** (Text):
  - Required.
  - Must be lowercase, URL-safe (hyphens instead of spaces).
  - Must be unique (no duplicate slugs allowed in the database).

2. **Edit Category**

![Edit category function interface for admin](images/feature2_edit.png){ height=280px }

- Same input rules as **Add**.
- Cannot change to have itself as its own parent.

3. **Delete Category**

![Delete category function interface for admin](images/feature2_delete.png){ height=280px }

- Allowed only if:
  - The category is not currently set as `Parent Id` of other categories or is having products.
  - Otherwise, a warning is shown: *"Seems like this category is used elsewhere."*

4. **Search Category**

![Search category function interface for admin](images/feature2_search.png){ height=280px }

- Search by keyword in the **Name** field.
- Case-insensitive and supports partial match.
- Empty search returns full list.

### Equivalence Partitioning (EP)

| Operation | Field     | Valid Partition                                               | Invalid Partition                                           |
| ----------------------- | ----------------------- | -------------------------------------------------------------- | ----------------------------------------------------------- |
| Add/Edit  | Parent Id | Empty or existing category `id` (≠ own id)                    | Non-existing `id`, or same as own `id`                      |
| Add/Edit  | Name      | Non-empty string ≤ 120 characters                             | Empty string, > 120 characters                              |
| Add/Edit  | Slug      | Unique, lowercase, hyphenated, ≤ 120 characters               | Empty, contains spaces/special chars, duplicate in database |
| Delete    | Category  | Category with no child categories                             | Category used as parent elsewhere                           |
| Search    | Keyword   | Empty or string that matches existing category name (partial) | Strings that don’t match any name                           |

### Boundary Value Analysis (BVA)

| Field     | Valid Values                           | Invalid Values                                |
| -------------- | -------------------------------------- | --------------------------------------------- |
| Name      | Length: 1, 120                         | Length: 0, 121                                |
| Slug      | Length: 1, 120; Format: `hand-tools`   | Length: 0, 121; Format: `Hand Tools`, `tool!` |
| Parent Id | Existing IDs ≠ current id              | Own `id`, non-existing ids                    |
| Search    | Length: 0 (returns all), Length: 1–120 | — (no functional invalid case for input size) |

\pagebreak
