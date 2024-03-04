from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List
from models.assets import Asset
from models.performance_metrics import PerformanceMetrics
from config.db import collection_assets, collection_performance_metrics
from schemas.asset_schema import list_serial
from schemas.performance_metrics_schema import list_performance_metrics
from bson import ObjectId

router = APIRouter()

# Home route :
router.get("/")
async def home():
    return {
        "message": "Welcome to the Assets and Performance Metrics Tracker API using fastAPI ",
        "documentation": "/docs"
    }

security = HTTPBasic()

# Function to authenticate users
def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "password"
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    return True

# CRUD operations for assets

# Create one asset
@router.post("/assets/")
async def add_asset(asset: Asset, authenticated: bool = Depends(authenticate_user)):
    try:
        collection_assets.insert_one(asset.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Create many assets
@router.post("/assets/bulk_insert")
async def bulk_insert_assets(assets: List[Asset], authenticated: bool = Depends(authenticate_user)):
    try:
        collection_assets.insert_many([asset.dict() for asset in assets])
        return {"message": "Assets inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Read all assets
@router.get("/assets/")
async def get_all_assets(authenticated: bool = Depends(authenticate_user)):
    try:
        assets = list_serial(collection_assets.find())
        return assets
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Update asset using asset id
@router.put("/assets/{id}")
async def update_asset(id: str, asset: Asset, authenticated: bool = Depends(authenticate_user)):
    try:
        collection_assets.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(asset)})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Delete particular asset
@router.delete("/assets/{id}")
async def delete_asset(id: str, authenticated: bool = Depends(authenticate_user)):
    try:
        collection_assets.find_one_and_delete({"_id": ObjectId(id)})
        return {"message": "Asset deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Delete all assets
@router.delete("/assets/")
async def delete_all_assets(authenticated: bool = Depends(authenticate_user)):
    try:
        collection_assets.delete_many({})
        return {"message": "All assets deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# CRUD operations for performance metrics

# Create one performance_metrics
@router.post("/performance_metrics/")
async def add_performance_metrics(performance_metrics: PerformanceMetrics, authenticated: bool = Depends(authenticate_user)):
    try:
        collection_performance_metrics.insert_one(performance_metrics.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Create many performance_metrics
@router.post("/performance_metrics/bulk_insert")
async def bulk_insert_performance_metrics(performance_metrics: List[PerformanceMetrics], authenticated: bool = Depends(authenticate_user)):
    try:
        collection_performance_metrics.insert_many([pm.dict() for pm in performance_metrics])
        return {"message": "Performance metrics inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Read all performance metrics
@router.get("/performance_metrics/")
async def get_all_performance_metrics(authenticated: bool = Depends(authenticate_user)):
    try:
        performance_metrics = list_performance_metrics(collection_performance_metrics.find())
        return performance_metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Update a performance_metric using its id
@router.put("/performance_metrics/{id}")
async def update_performance_metrics(id: str, performance_metrics: PerformanceMetrics, authenticated: bool = Depends(authenticate_user)):
    try:
        collection_performance_metrics.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(performance_metrics)})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Delete particular performance_metric
@router.delete("/performance_metrics/{id}")
async def delete_performance_metrics(id: str, authenticated: bool = Depends(authenticate_user)):
    try:
        collection_performance_metrics.find_one_and_delete({"_id": ObjectId(id)})
        return {"message": "Performance metric deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Delete all performance metrics
@router.delete("/performance_metrics/")
async def delete_all_performance_metrics(authenticated: bool = Depends(authenticate_user)):
    try:
        collection_performance_metrics.delete_many({})
        return {"message": "All performance metrics deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Data aggregation and insights

@router.get("/insights/average_downtime")
async def calculate_average_downtime(authenticated: bool = Depends(authenticate_user)):
    try:
        total_downtime = sum(performance_metric["downtime"] for performance_metric in collection_performance_metrics.find())
        total_assets = collection_performance_metrics.count_documents({})
        if total_assets == 0:
            raise HTTPException(status_code=404, detail="No performance metrics found")
        average_downtime = total_downtime / total_assets
        return {"average_downtime": average_downtime}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/insights/total_maintenance_costs")
async def calculate_total_maintenance_costs(authenticated: bool = Depends(authenticate_user)):
    try:
        total_maintenance_costs = sum(performance_metric["maintenance_costs"] for performance_metric in collection_performance_metrics.find())
        return {"total_maintenance_costs": total_maintenance_costs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/insights/high_failure_rate_assets")
async def identify_high_failure_rate_assets(authenticated: bool = Depends(authenticate_user)):
    try:
        high_failure_rate_threshold = 0.1  # Example threshold: 0.1
        high_failure_rate_assets = list_performance_metrics(collection_performance_metrics.find({"failure_rate": {"$gt": high_failure_rate_threshold}}))
        return {"high_failure_rate_assets": high_failure_rate_assets}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

