
---

# Hitcounter App
***Interview Assessment***

## Overview

The Hitcounter App is a simple web application designed to count the number of times a site has been visited. It leverages Redis to store and retrieve the hit count and returns this count to the client. This project was developed as part of an interview assessment.

## Features

- **Hit Counting**: Tracks the number of times the site has been visited.
- **Redis Integration**: Uses Redis as a backend datastore for hit counts.
- **Monitoring**: Integrated with Prometheus for monitoring and metrics collection.

## Project Structure

### Writing the Build

- **TASK 1: Python Build**
  - `app.py`: The main application file written in Python using the Flask framework.
  
- **TASK 2: Docker Build**
  - `Dockerfile`: Contains instructions for creating a Docker image of the app.
  
- **TASK 3: Docker Compose**
  - `docker-compose.yml`: Configuration file for defining and running multi-container Docker applications.

### Instrumentation

- **TASK 4: Prometheus Integration**
  - `prometheus.yml`: Configuration file for Prometheus monitoring.

### Deployment

- **TASK 5: Kubernetes Objects**
  - `app-deployment.yaml`: Kubernetes deployment configuration.
  - `app-ingress.yaml`: Kubernetes ingress configuration.
  - `app-service.yaml`: Kubernetes service configuration.
  - `app-servicemonitor.yaml`: ServiceMonitor configuration for Prometheus integration.
  
- **TASK 6: Deployment Script**
  - `deploy.sh`: Shell script to automate the deployment process on a Minikube cluster.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker**: Required to build and run the Dockerized application.
- **Minikube**: A local Kubernetes cluster for development and testing.
- **HELM**: A package manager for Kubernetes, used to install and manage applications.
- **Prometheus**: An open-source monitoring system with a dimensional data model.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone [repository-url]
   cd hitcounter-app
   ```

2. **Build and Run with Docker Compose**:
   ```bash
   docker-compose up
   ```

3. **Deploy to Minikube**:
   ```bash
   ./deploy.sh
   ```

4. **Access the Application**:
   - Hitcounter App: `http://localhost:8080`
   - Prometheus Console: `http://localhost:9090`

## Feedback and Contributions

Feedback and contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

---

