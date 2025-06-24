from faker import Faker
import random
from datetime import timedelta

fake = Faker('en_US')

NUM_BRANDS = 500  # Generating at least 500 brands

# Seed data to diversify brand names
industry_words = [
    "Tools", "Hardware", "Equipment", "Supplies", "Machinery", "Tech", "Industrial", 
    "Manufacturing", "Engineering", "Products", "Solutions", "Innovations", "Systems",
    "Materials", "Devices", "Instruments", "Components", "Mechanics", "Builders"
]

# Lists to help create more unique brand names when we exhaust Faker's unique companies
descriptive_words = [
    "Advanced", "Premier", "Elite", "Professional", "Superior", "Ultimate", "Master",
    "Precision", "Reliable", "Quality", "Durable", "Innovative", "Trusted", "Expert",
    "Dynamic", "Robust", "Heavy-Duty", "Industrial", "Performance", "Smart", "Technical",
    "Global", "National", "International", "Universal", "Prime", "Classic", "Modern"
]

formats = [
    "{first_name} {industry}", 
    "{last_name} {industry}",
    "{descriptive} {industry}",
    "{first_name} & {last_name} {industry}",
    "{first_name} {last_name} {industry}",
    "{descriptive} {last_name} {industry}",
    "{last_name} {descriptive} {industry}",
    "The {last_name} {industry} Co.",
    "{descriptive} {industry} Group",
    "{last_name} Brothers {industry}",
    "{first_letter}{last_letter} {industry}"
]

brands = []

# Try to get unique companies from Faker first
for i in range(1, NUM_BRANDS + 1):
    try:
        if i <= 200:  # Use Faker's unique company for first 200
            name = fake.unique.company()
        else:
            # For the rest, create custom brand names
            format_choice = random.choice(formats)
            name = format_choice.format(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                industry=random.choice(industry_words),
                descriptive=random.choice(descriptive_words),
                first_letter=fake.first_name()[0],
                last_letter=fake.last_name()[0]
            )
            
            # Add LLC, Inc, Group randomly to some names
            if random.random() < 0.3:
                suffix = random.choice([" LLC", " Inc.", " Corp.", " Co.", " Group", " Industries", " International"])
                name += suffix
                
    except Exception:
        # If we run out of unique companies, create a custom one
        name = f"{fake.last_name()} {random.choice(industry_words)} {random.randint(1, 999)}"
    
    # slug: convert name to lowercase, replace spaces with hyphens, remove special characters
    slug = name.lower().replace(' ', '-').replace(',', '').replace('.', '').replace('&', 'and')
    created_at = fake.date_time_between(start_date='-3y', end_date='now')
    updated_at = created_at + timedelta(days=random.randint(0, 1000))
    brands.append({
        "id": i,
        "name": name,
        "slug": slug,
        "created_at": created_at.strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": updated_at.strftime('%Y-%m-%d %H:%M:%S')
    })

# Xuất ra file CSV
import csv

with open("brands.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["id", "name", "slug", "created_at", "updated_at"])
    writer.writeheader()
    for b in brands:
        writer.writerow(b)

print("Done! Data saved to brands.csv")