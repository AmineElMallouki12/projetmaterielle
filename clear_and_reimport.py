import sqlite3
import pandas as pd
import os
from datetime import datetime

def clear_all_items():
    """Remove all items from the database"""
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    try:
        # Delete all items
        cursor.execute("DELETE FROM items")
        conn.commit()
        print("✓ All items have been removed from the database")
        
        # Reset the auto-increment counter
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='items'")
        conn.commit()
        print("✓ Database counter has been reset")
        
    except Exception as e:
        print(f"❌ Error clearing items: {e}")
        conn.rollback()
    finally:
        conn.close()

def reimport_items():
    """Re-import all items from the Excel file"""
    excel_file = 'inventory_data.xlsx'
    
    if not os.path.exists(excel_file):
        print(f"❌ Excel file '{excel_file}' not found!")
        return
    
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file)
        print(f"✓ Loaded {len(df)} items from Excel file")
        
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        
        # Prepare the insert statement
        insert_query = """
        INSERT INTO items (
            designation, marque, modele, numero_serie, 
            ancien_cab, nouveau_cab, etat, date_inventaire, 
            description, quantite, statut, image_path
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        items_added = 0
        
        for index, row in df.iterrows():
            try:
                # Handle NaN values by converting to None
                designation = str(row['Désignation']) if pd.notna(row['Désignation']) else ''
                marque = str(row['Marque']) if pd.notna(row['Marque']) else ''
                modele = str(row['Modèle']) if pd.notna(row['Modèle']) else ''
                numero_serie = str(row['N° Série']) if pd.notna(row['N° Série']) else ''
                ancien_cab = str(row['Ancien CAB']) if pd.notna(row['Ancien CAB']) else ''
                nouveau_cab = str(row['Nouveau CAB']) if pd.notna(row['Nouveau CAB']) else ''
                etat = str(row['État']) if pd.notna(row['État']) else ''
                date_inventaire = str(row['Date d\'inventaire']) if pd.notna(row['Date d\'inventaire']) else ''
                description = str(row['Description / Observation']) if pd.notna(row['Description / Observation']) else ''
                quantite = int(row['Quantité']) if pd.notna(row['Quantité']) else 1
                statut = str(row['Statut']) if pd.notna(row['Statut']) else 'Disponible'
                image_path = None  # No image for imported items
                
                cursor.execute(insert_query, (
                    designation, marque, modele, numero_serie,
                    ancien_cab, nouveau_cab, etat, date_inventaire,
                    description, quantite, statut, image_path
                ))
                items_added += 1
                
            except Exception as e:
                print(f"❌ Error importing row {index + 1}: {e}")
                continue
        
        conn.commit()
        print(f"✓ Successfully imported {items_added} items")
        
    except Exception as e:
        print(f"❌ Error during import: {e}")
        conn.rollback()
    finally:
        conn.close()

def main():
    print("🔄 Starting complete database reset and re-import...")
    print()
    
    # Step 1: Clear all items
    print("Step 1: Clearing all items from database...")
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