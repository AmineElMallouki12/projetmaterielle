import os
import argparse
import unicodedata
from typing import Optional
from pymongo import MongoClient


def normalize(text: Optional[str]) -> str:
    if text is None:
        return ""
    text = str(text).strip().lower()
    # Remove accents
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    # Collapse spaces
    return ' '.join(text.split())


def main():
    parser = argparse.ArgumentParser(description="Set image for equipment by designation")
    parser.add_argument("--file", required=True, help="Path to image file relative to project root, e.g. static/uploads/mire_de_nivellement.png")
    parser.add_argument("--designation", default="Mire de nivellement", help="Designation to match (case-insensitive)")
    parser.add_argument("--mode", choices=["equals", "contains"], default="equals", help="Match mode: exact equals or substring contains (normalized)")
    parser.add_argument("--category", default=None, help="Optional category filter (case-insensitive)")
    parser.add_argument("--dry-run", action="store_true", help="Only show which items would be updated")
    args = parser.parse_args()

    image_path = args.file.replace("\\", "/")
    if not os.path.exists(image_path):
        if args.dry_run:
            print(f"Dry-run: image file not found (ok in dry-run): {image_path}")
        else:
            print(f"❌ Image file not found: {image_path}")
            return

    # Connect to MongoDB (same URI as app)
    client = MongoClient("mongodb://localhost:27017/")
    db = client["inventory_db"]
    equipment = db["equipment"]

    # Normalize inputs and allow common spelling variants
    needle_norm = normalize(args.designation)
    # Add common variants
    variants = {
        needle_norm,
        needle_norm.replace("nivellement", "nivelement"),
        needle_norm.replace("nivelement", "nivellement"),
        needle_norm.replace("niveaulement", "nivellement"),
        needle_norm.replace("niveaulement", "nivelement"),
    }
    category_norm = normalize(args.category) if args.category else None

    # Find all items whose designation matches any variant (case-insensitive)
    items = list(equipment.find({}))
    to_update_ids = []
    for it in items:
        des_norm = normalize(it.get("designation", ""))
        cat_ok = True
        if category_norm:
            cat_ok = (normalize(it.get("category", "")) == category_norm)
        if not cat_ok:
            continue
        if args.mode == "equals":
            if des_norm in variants:
                to_update_ids.append(it.get("id"))
        else:
            # contains mode with broader heuristics
            hit = any(v in des_norm for v in variants)
            if not hit:
                # fallback heuristic: must contain 'mire' and one of nivel/nivea terms
                if "mire" in des_norm and ("nivel" in des_norm or "niveaul" in des_norm or "niveaulement" in des_norm):
                    hit = True
            if hit:
                to_update_ids.append(it.get("id"))

    if not to_update_ids:
        print("No equipment matched the designation. Nothing to update.")
        return

    if args.dry_run:
        print(f"Dry-run: would update {len(to_update_ids)} item(s):")
        print(" ", to_update_ids[:20], "..." if len(to_update_ids) > 20 else "")
        return

    result = equipment.update_many({"id": {"$in": to_update_ids}}, {"$set": {"image": os.path.basename(image_path)}})
    print(f"Updated {result.modified_count} equipment item(s). Set image to '{os.path.basename(image_path)}'.")


if __name__ == "__main__":
    main()


