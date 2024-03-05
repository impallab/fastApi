# Project Report

## Overview

This project aims to develop a sample FastAPI application to serve as the backend for an Asset Performance Analytics Dashboard. The application interacts with a MongoDB database to analyze and collate data related to various assets' performance.

## MongoDB Schema Design

### Assets Collection

- **Asset ID**: Unique identifier for the asset.
- **Asset Name**: Name of the asset.
- **Asset Type**: Type of the asset.
- **Location**: Location of the asset.
- **Purchase Date**: Date when the asset was purchased.
- **Initial Cost**: Initial cost of the asset.
- **Operational Status**: Current operational status of the asset.

### PerformanceMetrics Collection

- **Uptime**: Metric representing the time duration during which the asset was operational.
- **Downtime**: Metric representing the time duration during which the asset was not operational.
- **Maintenance Costs**: Costs incurred for maintenance activities related to the asset.
- **Failure Rate**: Rate of failure experienced by the asset.
- **Efficiency**: Efficiency metric of the asset.

## API Functionality

### CRUD Operations

- **Assets**: Create, read, update, and delete operations for assets.
- **Performance Metrics**: Create, read, update, and delete operations for performance metrics.

### Endpoints for Data Aggregation and Insights

- Calculate average downtime.
- Calculate total maintenance costs.
- Identify assets with high failure rates.

## Development Considerations

- Code is clean, efficient, and follows best practices.
- Thorough documentation is provided for setup, usage, and endpoint details.
- Tests are included to demonstrate API functionality.

## Challenges Faced and Solutions Implemented

### Challenges:

- **Authentication**: Implementing authentication for securing sensitive endpoints.
- **Data Aggregation**: Calculating insights such as average downtime and total maintenance costs.
- **Testing**: Writing comprehensive tests to ensure the functionality of the API.
- **Windows Default Security Prevention**: Facing issues with Windows default security settings preventing certain operations.

### Solutions:

- **Authentication**: Utilized HTTP Basic Authentication for securing endpoints, with hardcoded credentials for demonstration purposes.
- **Data Aggregation**: Implemented aggregation pipelines in MongoDB to calculate insights efficiently.
- **Testing**: Developed unit tests using testing frameworks like PyTest to cover API functionality.
- **Windows Default Security Prevention**: Configured Windows security settings to allow required operations, such as running the FastAPI application and accessing MongoDB.


## Self-Assessment Against Evaluation Criteria

The project meets the specified objectives and technical requirements. The MongoDB schema design effectively captures relevant data for assets and performance metrics. The API functionality covers CRUD operations, data aggregation, and insights generation. Thorough documentation and tests have been included to ensure clarity and reliability.

