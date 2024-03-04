from fastapi import APIRouter
from models.assets import Asset
from config.db import collection
from schemas.asset_schema import list_serial
from bson import ObjectId

router =APIRouter()

#Read Assets :
@router.get("/")
async def Get_all_assets():
    assets = list_serial(collection.find())
    return assets

