from faker import Faker
import pandas as pd
import random

fake = Faker()
data = {
    'id': range(1, 501),
    'product_id': [random.randint(1, 200) for _ in range(500)],
    'name': [f"{random.choice(['hammer', 'saw', 'drill'])}_image.jpg" for _ in range(500)],
    'by_user': [random.choice(["admin", "user1", "user2"]) for _ in range(500)],
    'source': [random.choice(["website", "upload", "external"]) for _ in range(500)],
    'file_name': [f"prod_{i:03d}_{random.choice(['hammer', 'saw', 'drill'])}.jpg" for i in range(1, 501)],
    'title': [f"Hình {random.choice(['búa', 'cưa', 'khoan'])}" for _ in range(500)],
    'created_at': [fake.date_time_between(start_date="-1y", end_date="now") for _ in range(500)],
    'updated_at': [fake.date_time_between(start_date="-1y", end_date="now") for _ in range(500)]
}
df_images = pd.DataFrame(data)
df_images.to_excel('product_images.xlsx', index=False)