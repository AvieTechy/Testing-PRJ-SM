from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()
data = {
    'id': range(1, 501),
    'tokenable_id': [random.randint(1, 100) for _ in range(500)],
    'tokenable_type': [random.choice(["App\\User", "App\\Admin"]) for _ in range(500)],
    'name': [f"Token #{i}" for i in range(1, 501)],
    'token': [fake.uuid4()[:64] for _ in range(500)],  # Chuỗi ngẫu nhiên 64 ký tự
    'abilities': [random.choice(["read", "write", "read,write"]) for _ in range(500)],
    'last_used_at': [fake.date_time_between(start_date="-1y", end_date="now") if random.choice([True, False]) else None for _ in range(500)],
    'expires_at': [fake.date_time_between(start_date="+1d", end_date="+1y") if random.choice([True, False]) else None for _ in range(500)],
    'created_at': [fake.date_time_between(start_date="-1y", end_date="now") for _ in range(500)],
    'updated_at': [fake.date_time_between(start_date="-1y", end_date="now") for _ in range(500)]
}
df_tokens = pd.DataFrame(data)
df_tokens.to_excel('personal_access_tokens.xlsx', index=False)