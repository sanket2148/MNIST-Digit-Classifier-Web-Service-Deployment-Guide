# MNIST Digit Classifier Web Service Deployment Guide

Welcome to the MNIST Digit Classifier Deployment Guide. This step-by-step guide will walk you through deploying a Flask-based web service that utilizes a trained MNIST model to classify handwritten digits.

## Prerequisites

Before we begin, ensure you have the following installed:
- Docker Desktop with Kubernetes
- Python 3
- Git

## Setup Instructions

### Clone the Repository

First, clone the repository to get the code on your local machine:

```sh
git clone https://github.com/sanket2148/MNIST-Digit-Classifier-Web-Service-Deployment-Guide.git
cd MNIST-Digit-Classifier-Web-Service-Deployment-Guide
```

### Run the Flask App Locally

Create a Python virtual environment and activate it:

Windows:
```sh
python -m venv venv
.\venv\Scripts\activate
```

macOS/Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:
```sh
pip install -r requirements.txt
```

Start the Flask app:
```sh
python app.py
```

Visit `http://localhost:5000` in your web browser to ensure it's running.

### Containerize the Application

Build the Docker image:
```sh
docker build -t ai-assignment-app .
```

Run the container:
```sh
docker run -p 5000:5000 ai-assignment-app
```

### Deploy to Kubernetes

Apply the Kubernetes deployment configuration:
```sh
kubectl apply -f k8s/app-deployment.yaml
```

Apply the Kubernetes service configuration:
```sh
kubectl apply -f k8s/app-service.yaml
```

### Interact With Your Deployment

Find your pod name:
```sh
kubectl get pods
```

Look for the pod name that starts with `ai-assignment-app-deployment`.

Access the logs for a specific pod:
```sh
kubectl logs [your-pod-name]
```

Replace `[your-pod-name]` with the actual pod name from the previous command.

Port-forward to access the Flask app:
```sh
kubectl port-forward pod/[your-pod-name] 5000:5000
```

Open `http://localhost:5000` in your web browser.

### Troubleshooting

If you run into issues, ensure the Kubernetes services are correctly set up:
```sh
kubectl get services
```

For detailed logs, run:
```sh
kubectl describe pod [your-pod-name]
```

---
