from faker import Faker
import random
import pandas as pd
from datetime import datetime, timedelta

fake = Faker('en_US')

# Constants
NUM_INVOICES = 500
NUM_USERS = 500

PAYMENT_METHODS = [
    'Bank Transfer',
    'Cash on Delivery',
    'Credit Card',
    'Buy Now Pay Later',
    'Gift Card'
]

STATUS_CHOICES = [
    'AWAITING_FULFILLMENT',
    'ON_HOLD',
    'AWAITING_SHIPMENT',
    'SHIPPED',
    'COMPLETED'
]
try:
    products_df = pd.read_csv('products.csv')
    products_available = True
    product_ids = products_df['id'].tolist()
    product_prices = dict(zip(products_df['id'], products_df['price']))
except FileNotFoundError:
    print("Warning: products.csv not found. Using random values for invoice items.")
    products_available = False
    product_ids = list(range(1, 601))  # Assume 600 products as in products.py
    product_prices = {pid: round(random.uniform(10.0, 1000.0), 2) for pid in product_ids}

invoices = []
invoice_items = []
item_id_counter = 1

for i in range(1, NUM_INVOICES + 1):
    user_id = random.randint(1, NUM_USERS)
    invoice_date = fake.date_time_between(start_date='-2y', end_date='now')
    invoice_number = f"INV{random.randint(100000,999999)}"
    billing_address = fake.street_address()
    billing_city = fake.city()
    billing_state = fake.state()
    billing_country = fake.country()
    billing_postcode = fake.postcode()
    
    # Generate between 1 and 5 items per invoice
    num_items = random.randint(1, 5)
    invoice_total = 0
    
    # Create invoice items
    for j in range(num_items):
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 5)
        unit_price = product_prices[product_id]
        item_total = round(quantity * unit_price, 2)
        invoice_total += item_total
        
        invoice_items.append({
            "id": item_id_counter,
            "invoice_id": i,
            "product_id": product_id,
            "unit_price": unit_price,
            "quantity": quantity,
            "created_at": invoice_date.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": invoice_date.strftime('%Y-%m-%d %H:%M:%S')
        })
        item_id_counter += 1
    
    payment_method = random.choice(PAYMENT_METHODS)
    payment_account_name = fake.name()
    payment_account_number = fake.bban()
    status = random.choice(STATUS_CHOICES)
    
    # Generate meaningful status messages based on status
    status_messages = {
        'AWAITING_FULFILLMENT': [
            f"Order #{invoice_number} is being processed by our team.",
            f"Your order is currently being processed in our system.",
            f"We've received your order and are preparing it for shipment.",
            f"Order received on {invoice_date.strftime('%Y-%m-%d')} is being prepared.",
            f"Your payment has been confirmed, order is being processed."
        ],
        'ON_HOLD': [
            f"Order #{invoice_number} is on hold pending payment verification.",
            f"Additional verification needed before processing your order.",
            f"We're waiting for stock replenishment for items in your order.",
            f"Order placed on hold due to payment authorization issues.",
            f"Please contact customer service regarding your order status."
        ],
        'AWAITING_SHIPMENT': [
            f"Order #{invoice_number} has been packed and is awaiting pickup by carrier.",
            f"Your order has been processed and will ship soon.",
            f"Shipping label has been created, awaiting carrier pickup.",
            f"Your order is in the final stage before shipment.",
            f"Order is scheduled for shipment within the next business day."
        ],
        'SHIPPED': [
            f"Order #{invoice_number} has been shipped via {random.choice(['USPS', 'UPS', 'FedEx', 'DHL'])}.",
            f"Your package is on the way! Expected delivery in {random.randint(1, 7)} days.",
            f"Order shipped on {(invoice_date + timedelta(days=random.randint(1, 3))).strftime('%Y-%m-%d')}.",
            f"Your items are on their way to {billing_city}, {billing_state}.",
            f"Shipment in transit to your delivery address."
        ],
        'COMPLETED': [
            f"Order #{invoice_number} has been delivered successfully.",
            f"Your order was delivered on {(invoice_date + timedelta(days=random.randint(3, 10))).strftime('%Y-%m-%d')}.",
            f"Thank you for your purchase! Your order is now complete.",
            f"Order delivered to {billing_address}, {billing_city}, {billing_state}.",
            f"Your order has been completed. We hope you enjoy your purchase!"
        ]
    }
    
    # Select a random appropriate message based on status
    status_message = random.choice(status_messages[status])
    created_at = invoice_date
    updated_at = created_at + timedelta(days=random.randint(0, 60))
    
    invoices.append({
        "id": i,
        "user_id": user_id,
        "invoice_date": invoice_date.strftime('%Y-%m-%d %H:%M:%S'),
        "invoice_number": invoice_number,
        "billing_address": billing_address,
        "billing_city": billing_city,
        "billing_state": billing_state,
        "billing_country": billing_country,
        "billing_postcode": billing_postcode,
        "total": invoice_total,
        "payment_method": payment_method,
        "payment_account_name": payment_account_name,
        "payment_account_number": payment_account_number,
        "status": status,
        "status_message": status_message,
        "created_at": created_at.strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": updated_at.strftime('%Y-%m-%d %H:%M:%S')
    })

# Export invoice items to CSV
import csv

# Export invoices to CSV
with open("invoices.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = [
        "id", "user_id", "invoice_date", "invoice_number", "billing_address", "billing_city",
        "billing_state", "billing_country", "billing_postcode", "total", "payment_method",
        "payment_account_name", "payment_account_number", "status", "status_message",
        "created_at", "updated_at"
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for inv in invoices:
        writer.writerow(inv)

# Export invoice items to CSV
with open("invoice_items.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = [
        "id", "invoice_id", "product_id", "unit_price", "quantity",
        "created_at", "updated_at"
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in invoice_items:
        writer.writerow(item)

print("Done! Data saved to invoices.csv and invoice_items.csv")