from pymongo import MongoClient
from datetime import datetime

def fix_quantities():
    """Fix quantity fields for all existing items"""
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['inventory_db']
        collection = db['equipment']
        
        print("🔧 Fixing quantity fields for all items...")
        print("=" * 50)
        
        # Get all equipment
        all_equipment = list(collection.find())
        
        updated_count = 0
        
        for item in all_equipment:
            item_id = item['_id']
            
            # Set default quantities if they don't exist
            update_fields = {}
            
            if 'quantite_totale' not in item:
                update_fields['quantite_totale'] = 1
            
            if 'quantite_disponible' not in item:
                update_fields['quantite_disponible'] = 1
            
            if 'quantite_cassée' not in item:
                update_fields['quantite_cassée'] = 0
            
            if 'quantite_en_réparation' not in item:
                update_fields['quantite_en_réparation'] = 0
            
            # Only update if there are fields to update
            if update_fields:
                update_fields['updated_at'] = datetime.now()
                
                collection.update_one(
                    {'_id': item_id},
                    {'$set': update_fields}
                )
                
                updated_count += 1
                print(f"✅ Updated item: {item.get('designation', 'N/A')}")
        
        print(f"\n📊 Summary:")
        print(f"   Total items: {len(all_equipment)}")
        print(f"   Updated items: {updated_count}")
        print(f"   Items already correct: {len(all_equipment) - updated_count}")
        
        client.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    fix_quantities() 