import pandas as pd

def check_excel_columns():
    """Check the actual column names in the Excel file"""
    excel_file = 'NV INVENTAIRE.xlsx'
    
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file)
        
        print("📊 Excel file columns:")
        print("=" * 50)
        for i, col in enumerate(df.columns):
            print(f"{i+1:2d}. '{col}'")
        
        print("\n📋 First few rows of data:")
        print("=" * 50)
        print(df.head(3).to_string())
        
        print(f"\n📈 Total rows: {len(df)}")
        
    except Exception as e:
        print(f"❌ Error reading Excel file: {e}")

if __name__ == "__main__":
    check_excel_columns() 