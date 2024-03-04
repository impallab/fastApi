from pydantic import BaseModel
from typing import Optional

class Asset(BaseModel):
    asset_id: str
    asset_name: str
    asset_type: str
    location: str
    purchase_date: str
    initial_cost: float
    operational_status: str
