from pymongo import MongoClient
from bson.objectid import ObjectId

def debug_equipment_status():
    """Debug script to check equipment status and quantities"""
    try:
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['inventory_db']
        collection = db['equipment']
        
        print("🔍 Debugging Equipment Status")
        print("=" * 50)
        
        # Get all equipment
        all_equipment = list(collection.find())
        
        for item in all_equipment:
            print(f"\n📦 Item: {item.get('designation', 'N/A')}")
            print(f"   ID: {item.get('id', 'N/A')}")
            print(f"   Status: {item.get('status', 'N/A')}")
            print(f"   Quantité Totale: {item.get('quantite_totale', 'N/A')}")
            print(f"   Quantité Disponible: {item.get('quantite_disponible', 'N/A')}")
            print(f"   Quantité Cassée: {item.get('quantite_cassée', 'N/A')}")
            print(f"   Quantité en Réparation: {item.get('quantite_en_réparation', 'N/A')}")
            
            # Check if it should appear in public catalog
            status = item.get('status', '')
            quantite_disponible = item.get('quantite_disponible', item.get('quantite_totale', 1))
            
            should_show = (
                (status == 'Disponible' or status == 'Available') and 
                quantite_disponible > 0
            )
            
            print(f"   Should show in catalog: {'✅ YES' if should_show else '❌ NO'}")
        
        print(f"\n📊 Summary:")
        print(f"   Total items: {len(all_equipment)}")
        
        # Count by status
        status_counts = {}
        for item in all_equipment:
            status = item.get('status', 'Unknown')
            status_counts[status] = status_counts.get(status, 0) + 1
        
        for status, count in status_counts.items():
            print(f"   Status '{status}': {count} items")
        
        client.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    debug_equipment_status() 