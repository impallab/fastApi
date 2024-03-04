from fastapi import APIRouter
from models.assets import Asset
from config.db import collection
from schemas.asset_schema import list_serial
from bson import ObjectId

router =APIRouter()

# Create Asset :
@router.post("/")
async def Add_an_asset(asset:Asset):
    collection.insert_one(dict(asset))

#Read Assets :
@router.get("/")
async def Get_all_assets():
    assets = list_serial(collection.find())
    return assets

#Update Asset :
@router.put("/{id}")
async def  Update_asset(id:str, asset:Asset):
    collection.find_one_and_update( {"_id":ObjectId(id)},{"$set": dict(asset)})

#Delete Asset :
@router.delete("/{id}")
async def Delete_Asset(id:str):
    collection.find_one_and_delete({"_id":ObjectId(id)})