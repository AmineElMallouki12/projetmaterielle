import pandas as pd
from pymongo import MongoClient

# Load Excel file
excel_path = 'NV INVENTAIRE.xlsx'
df = pd.read_excel(excel_path)

client = MongoClient("mongodb://localhost:27017/")
db = client["inventory_db"]
equipment = db.equipment

def safe_str(val):
    return str(val).strip().lower() if val is not None else ''

added = 0
skipped = 0
for _, row in df.iterrows():
    key = {
        'designation': safe_str(row.get('designation', row.get('Désignation', ''))),
        'marque': safe_str(row.get('marque', row.get('Marque', ''))),
        'modele': safe_str(row.get('modele', row.get('Modèle', ''))),
        'n_serie': safe_str(row.get('n_serie', row.get('N° Série', ''))),
        'ancien_cab': safe_str(row.get('ancien_cab', row.get('Ancien CAB', ''))),
        'nouveau_cab': safe_str(row.get('nouveau_cab', row.get('Nouveau CAB', ''))),
        'description': safe_str(row.get('description', row.get('Description / Observation', ''))),
        'status': safe_str(row.get('status', row.get('Statut', ''))),
        'condition': safe_str(row.get('letat', ''))
    }
    # Check if item exists
    exists = equipment.find_one(key)
    if not exists:
        doc = {
            'designation': row.get('designation', row.get('Désignation', '')),
            'marque': row.get('marque', row.get('Marque', '')),
            'modele': row.get('modele', row.get('Modèle', '')),
            'n_serie': row.get('n_serie', row.get('N° Série', '')),
            'ancien_cab': row.get('ancien_cab', row.get('Ancien CAB', '')),
            'nouveau_cab': row.get('nouveau_cab', row.get('Nouveau CAB', '')),
            'description': row.get('description', row.get('Description / Observation', '')),
            'status': row.get('status', row.get('Statut', '')),
            'condition': row.get('letat', ''),
            'quantity': int(row.get('quantity', row.get('Quantité', 1))),
            'date_inv': str(row.get('date_inv', row.get('Date d’inventaire', ''))),
        }
        equipment.insert_one(doc)
        added += 1
    else:
        skipped += 1

print(f"Added {added} new items. Skipped {skipped} existing items.") 