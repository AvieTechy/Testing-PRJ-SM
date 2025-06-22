# Scenario Definition

## Feature 1: Contact (Guest User)

### Flow

**Basic Flow** 

1. The guest user accesses the Contact form page.
2. Enters First Name, Last Name, and Email.
3. Selects a Subject from the dropdown.
4. Writes a Message.
5. (Optional) Uploads an attachment file.
6. Clicks the **Submit** button.
7. The system displays a success message: “Message sent successfully.”

**Alternate Flows**

* **2.a.** First Name or Last Name or Email is empty → Inline error on blur, submission blocked.
* **2.b.** First Name or Last Name or Email exceeds 120 characters → Field rejected and error message displayed.
* **2.c.** Email is in invalid format (e.g., missing "@", domain) → Error shown immediately.
* **3.a.** Subject is not changed from default value → Error on submit.
* **4.a.** Message is empty → Inline error shown when field is blurred.
* **4.b.** Message is shorter than 50 characters → Submit rejected with warning.
* **4.c.** Message is longer than 250 characters → Submit rejected with warning.
* **5.a.** File is uploaded with unsupported extension (e.g., `.exe`, `.docx`) → Upload blocked, error shown.
* **5.b.** File size exceeds 500KB → Upload blocked, error message shown.

### Scenario Table 

| Scenario ID | Scenario Name                           | Starting Flow | Alternate Flow |
| ---------------- | --------------------------------------- | ------------- | -------------- |
| SC-CON-01   | Guest submits valid contact form        | 1 → 7         | –              |
| SC-CON-02   | Unfulfilled prerequisites                     | Step 2        | 2.a            |
| SC-CON-03   | Email or Name exceeds 120 characters            | Step 2        | 2.b            |
| SC-CON-04   | Email is in invalid format              | Step 2        | 2.c            |
| SC-CON-05   | Subject is not selected from dropdown   | Step 3        | 3.a            |
| SC-CON-06   | Message field is empty                  | Step 4        | 4.a            |
| SC-CON-07   | Message is shorter than 50 characters   | Step 4        | 4.b            |
| SC-CON-08   | Message is longer than 250 characters   | Step 4        | 4.c            |
| SC-CON-09   | File uploaded has unsupported extension | Step 5        | 5.a            |
| SC-CON-10   | File uploaded exceeds 500KB             | Step 5        | 5.b            |

## Feature 2: Category Management (Admin)

### Flow – Add Category

**Basic Flow** 

1. In Category management Page, click button "Add Category".
2. Selects **Parent ID** (optional).
3. Enters **Name** (no more than 120 characters, unique).
4. Enters **Slug** (lowercase, URL-safe, unique).
5. Clicks the **Save** button.
6. System shows success message: “Category created successfully.”

**Alternate Flows**

* **3.a.** Name field is left empty → Inline error on blur, submit blocked.
* **3.b.** Name exceeds 120 characters → Validation error shown.
* **3.c.** Name is not unique (already exists) → Error: "Name already exists."
* **4.a.** Slug contains spaces, special characters → Error on submit.
* **4.b.** Slug field is empty → Submit blocked with error.
* **4.c.** Slug already exists in the database → Duplicate error shown.

### Flow – Edit Category

**Basic Flow** 

1. In Category Management page, click "Edit" on a category row.
2. Select Parent ID (optional).
3. Edit Name (required, no more than 120 chars, unique).
4. Edit Slug (required, lowercase, hyphenated, unique).
5. Click Save.
6. System displays success message: "Category updated successfully."

**Alternate Flows**

* **3.a.** Name field is empty → validation error.
* **3.b.** Name exceeds 120 characters → error shown.
* **3.c.** Name duplicates another category's name → error shown.
* **4.a.** Slug is empty → validation error.
* **4.b.** Slug contains spaces, special characters, or uppercase → format error.
* **4.c.** Slug already exists (conflicts with another category) → duplicate error.

### Flow – Search Category

**Basic Flow** 

1. In Category Management page, enter a keyword in the search bar.
2. System filters category list by name (partial match, case-insensitive).
3. Matching results are displayed.

**Alternate Flows**

* **1.a.** Keyword matches no categories → system shows empty list.
* **1.b.** Keyword field is left blank → system shows full category list.

### Flow – Delete Category

**Basic Flow** 

1. In Category Management page, click “Delete” on a category.
2. System deletes category and shows message: "Category deleted successfully."

**Alternate Flows**

* **1.a.** Category is parent of another category → error: "This category is used elsewhere."
* **1.b.** Category contains products → error: "This category contains products and cannot be deleted."

### Scenario Table

**Add category**

| Scenario ID | Scenario Name                                         | Starting Flow | Alternate Flow |
| ---------------- | ----------------------------------------------------- | ------------- | -------------- |
| SC-CAT-01   | Successfully add a new category                       | 1 → 6         | –              |
| SC-CAT-02   | Name field is left empty                              | Step 3        | 3.a            |
| SC-CAT-03   | Name exceeds 120 characters                   | Step 3        | 3.b            |
| SC-CAT-04   | Name is not unique                                    | Step 3        | 3.c            |
| SC-CAT-05   | Slug contains invalid characters  | Step 4        | 4.a            |
| SC-CAT-06   | Slug field is empty                                   | Step 4        | 4.b            |
| SC-CAT-07   | Slug already exists in the database                   | Step 4        | 4.c            |

**Edit category**

| Scenario ID    | Scenario Name                                 | Starting Flow | Alternate Flow |
| ---------------- | --------------------------------------------- | ------------- | -------------- |
| SC-CAT-EDIT-01 | Edit category successfully                    | 1 → 6         | –              |
| SC-CAT-EDIT-02 | Parent ID is same as category’s own ID        | Step 2        | 2.a            |
| SC-CAT-EDIT-03 | Name is empty                                 | Step 3        | 3.a            |
| SC-CAT-EDIT-04 | Name exceeds max length                       | Step 3        | 3.b            |
| SC-CAT-EDIT-05 | Name already exists                           | Step 3        | 3.c            |
| SC-CAT-EDIT-06 | Slug is empty                                 | Step 4        | 4.a            |
| SC-CAT-EDIT-07 | Slug is not URL-safe (e.g., spaces/uppercase) | Step 4        | 4.b            |
| SC-CAT-EDIT-08 | Slug already exists                           | Step 4        | 4.c            |

**Search category**

| Scenario ID      | Scenario Name                  | Starting Flow | Alternate Flow |
| ---------------- | ------------------------------ | ------------- | -------------- |
| SC-CAT-SEARCH-01 | Search with partial name match | 1 → 3         | –              |
| SC-CAT-SEARCH-02 | Search with no matching result | Step 1        | 1.a            |
| SC-CAT-SEARCH-03 | Search with empty keyword      | Step 1        | 1.b            |

**Delete Category**

| Scenario ID   | Scenario Name                                | Starting Flow | Alternate Flow |
| ------------- | -------------------------------------------- | ------------- | -------------- |
| SC-CAT-DEL-01 | Successfully delete a category               | 1 → 3         | –              |
| SC-CAT-DEL-02 | Category is being used as Parent             | Step 1        | 1.a            |
| SC-CAT-DEL-03 | Category contains products                   | Step 1        | 1.b            |

\pagebreak