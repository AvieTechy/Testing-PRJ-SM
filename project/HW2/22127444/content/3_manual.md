# Manual Test Cases

## Feature 1: Contact – Test Cases

1. Test case 1

- **Test Case ID**: `TC_CONTACT_01`
- **Title**: Submit contact form as logged-in user with valid data
- **Preconditions**: User is logged in
- **Inputs**:

  - Subject: "Feedback"
  - Message: 100-character valid text
  - Attachment: `sample.pdf` (400KB)
- **Test Steps**:

  1. Select a valid subject
  2. Enter a message of 100 characters
  3. Attach a `.pdf` file (400KB)
  4. Click "Submit"
- **Expected Result**: Form submitted successfully with a confirmation message
- **Type**: EP

2. Test Case 2

- **Test Case ID**: `TC_CONTACT_02`
- **Title**: Submit form as guest with invalid email
- **Preconditions**: User is not logged in
- **Inputs**:

  - Email: `invalidemail`
  - First Name: "John"
  - Last Name: "Doe"
  - Message: Valid message
- **Test Steps**:

  1. Enter invalid email
  2. Fill in other fields
  3. Click "Submit"
- **Expected Result**: Validation error for email format
- **Type**: EP

3. Test Case 3

- **Test Case ID**: `TC_CONTACT_03`
- **Title**: Check lower boundary for message length
- **Preconditions**: User is logged in
- **Inputs**:

  - Message: 50 characters
- **Test Steps**:

  1. Enter exactly 50 characters into the message field
  2. Click "Submit"
- **Expected Result**: Form is accepted
- **Type**: BVA

4. Test Case 4

- **Test Case ID**: `TC_CONTACT_04`
- **Title**: Upload oversized attachment
- **Preconditions**: User is logged in
- **Inputs**:

  - Attachment: `file.exe` (600KB)
- **Test Steps**:

  1. Attach an `.exe` file larger than 500KB
  2. Click "Submit"
- **Expected Result**: File type and size error message is shown
- **Type**: EP

## Feature 2: Category Management – Test Cases

1. Test Case 1

- **Test Case ID**: `TC_CATEGORY_01`
- **Title**: Add new root category with valid data
- **Preconditions**: Admin is logged in
- **Inputs**:

  - Name: "Cutting Tools"
  - Slug: `cutting-tools`
  - Parent ID: empty
- **Test Steps**:

  1. Enter category name
  2. Enter a valid slug
  3. Leave Parent ID empty
  4. Click "Save"
- **Expected Result**: New root category is created successfully
- **Type**: EP

2. Test Case 2

- **Test Case ID**: `TC_CATEGORY_02`
- **Title**: Add category with duplicate slug
- **Preconditions**: A category with slug `hammer` already exists
- **Inputs**:

  - Name: "Hammer 2"
  - Slug: `hammer`
- **Test Steps**:

  1. Enter category name
  2. Enter duplicate slug
  3. Click "Save"
- **Expected Result**: Error message for duplicate slug is shown
- **Type**: EP

3. Test Case 3

- **Test Case ID**: `TC_CATEGORY_03`
- **Title**: Edit category with own ID as parent
- **Preconditions**: Category with ID = 5 exists
- **Inputs**:

  - Parent ID: 5 (same as the category being edited)
- **Test Steps**:

  1. Select category to edit
  2. Set its own ID as parent
  3. Click "Save"
- **Expected Result**: Validation error for circular reference
- **Type**: EP

4. Test Case 4

- **Test Case ID**: `TC_CATEGORY_04`
- **Title**: Enter category name with 121 characters
- **Preconditions**: Admin is on Add Category form
- **Inputs**:

  - Name: 121-character string
- **Test Steps**:

  1. Enter 121-character category name
  2. Click "Save"
- **Expected Result**: Validation error for exceeding max length
- **Type**: BVA

