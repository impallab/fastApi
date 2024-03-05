import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_asset():
    # Test creating a new asset
    asset_data = {
        "asset_id": "123",
        "asset_name": "Test Asset",
        "asset_type": "Test Type",
        "location": "Test Location",
        "purchase_date": "2023-01-01",
        "initial_cost": 1000.00,
        "operational_status": "Operational"
    }
    response = client.post("/assets/", json=asset_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Asset created successfully"}

def test_get_all_assets():
    # Test getting all assets
    response = client.get("/assets/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_asset():
    # Test updating an existing asset
    asset_id = "123"
    updated_data = {
        "asset_name": "Updated Asset Name",
        "asset_type": "Updated Asset Type",
        "location": "Updated Location"
    }
    response = client.put(f"/assets/{asset_id}", json=updated_data)
    assert response.status_code == 200

def test_delete_asset():
    # Test deleting a specific asset
    asset_id = "123"
    response = client.delete(f"/assets/{asset_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Asset deleted successfully"}

def test_calculate_average_downtime():
    # Test calculating average downtime
    response = client.get("/insights/average_downtime")
    assert response.status_code == 200
    assert "average_downtime" in response.json()


