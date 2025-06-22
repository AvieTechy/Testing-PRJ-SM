# Data Generation

## Data tables and ranges of rules

To ensure that the generated data is valid and usable in the system, all field rules were derived from three main sources:

* **Laravel migration files** were used to determine the technical constraints of each field, such as data type, maximum length, nullability, and uniqueness.

* **The user interface (UI)** provided insights into how fields are used in practice. Some constraints, like the `subject` field in the `contact_requests` table appear as a dropdown in the UI. This indicates a predefined set of values (an implicit enum) that should be respected during data generation.

* **Business rules and domain knowledge** were applied to define logical ranges and relationships between fields. Similarly, `updated_at` was always generated to be equal to or later than `created_at` to maintain timestamp consistency.

### Table `Users`

| Field Name                 | Type                  | Rule for Valid Data Generation                  |
| ---------------------------- | ------------------- | ----------------------------------------------- |
| `first_name`               | string(40)            | Common given names ($\leq$ 40 characters)            |
| `last_name`                | string(20)            | Common surnames ($\leq$ 20 characters)               |
| `address`                  | string(70)            | Short full addresses ($\leq$ 70 characters)          |
| `city`                     | string(40)            | Real cities ($\leq$ 40 characters)                   |
| `state`                    | string(40)  | Optional; can be blank or a valid state name    |
| `country`                  | string(40)            | One of: "Vietnam", "USA", "UK", etc.            |
| `postcode`                 | string(10)  | Optional; 5–6 digit ZIP/postal code or blank    |
| `phone`                    | string(24)  | Optional; numeric string 9–11 digits, or blank  |
| `dob`                      | date                  | Between 1960–2010 (age 15–65)                   |
| `email`                    | string(60), unique    | Unique email, valid format, $\leq$ 60 characters     |
| `password`                 | string      | Optional; alphanumeric or hashed string         |
| `role`                     | string                | One of: `"customer"`, `"admin"`                 |
| `enabled`                  | boolean, default true | Either `true` or `false`                        |
| `failed_login_attempts`    | integer, default 0    | Integer $\geq$ 0                                     |
| `created_at`, `updated_at` | timestamps            | ISO timestamp format, updated\_at $\geq$ created\_at |

\pagebreak

### Table `Contact Requests`

| Field Name                 | Type                         | Rule for Valid Data Generation                                   |
| ---------------------------- | -------------------------- | ---------------------------------------------------------------- |
| `user_id`                  | unsignedBigInteger | Optional; match an existing user ID or leave null                |
| `name`                     | string(60)         | Optional; full name, $\leq$ 60 chars or leave blank                   |
| `email`                    | string(60)         | Optional; valid format or blank                                  |
| `subject`                  | string(120)                  | Short, meaningful topic like “Customer service” ($\leq$ 120 characters) |
| `message`                  | string(250)                  | Realistic sentence or complaint text ($\leq$ 250 characters)          |
| `status`                   | enum                         | One of: `"NEW"`, `"IN_PROGRESS"`, `"RESOLVED"`                   |
| `created_at`, `updated_at` | timestamps                   | ISO timestamps, updated\_at $\geq$ created\_at                        |

## Data Generation Tools and Process

To ensure that the generated data was both valid and meaningful, I adopted a semi-automated approach combining AI-assisted data synthesis and structured Python scripting.

### Tools Used

**1. ChatGPT**

Used to synthesize realistic datasets and enrich semantic quality for two key areas:

- **Address-related fields:** (`address`, `city`, `state`, `country`, `postcode`)
- **Contact topics:** Semantic pairs of `subject` and relevant `message` content.

Generated datasets were saved into `.txt` files and then read during the data generation step.

**2. Python (Faker library)**

Main logic for data generation, combining:

- Field-by-field rule application based on migration and UI constraints.

- Controlled randomness (with seeds) to ensure reproducibility.

Manual .txt data sources:

- `subject_message_data.txt` (gened by ChatGPT): Stored 500+ realistic subject–message pairs generated via ChatGPT prompts based on the actual dropdown items seen in the UI.

- `address_data.txt` (gened by ChatGPT): Contained pre-aligned synthetic address entries, also AI-generated, ensuring compatibility between related location fields.

### Generation Process

**1. Generate Address Data with ChatGPT**

**Prompt Used for Address Data:**

```plaintext
Generate a file .txt contains at least 500 realistic and 
human-like full address lines for testing purposes.

Each line must include:
- Address
- City
- State
- Country
- Postcode (valid in the selected country)

Requirements:
- All components (address, city, state, country, postal code) 
must match each other geographically and logically.
- Do not mix locations across countries (e.g., do not put a 
UK postal code in a US city).
- All lines should be unique and vary across multiple cities 
and countries.

Format (one line per address):
[address], [city], [state], [country], [postal code]

Example:
123 Maple Street, Springfield, Illinois, USA, 62704
14 King Street, London, England, UK, SW1A 1AA

```

![File `address_data.txt`](images/address.png){ height=200px }

**2. Generate Contact Message Data with ChatGPT**

**Prompt Used for Subject–Message Pairs:**

```plaintext
Generate a .txt file contains 500 contact request subject–message
pairs for a customer/admin support system.

Each subject must be selected from the following list:
- Customer service  
- Webmaster  
- Return  
- Error 101: Subject not found  
- Payments  
- Warranty  
- Status of my order  
- Error 202: Translation error  

For each pair:
- Use the subject exactly as written (case-sensitive).
- Write a realistic message (1–3 sentences, not more than 250 
characters) that logically relates to the subject.
- Ensure the message sounds like something a real user might 
write in a contact form.

Format:
[subject]: [message]

Example:
Payments: I made a payment two days ago but it's not showing 
in my order history.

```

![File `subject_message_data.txt`](images/contact_message.png){ height=200px }

**3. Implement Custom Generator in Jupyter Notebook**

A custom `.ipynb` script generates 500 rows for both `users` and `contact_requests` tables. The process followed these key steps:

- **Step 1:** Read `address_data.txt` and split each line into components: address, city, state, country, and postcode.
- **Step 2:** Read `subject_message_data.txt` and split into paired fields: subject and corresponding message.
- **Step 3:** For each record (iteration 1 to 500):
  - Randomly choose an address line and decompose into fields.
  - Generate realistic user data using `faker` (first name, last name, phone, email, date of birth).
  - Randomly assign optional fields as blank/null based on nullability.
  - Ensure logical constraints, such as:
    - `updated_at` greater than `created_at`
    - `dob` between 1960 and 2010
    - unique emails
- **Step 4:** For contact requests:
  - Randomly choose an existing user ID.
  - Randomly assign subject–message pairs from the dataset.
  - Randomly assign one of the valid `status` enum values: `"NEW"`, `"IN_PROGRESS"`, `"RESOLVED"`

All timestamps are generated using `faker.date_time_this_decade()` to ensure recent but valid ISO timestamp formats.

**4. Output and Export**

At the end of the process:

- All generated data was structured into two `pandas.DataFrame`s.
- The entire dataset was exported into a single Excel file contains two sheets: `users` and `contact_requests`.

\pagebreak

### Sample Data

1. Table `Users`

![Users Sheet](./images/user.png)

2. Table `Contact Requests`

![Contact Requests Sheet](./images/contact_request.png)


\pagebreak
