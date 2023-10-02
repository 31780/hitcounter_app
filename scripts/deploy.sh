#!/bin/bash

# Start minikube
minikube start

# Set Docker environment
eval $(minikube docker-env)

# Build the Docker image within Minikube
docker build -t hitcounter_app:latest .

# Apply the Kubernetes configurations
kubectl apply -f ./kubernetes-configs/app-deployment.yaml
kubectl apply -f ./kubernetes-configs/app-service.yaml
kubectl apply -f ./kubernetes-configs/app-ingress.yaml
kubectl apply -f ./kubernetes-configs/app-servicemonitor.yaml

# Configure Prometheus to scrape the /metrics endpoint
cat <<EOF | kubectl apply -f -
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: flask-app-monitor
  labels:
    release: prometheus
spec:
  selector:
    matchLabels:
      app: flask-app
  endpoints:
  - port: web
    path: /metrics
EOF

# Open Prometheus in the browser
minikube service prometheus-server