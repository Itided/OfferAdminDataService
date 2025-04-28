# Litestar Service: API Gateway for Admin Panel

## Overview

A new service has been implemented using **Litestar**, which acts as an API gateway for all requests under the /domain/api path. This service now handles the logic that was previously handled by the admin_panel API

## Key Features

- **API Gateway**: The Litestar service serves as a central entry point for all API requests under the /domain/api path.
- **Refactored API Logic**: The logic of the existing admin_panel API has been refactored and integrated into the new Litestar-based service.
  
The service intercepts all incoming requests that begin with /domain/api 

## Example of  Endpoints
**API Schema**: [http://localhost:5000/schema](http://localhost:5000/schema)

### API Gateway for Admin Panel  
**Author of OfferAdmin**: [L1onLight](https://github.com/L1onLight) 

# Running the Project in Development Mode

To run the project in development mode, use the following command:
```bash
$ make dev
