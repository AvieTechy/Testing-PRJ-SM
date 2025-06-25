import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

brands = pd.read_csv('brands.csv')
categories = pd.read_csv('categories.csv')

faker = Faker()

product_adjectives = [
    "Professional", "Heavy-Duty", "Industrial", "Premium", "Precision", "Advanced", 
    "Compact", "Ergonomic", "High-Performance", "Ultra-Light", "Durable", "Cordless",
    "Electric", "Hydraulic", "Pneumatic", "Automatic", "Manual", "Digital", "Smart",
    "Commercial-Grade", "Portable", "Adjustable", "Heavy-Gauge", "All-Purpose"
]

product_features = [
    "ergonomic handle for reduced fatigue", 
    "impact-resistant casing for durability",
    "quick-release mechanism for easy operation",
    "precision-engineered components for superior performance",
    "energy-efficient motor that saves on operating costs",
    "anti-slip grip for safer operation",
    "lightweight design for extended use without fatigue",
    "rust-resistant coating for longer tool life",
    "LED work light for improved visibility",
    "variable speed control for versatility",
    "advanced safety features for protection",
    "quick-charge battery system for minimal downtime",
    "modular design for easy maintenance and repair",
    "superior balance for improved control",
    "high-torque output for demanding applications",
    "reinforced structure for heavy-duty use",
    "precision calibration for accurate results",
    "integrated storage solution for accessories"
]

category_specific_names = {
    "Power Tools": ["Drill", "Saw", "Grinder", "Sander", "Impact Wrench", "Heat Gun", "Router", "Jigsaw", "Rotary Tool"],
    "Hand Tools": ["Hammer", "Screwdriver Set", "Wrench", "Pliers", "Socket Set", "Utility Knife", "Clamp", "Chisel"],
    "Garden Tools": ["Pruner", "Lawn Mower", "Hedge Trimmer", "Shovel", "Rake", "Garden Hose", "Sprinkler", "Wheelbarrow"],
    "Measuring Tools": ["Tape Measure", "Level", "Caliper", "Square", "Angle Finder", "Laser Measure", "Ruler"],
    "Cutting Tools": ["Utility Knife", "Scissors", "Saw Blade", "Circular Blade", "Hacksaw", "Bolt Cutter", "Tin Snips"],
    "Storage Tools": ["Tool Box", "Organizer", "Cabinet", "Mobile Cart", "Tool Belt", "Storage Bin", "Wall System"],
    "Automotive Tools": ["Socket Set", "Wrench Set", "Jack", "Battery Charger", "Diagnostic Tool", "Tire Inflator"],
    "Safety Equipment": ["Safety Glasses", "Work Gloves", "Ear Protection", "Dust Mask", "Hard Hat", "Safety Harness"],
    "Electrical Tools": ["Multimeter", "Wire Stripper", "Tester", "Soldering Iron", "Crimping Tool", "Voltage Detector"],
    "Plumbing Tools": ["Pipe Wrench", "Plunger", "Snake", "Pipe Cutter", "Crimper", "Plumbing Kit", "Threading Set"],
    "Welding Tools": ["Welding Machine", "Welding Mask", "Electrode Holder", "Welding Gloves", "Chipping Hammer"],
    "Woodworking Tools": ["Planer", "Jointer", "Router", "Lathe", "Band Saw", "Chisel Set", "Wood Carving Kit"],
    "Painting Supplies": ["Paint Sprayer", "Roller Set", "Paintbrush", "Tray", "Extension Pole", "Masking Tool"],
    "Cleaning Equipment": ["Pressure Washer", "Vacuum", "Steam Cleaner", "Brush Set", "Squeegee", "Mop System"],
    "Construction Tools": ["Demolition Hammer", "Concrete Mixer", "Nail Gun", "Air Compressor", "Jackhammer", "Tamper"]
}

tool_names = [
    # Hand Tools
    "Hammer", "Screwdriver", "Wrench", "Pliers", "Tape Measure", "Utility Knife",
    "Chisel", "Hex Key", "Handsaw", "Level", "Adjustable Wrench", "Ratchet",
    "Socket Wrench", "Pry Bar", "Clamp",

    # Power Tools
    "Electric Drill", "Cordless Screwdriver", "Angle Grinder", "Circular Saw",
    "Jigsaw", "Heat Gun", "Rotary Tool", "Sander", "Impact Driver", "Nail Gun",
    "Electric Soldering Iron", "Oscillating Tool", "Demolition Hammer",

    # Measuring & Testing Tools
    "Voltage Tester", "Multimeter", "Stud Finder", "Laser Level", "Caliper",
    "Torque Wrench", "Infrared Thermometer",

    # Specialized Tools
    "Pipe Cutter", "Wire Stripper", "Crimping Tool", "Hole Saw", "Tile Cutter",
    "Caulking Gun", "Rivet Gun", "Staple Gun", "Torque Screwdriver",
    "Oil Filter Wrench", "Spark Plug Wrench",

    # Miscellaneous
    "Tool Box", "Work Light", "Safety Goggles", "Dust Mask", "Work Gloves",
    "Step Ladder", "Extension Cord", "Portable Air Compressor"
]

def generate_products(n):
    products = []
    for i in range(1, n + 1):
        category_id = random.choice(categories['id'])
        category_row = categories.loc[categories['id'] == category_id].iloc[0]
        category_name = category_row['name']
        
        brand_id = random.choice(brands['id'])
        brand_name = brands.loc[brands['id'] == brand_id, 'name'].iloc[0]
        
        adjective = random.choice(product_adjectives)
        
        root_category = category_name.split(' - ')[0] if ' - ' in category_name else category_name
        if root_category in category_specific_names:
            tool_name = random.choice(category_specific_names[root_category])
        else:
            tool_name = random.choice(tool_names)
        
        name = f"{adjective} {tool_name}"
        
        model_number = f"{faker.random_uppercase_letter()}{random.randint(100, 999)}"
        name = f"{name} {model_number}"
        
        description = f"This {adjective.lower()} {tool_name.lower()} from {brand_name} is designed for professional and DIY enthusiasts alike. "
        
        selected_features = random.sample(product_features, random.randint(2, 3))
        description += f"Features include {', '.join(selected_features[:-1])} and {selected_features[-1]}. "
        
        description += f"Perfect for {random.choice(['home workshops', 'construction sites', 'professional settings', 'industrial applications', 'DIY projects'])}."
        
        created_at = faker.date_time_between(start_date='-1y', end_date='now')
        updated_at = created_at + timedelta(days=random.randint(0, 30))
        product = {
            "id": i,
            "name": name,
            "description": description,
            "stock": random.randint(0, 500),
            "price": round(random.uniform(10.0, 1000.0), 2),
            "is_location_offer": random.randint(0, 1),
            "is_rental": random.randint(0, 1),
            "brand_id": brand_id,
            "category_id": category_id,
            "product_image_id": random.randint(1, 500),
            "created_at": created_at.strftime('%Y-%m-%d %H:%M:%S'),
            "updated_at": updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        products.append(product)
    return products

product_data = generate_products(600)

df = pd.DataFrame(product_data)
df.to_csv("products.csv", index=False)
print("Done! Data saved to products.csv")
