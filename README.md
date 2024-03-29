# Asset Performance Analytics Dashboard API Documentation

## Introduction

Welcome to the Asset Performance Analytics Dashboard API documentation. This API serves as the backend for an Asset Performance Analytics Dashboard, allowing users to interact with data related to various assets' performance. This documentation provides instructions for setup, usage, and details about the available endpoints.

## Setup

To set up the API, follow these steps:

1. Clone the repository from GitHub: `git clone https://github.com/impallab/fastApi.git`

2. Install the required dependencies: `pip install -r requirements.txt`
3. Configure the MongoDB connection in `config/db.py`
4. Run the FastAPI application: `uvicorn main:app --reload`

## Usage

Once the API is set up and running, you can interact with it using HTTP requests. Here are the available endpoints:

### Assets

- **GET /assets/**: Retrieve all assets.
- **GET /assets/{id}**: Retrieve a specific asset by its ID.
- **POST /assets/**: Create a new asset.
- **PUT /assets/{id}**: Update an existing asset.
- **DELETE /assets/{id}**: Delete a specific asset by its ID.
- **DELETE /assets/**: Delete all assets.

### Performance Metrics

- **GET /performance_metrics/**: Retrieve all performance metrics.
- **GET /performance_metrics/{id}**: Retrieve a specific performance metric by its ID.
- **POST /performance_metrics/**: Create a new performance metric.
- **PUT /performance_metrics/{id}**: Update an existing performance metric.
- **DELETE /performance_metrics/{id}**: Delete a specific performance metric by its ID.
- **DELETE /performance_metrics/**: Delete all performance metrics.

### Insights

- **GET /insights/average_downtime**: Calculate the average downtime across all assets.
- **GET /insights/total_maintenance_costs**: Calculate the total maintenance costs across all assets.
- **GET /insights/high_failure_rate_assets**: Identify assets with high failure rates.

## Authentication

Sensitive endpoints require authentication using HTTP Basic Authentication. Include the username and password in the request headers as follows:


Replace `base64_encode(username:password)` with the Base64-encoded string of your actual username and password (e.g., `YWRtaW46cGFzc3dvcmQ=`).

## Example

Here's an example of how to make a request to create a new asset using cURL:

```bash
curl -X POST "http://localhost:8000/assets/" \
     -H "Content-Type: application/json" \
     -H "Authorization: Basic YWRtaW46cGFzc3dvcmQ=" \
     -d '{"asset_id": "123", "asset_name": "Asset 1", "asset_type": "Type 1", "location": "Location 1", "purchase_date": "2023-01-01", "initial_cost": 1000.00, "operational_status": "Operational"}'

## Error Handling

For unsuccessful requests, the API returns appropriate HTTP status codes along with error messages in the response body. Here are some common status codes:

- **400 Bad Request**: The request could not be understood or was missing required parameters.
- **401 Unauthorized**: The request requires user authentication.
- **404 Not Found**: The requested resource could not be found.
- **500 Internal Server Error**: The server encountered an unexpected condition that prevented it from fulfilling the request.

## Data Validation Rules

When creating or updating assets and performance metrics, ensure that the request body adheres to the following data validation rules:

- **asset_id**: Must be a unique identifier for the asset.
- **asset_name**: Must be a non-empty string.
- **asset_type**: Must be a non-empty string.
- **location**: Must be a non-empty string.
- **purchase_date**: Must be a valid date in the format YYYY-MM-DD.
- **initial_cost**: Must be a non-negative float.
- **operational_status**: Must be one of the predefined operational statuses (e.g., "Operational", "Under Maintenance", "Out of Service").

Similar validation rules apply to performance metrics fields such as uptime, downtime, maintenance_costs, failure_rate, and efficiency.

## Limitations and Constraints

There are no rate limits imposed on API requests at this time.
The maximum payload size for requests is 10 MB.

## Project Report

For detailed information about the project, including its objectives, MongoDB schema design, API functionality, development considerations, challenges faced, solutions implemented, and self-assessment against the evaluation criteria, refer to the [Project_Report.md](Project_Report.md) file.


## Contact

For assistance or further inquiries, feel free to reach out via email:

- **Email**: [pallab13nayagram@gmail.com](mailto:pallab13nayagram@gmail.com)
