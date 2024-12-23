# QR Code Generator - DevOps Project

A comprehensive DevOps implementation of a QR Code Generator that demonstrates modern cloud-native development practices. The project combines a Next.js front-end with a FastAPI backend, orchestrated through Kubernetes and managed via Terraform infrastructure as code.

## 🚀 Features

- Full-stack application with Next.js frontend and FastAPI backend
- Containerized applications using Docker
- Infrastructure as Code using Terraform
- Kubernetes deployments for orchestration
- Automated CI/CD pipeline with GitHub Actions

## 🏗️ Architecture

### Frontend
- Built with Next.js
- Containerized using Docker
- Kubernetes deployment configuration
- Tailwind CSS for styling

### Backend
- FastAPI-powered REST API
- Python-based microservice
- Containerized using Docker
- Kubernetes deployment configuration

### DevOps Pipeline
- Automated builds using GitHub Actions
- Docker image publication to Docker Hub
- Infrastructure provisioning with Terraform
- Kubernetes orchestration

## 🛠️ Technical Stack

- **Frontend**: Next.js
- **Backend**: FastAPI (Python)
- **Infrastructure**: Terraform, AWS
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions

## 📁 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── build-docker.yaml
├── api/
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── test_main.py
├── front-end-nextjs/
│   ├── Dockerfile
│   └── src/
├── infrastructure/
│   ├── main.tf
│   └── provider.tf
├── backend.yaml
├── frontend.yaml
└── README.md
```

## 🚀 Deployment Pipeline

The CI/CD pipeline automates the following steps:
1. Code checkout
2. Docker image building for both frontend and backend
3. Image publication to Docker Hub
4. Infrastructure provisioning
5. Kubernetes deployment

## Deployment & Infrastructure

## 🔄 CI/CD Pipeline

The CI/CD pipeline is implemented using GitHub Actions and is defined in `build-docker.yaml`. This pipeline automates the build and deployment process for both frontend and backend services.

### Pipeline Steps
1. **Code Checkout** 
   - Utilizes `actions/checkout@v4`
   - Fetches the latest code from the repository

2. **Docker Image Building**
   - Builds separate images for API and frontend
   - Uses dedicated Dockerfiles for each service

3. **Image Publication**
   - Pushes built images to Docker Hub
   - Ensures availability for deployment

## 🐳 Docker Configuration

### Backend Service
- Uses official Python base image
- Located in `/api/Dockerfile`
- Dependencies managed via `requirements.txt`

### Frontend Service
- Uses official Node.js base image
- Located in `/front-end-nextjs/Dockerfile`
- Dependencies managed via package lockfile

## ☁️ Infrastructure

The project's infrastructure is managed through Terraform, with configuration files located in the `/infrastructure` directory.

### AWS Provider Setup
- Provider configuration in `provider.tf`
- Manages AWS authentication and region settings

### Core Infrastructure (`main.tf`)
- VPC configuration
- Subnet management
- Route table setup
- EKS cluster provisioning

## ☸️ Kubernetes Deployments

### API Service
- Deployment defined in `backend.yaml`
- Creates:
  - Kubernetes Deployment
  - Associated Service
  - Required configurations

### Frontend Service
- Deployment defined in `frontend.yaml`
- Creates:
  - Kubernetes Deployment
  - Associated Service
  - Required configurations

---

This infrastructure setup ensures a scalable, maintainable, and automated deployment process for the QR Code Generator application.

## 💻 Local Development

### Backend Setup
```bash
cd api
python -m venv .venv
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Setup
```bash
cd front-end-nextjs
npm install
npm run dev
```
