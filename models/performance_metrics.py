from pydantic import BaseModel

class PerformanceMetrics(BaseModel):
    PerformanceMetrics_id: str
    asset_name: str
    uptime: float
    downtime: float
    maintenance_costs: float
    failure_rate: float
    efficiency: float
