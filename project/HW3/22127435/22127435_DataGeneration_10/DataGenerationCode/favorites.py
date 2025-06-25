from faker import Faker
import random
from datetime import timedelta
import pandas as pd

fake = Faker('en_US')

NUM_FAVORITES = 600
NUM_USERS = 500     
NUM_PRODUCTS = 600   

favorites = []
generated_pairs = set() 

while len(favorites) < NUM_FAVORITES:
    user_id = random.randint(1, NUM_USERS)
    product_id = random.randint(1, NUM_PRODUCTS)

    if (user_id, product_id) in generated_pairs:
        continue 

    generated_pairs.add((user_id, product_id))
    
    created_at = fake.date_time_between(start_date='-2y', end_date='now')
    updated_at = created_at + timedelta(days=random.randint(0, 300))
    
    favorites.append({
        "id": len(favorites) + 1, 
        "user_id": user_id,
        "product_id": product_id,
        "created_at": created_at.strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": updated_at.strftime('%Y-%m-%d %H:%M:%S')
    })

df = pd.DataFrame(favorites)
df.to_csv("favorites.csv", index=False, encoding="utf-8")

print("Done! Data saved to favorites.csv")