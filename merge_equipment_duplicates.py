from pymongo import MongoClient
from collections import defaultdict
from datetime import datetime

MONGO_URI = "mongodb://localhost:27017/inventory_db"
client = MongoClient(MONGO_URI)
db = client.get_database()
equipment_col = db.equipment

def normalize_name(name):
    return str(name).strip().lower() if name else ''

groups = defaultdict(list)

# Fetch all equipment
for doc in equipment_col.find():
    norm_name = normalize_name(doc.get('name'))
    groups[norm_name].append(doc)

merged_count = 0
for norm_name, docs in groups.items():
    if not norm_name or len(docs) == 1:
        continue  # Skip empty names or already unique
    # Sum quantities
    total_quantity = 0
    for d in docs:
        try:
            qty = int(d.get('quantity', 1) or 1)
        except Exception:
            qty = 1
        total_quantity += qty
    # Use the most recent/complete doc as base
    docs_sorted = sorted(docs, key=lambda d: d.get('updated_at', d.get('created_at', datetime.min)), reverse=True)
    base = docs_sorted[0].copy()
    base['quantity'] = total_quantity
    # Remove all docs for this name
    ids = [d['_id'] for d in docs]
    equipment_col.delete_many({'_id': {'$in': ids}})
    # Insert merged doc
    equipment_col.insert_one(base)
    merged_count += len(docs) - 1
    print(f"Merged {len(docs)} items named '{base['name']}' into one with quantity {total_quantity}.")

print(f"Done. Merged {merged_count} duplicate equipment entries.") 