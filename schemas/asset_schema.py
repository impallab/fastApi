def individual_serial(asset) -> dict:
    return {
    "id": str(asset["_id"]),
    "asset_name": str(asset["asset_name"]),
    "asset_type": str(asset["asset_type"]),
    "location": str(asset["location"]),
    "purchase_date": str(asset["purchase_date"]),
    "initial_cost": float(asset["initial_cost"]),
    "operational_status": str(asset["operational_status"])
    }

def list_serial(assets) -> list:
    return  [individual_serial(asset) for asset in  assets] 