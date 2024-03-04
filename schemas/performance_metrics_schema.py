def individual_performance_metrics(performance_metric) -> dict:
    return {
        "asset_id": str(performance_metric["asset_id"]),
        "uptime": float(performance_metric["uptime"]),
        "downtime": float(performance_metric["downtime"]),
        "maintenance_costs": float(performance_metric["maintenance_costs"]),
        "failure_rate": float(performance_metric["failure_rate"]),
        "efficiency": float(performance_metric["efficiency"])
    }

def list_performance_metrics(performance_metrics) -> list:
    return [individual_performance_metrics(performance_metric) for performance_metric in performance_metrics]
