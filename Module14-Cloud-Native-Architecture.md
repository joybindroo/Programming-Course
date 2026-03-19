# Module 14 – Cloud‑Native Architecture

---

## Learning Objectives
- Distinguish between IaaS, PaaS, and SaaS models.
- Deploy a microservice to a managed Kubernetes service (e.g., GKE/EKS/AKS).
- Use serverless functions (AWS Lambda, Cloud Functions) for event‑driven workloads.
- Implement infrastructure‑as‑code with Terraform for cloud resources.
- Apply cost‑optimization and autoscaling strategies.

## Overview
Modern applications run on cloud platforms that provide elasticity, managed services, and global reach. This module equips you with the concepts and hands‑on skills to design, provision, and operate cloud‑native systems.

## Key Topics
1. **Cloud Service Models** – compute, storage, networking, managed databases.
2. **Containers & Orchestration** – Docker, Kubernetes basics, Helm charts.
3. **Serverless** – functions‑as‑a‑service, event sources, cold‑start considerations.
4. **IaC with Terraform** – providers, state management, modules.
5. **Observability** – Prometheus, Grafana, distributed tracing (Jaeger).
6. **Security in the Cloud** – IAM roles, VPC, network policies.
7. **Cost Management** – budgeting, right‑sizing, spot instances.
8. **Resilience Patterns** – circuit breaker, bulkhead, graceful degradation.

## Mini‑Lab
1. Write a simple **REST API** in FastAPI, containerize it, and push to Docker Hub.
2. Deploy the container to a **Kubernetes cluster** using a Helm chart.
3. Add a **serverless function** that processes messages from a queue and stores results in a cloud‑hosted database.
4. Define the entire stack in **Terraform**, apply it, and destroy it cleanly.
5. Set up **Prometheus** alerts for CPU usage > 80 % and auto‑scale the deployment.

## Resources
- *The Cloud Native Landscape* – CNCF (https://landscape.cncf.io)
- Terraform docs: https://developer.hashicorp.com/terraform/docs
- Kubernetes official tutorial: https://kubernetes.io/docs/tutorials/
- Serverless guide: https://aws.amazon.com/lambda/faqs/
- Cost‑optimization: https://cloud.google.com/blog/topics/cost-management

---

*End of Module 14*