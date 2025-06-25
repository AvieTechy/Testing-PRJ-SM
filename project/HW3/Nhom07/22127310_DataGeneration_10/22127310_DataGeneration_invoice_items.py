from faker import Faker
import random
import pandas as pd
from datetime import datetime, timedelta
import csv

# Initialize faker
fake = Faker('en_US')

# Constants
NUM_INVOICES = 500  # Maximum invoice_id
NUM_INVOICE_ITEMS = 2000  # How many invoice items to generate

# Load products data
try:
    products_df = pd.read_csv('products.csv')
    products_available = True
    product_ids = products_df['id'].tolist()
    product_prices = dict(zip(products_df['id'], products_df['price']))
    print(f"Loaded {len(product_ids)} products from products.csv")
except FileNotFoundError:
    print("Warning: products.csv not found. Using random values for invoice items.")
    products_available = False
    product_ids = list(range(1, 601))  # Assume 600 products as in products.py
    product_prices = {pid: round(random.uniform(10.0, 1000.0), 2) for pid in product_ids}

# Generate invoice items
invoice_items = []
item_id = 1

for i in range(1, NUM_INVOICE_ITEMS + 1):
    # Generate an invoice_id between 1 and NUM_INVOICES
    invoice_id = random.randint(1, NUM_INVOICES)
    
    # Random product
    product_id = random.choice(product_ids)
    
    # Generate realistic quantity (1-10 items)
    quantity = random.randint(1, 10)
    
    # Get unit price from products data or random if not available
    unit_price = product_prices[product_id]
    
    # Generate timestamps
    created_at = fake.date_time_between(start_date='-2y', end_date='now')
    
    # Decide update pattern: 
    # - 70% chance: minor update (minutes to hours later)
    # - 30% chance: major update (days later)
    # All items will have updated_at strictly after created_at
    
    update_pattern = random.random()
    
    if update_pattern < 0.70:
        # Minor update (minutes to hours)
        updated_at = created_at + timedelta(
            minutes=random.randint(1, 360)  # 1 minute to 6 hours
        )
    else:
        # Major update (days)
        updated_at = created_at + timedelta(days=random.randint(1, 30))
    
    invoice_items.append({
        "id": i,
        "invoice_id": invoice_id,
        "product_id": product_id,
        "unit_price": unit_price,
        "quantity": quantity,
        "created_at": created_at.strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": updated_at.strftime('%Y-%m-%d %H:%M:%S')
    })

# Export to CSV
with open("invoice_items.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = [
        "id", "invoice_id", "product_id", "unit_price", "quantity", 
        "created_at", "updated_at"
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in invoice_items:
        writer.writerow(item)

print(f"Done! Generated {NUM_INVOICE_ITEMS} invoice items saved to invoice_items.csv")
