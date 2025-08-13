from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["inventory_db"]
equipment = db.equipment

# Step 1: Fetch all equipment
all_items = list(equipment.find())

# Step 2: Group by all relevant fields
from collections import defaultdict

def safe_str(val):
    return str(val).strip().lower() if val is not None else ''

groups = defaultdict(list)
for item in all_items:
    key = (
        safe_str(item.get('designation')),
        safe_str(item.get('marque')),
        safe_str(item.get('modele')),
        safe_str(item.get('n_serie')),
        safe_str(item.get('ancien_cab')),
        safe_str(item.get('nouveau_cab')),
        safe_str(item.get('description')),
        safe_str(item.get('status')),
    )
    groups[key].append(item)

# Step 3: For each group, merge quantities and keep one
merged_count = 0
for group_items in groups.values():
    if len(group_items) > 1:
        # Sum quantities (default to 1 if missing)
        total_quantity = sum(int(i.get('quantity', 1)) for i in group_items)
        # Keep the first item, update its quantity
        main_id = group_items[0]['_id']
        equipment.update_one({'_id': main_id}, {'$set': {'quantity': total_quantity}})
        # Remove the rest
        for dup in group_items[1:]:
            equipment.delete_one({'_id': dup['_id']})
        merged_count += 1

print(f"Merged {merged_count} equipment groups.") 