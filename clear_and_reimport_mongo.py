import pandas as pd
import os
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

def clear_all_items():
    """Remove all items from MongoDB"""
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['inventory_db']
        collection = db['equipment']
        
        # Delete all items
        result = collection.delete_many({})
        print(f"✓ Removed {result.deleted_count} items from the database")
        
        client.close()
        
    except Exception as e:
        print(f"❌ Error clearing items: {e}")

def reimport_items():
    """Re-import all items from the Excel file"""
    excel_file = 'NV INVENTAIRE.xlsx'
    
    if not os.path.exists(excel_file):
        print(f"❌ Excel file '{excel_file}' not found!")
        return
    
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file)
        print(f"✓ Loaded {len(df)} items from Excel file")
        
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['inventory_db']
        collection = db['equipment']
        
        items_added = 0
        
        for index, row in df.iterrows():
            try:
                # Handle NaN values by converting to None
                designation = str(row['DESIGNATION']) if pd.notna(row['DESIGNATION']) else ''
                marque = str(row['MARQUE']) if pd.notna(row['MARQUE']) else ''
                modele = str(row['MODELE']) if pd.notna(row['MODELE']) else ''
                numero_serie = str(row['N° Série']) if pd.notna(row['N° Série']) else ''
                ancien_cab = str(row['ANCIEN CAB']) if pd.notna(row['ANCIEN CAB']) else ''
                nouveau_cab = str(row['NOUVEAU CAB']) if pd.notna(row['NOUVEAU CAB']) else ''
                etat = str(row['ETAT']) if pd.notna(row['ETAT']) else ''
                date_inventaire = str(row['DATE_INV']) if pd.notna(row['DATE_INV']) else ''
                
                # Combine Description and Observation
                description = ''
                if pd.notna(row['Description']):
                    description += str(row['Description'])
                if pd.notna(row['OBSERVATION']):
                    if description:
                        description += ' - '
                    description += str(row['OBSERVATION'])
                
                # Default values
                quantite = 1
                statut = 'Disponible'
                
                # Create the item document
                item_doc = {
                    'id': f"ITEM_{index + 1:04d}",
                    'designation': designation,
                    'marque': marque,
                    'modele': modele,
                    'n_serie': numero_serie,
                    'ancien_cab': ancien_cab,
                    'nouveau_cab': nouveau_cab,
                    'status': statut,
                    'date_inv': date_inventaire,
                    'description': description,
                    'quantite_totale': 1,
                    'quantite_cassée': 0,
                    'quantite_en_réparation': 0,
                    'quantite_disponible': 1,
                    'image': None,  # No image for imported items
                    'created_at': datetime.now(),
                    'updated_at': datetime.now()
                }
                
                collection.insert_one(item_doc)
                items_added += 1
                
            except Exception as e:
                print(f"❌ Error importing row {index + 1}: {e}")
                continue
        
        print(f"✓ Successfully imported {items_added} items")
        client.close()
        
    except Exception as e:
        print(f"❌ Error during import: {e}")

def main():
    print("🔄 Starting complete MongoDB reset and re-import...")
    print()
    
    # Step 1: Clear all items
    print("Step 1: Clearing all items from MongoDB...")
    clear_all_items()
    print()
    
    # Step 2: Re-import items
    print("Step 2: Re-importing items from Excel file...")
    reimport_items()
    print()
    
    print("✅ Database reset and re-import completed!")
    print("You can now refresh your web application to see the clean data.")

if __name__ == "__main__":
    main() 