from faker import Faker
import random
from datetime import datetime, timedelta
import csv

fake = Faker('en_US')

# Define meaningful tool categories
root_categories = [
    "Power Tools", "Hand Tools", "Garden Tools", "Measuring Tools", "Cutting Tools",
    "Storage Tools", "Automotive Tools", "Safety Equipment", "Electrical Tools", "Plumbing Tools",
    "Welding Tools", "Woodworking Tools", "Painting Supplies", "Cleaning Equipment", "Construction Tools"
]

# For each root category, define potential child categories
child_categories = {
    "Power Tools": ["Drills", "Saws", "Sanders", "Grinders", "Impact Wrenches", "Heat Guns", "Routers", "Planers"],
    "Hand Tools": ["Hammers", "Screwdrivers", "Wrenches", "Pliers", "Chisels", "Files", "Utility Knives", "Clamps"],
    "Garden Tools": ["Lawn Mowers", "Trimmers", "Pruners", "Shovels", "Rakes", "Hoses", "Sprinklers", "Wheelbarrows"],
    "Measuring Tools": ["Tape Measures", "Levels", "Calipers", "Squares", "Angle Finders", "Laser Measures", "Rulers"],
    "Cutting Tools": ["Saws", "Scissors", "Box Cutters", "Snips", "Bolt Cutters", "Pipe Cutters", "Glass Cutters"],
    "Storage Tools": ["Toolboxes", "Cabinets", "Shelving", "Cases", "Bags", "Organizers", "Hooks", "Bins"],
    "Automotive Tools": ["Socket Sets", "Car Jacks", "Battery Tools", "Oil Change Tools", "Tire Tools", "Diagnostic Tools"],
    "Safety Equipment": ["Gloves", "Safety Glasses", "Ear Protection", "Masks", "Helmets", "First Aid Kits", "Vests"],
    "Electrical Tools": ["Multimeters", "Wire Strippers", "Soldering Irons", "Voltage Testers", "Circuit Testers"],
    "Plumbing Tools": ["Pipe Wrenches", "Plungers", "Pipe Cutters", "Drain Snakes", "Pipe Benders", "Faucet Keys"],
    "Welding Tools": ["Welding Machines", "Welding Helmets", "Electrode Holders", "Welding Gloves", "Welding Clamps"],
    "Woodworking Tools": ["Chisels", "Planes", "Saws", "Wood Lathes", "Carving Tools", "Sanders", "Router Bits"],
    "Painting Supplies": ["Brushes", "Rollers", "Sprayers", "Drop Cloths", "Paint Mixers", "Trays", "Tape"],
    "Cleaning Equipment": ["Pressure Washers", "Vacuums", "Brooms", "Mops", "Buckets", "Scrubbers", "Dusters"],
    "Construction Tools": ["Concrete Tools", "Ladders", "Scaffolding", "Drywall Tools", "Flooring Tools", "Roofing Tools"]
}

# Extra child categories to ensure variety
additional_subcategories = [
    "Accessories", "Parts", "Kits", "Sets", "Professional", "DIY", "Compact", "Heavy Duty",
    "Cordless", "Corded", "Rechargeable", "Portable", "Bench Top", "Industrial", "Precision",
    "Home", "Workshop", "Garage", "Budget", "Premium", "Deluxe", "Basic", "Advanced", "Entry-Level",
    "Commercial", "Contractor", "Tradesman", "Essential", "Specialty", "Multi-Purpose", "All-Purpose",
    "Ergonomic", "Adjustable", "Folding", "Extendable", "Smart", "Digital", "Manual", "Automatic",
    "Hydraulic", "Pneumatic", "Electric", "Battery-Powered", "Handheld", "Wall-Mounted", "Stand-Alone"
]

# Add brand prefixes for more variety
brands = [
    "DeWalt", "Milwaukee", "Makita", "Bosch", "Stanley", "Craftsman", "Ryobi", "Black & Decker",
    "Ridgid", "Hilti", "Festool", "Dremel", "Porter-Cable", "Skil", "Snap-on", "Irwin",
    "Husky", "Klein", "Kobalt", "Metabo", "Hitachi", "Worx", "Tacklife", "Hart"
]

# How many parent and child categories to generate
NUM_ROOT = 15  # Use all root categories
NUM_CHILD = 485  # To get at least 500 total rows (15 root + 485 child = 500)

categories = []
next_id = 1

# Generate parent categories
for i in range(NUM_ROOT):
    name = root_categories[i]
    slug = name.lower().replace(' ', '-')
    created_at = fake.date_time_between(start_date='-2y', end_date='now')
    updated_at = created_at + timedelta(days=random.randint(0, 365))
    categories.append({
        "id": next_id,
        "parent_id": None,
        "name": name,
        "slug": slug,
        "created_at": created_at.strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": updated_at.strftime('%Y-%m-%d %H:%M:%S')
    })
    next_id += 1

# Generate child categories
for i in range(NUM_CHILD):
    # Select a random parent
    parent_index = random.randint(0, NUM_ROOT - 1)
    parent_id = parent_index + 1
    parent_name = root_categories[parent_index]
    
    # Get child categories for this parent
    potential_children = child_categories[parent_name].copy()
    
    # Create more variety for child categories with different combinations
    variation_type = random.randint(1, 5)
    
    # Make sure we have a child category to work with
    if not potential_children:
        # Fallback if the list is empty
        name = f"{fake.word().capitalize()} Tools"
    else:
        child_base = potential_children[random.randint(0, len(potential_children) - 1)]
        
        if variation_type == 1:
            # Simple child category
            name = child_base
        elif variation_type == 2:
            # Descriptor + child
            descriptor = additional_subcategories[random.randint(0, len(additional_subcategories) - 1)]
            name = f"{descriptor} {child_base}"
        elif variation_type == 3:
            # Brand + child
            brand = brands[random.randint(0, len(brands) - 1)]
            name = f"{brand} {child_base}"
        elif variation_type == 4:
            # Brand + descriptor + child
            brand = brands[random.randint(0, len(brands) - 1)]
            descriptor = additional_subcategories[random.randint(0, len(additional_subcategories) - 1)]
            name = f"{brand} {descriptor} {child_base}"
        else:
            # Descriptor + child + other descriptor
            descriptor1 = additional_subcategories[random.randint(0, len(additional_subcategories) - 1)]
            descriptor2 = random.choice(["Set", "Kit", "Collection", "Series", "Line", "Pack"])
            name = f"{descriptor1} {child_base} {descriptor2}"
    
    slug = name.lower().replace(' ', '-')
    created_at = fake.date_time_between(start_date='-2y', end_date='now')
    updated_at = created_at + timedelta(days=random.randint(0, 365))
    categories.append({
        "id": next_id,
        "parent_id": parent_id,
        "name": name,
        "slug": slug,
        "created_at": created_at.strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": updated_at.strftime('%Y-%m-%d %H:%M:%S')
    })
    next_id += 1

# Export the results to CSV
with open("categories.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["id", "parent_id", "name", "slug", "created_at", "updated_at"])
    writer.writeheader()
    for cat in categories:
        writer.writerow(cat)

print(f"Done! Generated {len(categories)} rows of meaningful tool shop categories saved to categories.csv")
