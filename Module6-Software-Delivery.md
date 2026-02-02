# Module 6: Software Delivery & DevOps

This module turns advanced engineering work into durable, observable, and continuously deployable systems. You will master the tooling and mindsets required to ship, monitor, and evolve production services.

## Learning Outcomes
- Design CI/CD pipelines that gate changes with automated tests, quality gates, and approvals.
- Manage infrastructure as code (IaC) for consistent environments across dev, staging, and prod.
- Package, deploy, and observe services with containers, orchestration, and telemetry stacks.
- Embed security, resilience, and incident-response practices throughout the delivery lifecycle.

---

## Section 1 – Release Engineering & CI/CD

### Key Concepts
- **Branching & Release Strategies:** Trunk-based vs GitFlow, feature flags, and release trains.
- **Automated Quality Gates:** Unit/integration tests, linting, static analysis, and code coverage thresholds.
- **Artifacts & Versioning:** Build once, promote many; semantic versioning, SBOM generation.

```yaml
# .github/workflows/ci.yml (conceptual snippet)
name: service-ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest --maxfail=1 --disable-warnings
```

### Lab
1. Build a GitHub Actions workflow that compiles, tests, and publishes coverage reports.
2. Add required status checks before merging to `main`.

---

## Section 2 – Infrastructure as Code (IaC)

### Tooling & Practices
- Declarative IaC (Terraform, Pulumi) vs configuration management (Ansible, Chef).
- Module decomposition, variables, and remote state backends for collaborative teams.
- Secrets handling (Vault, SSM, sealed secrets) and least-privilege credentials.

### Exercise
Provision a staging environment:
1. VPC + subnets + security groups.
2. Managed database + parameterized storage.
3. Outputs consumed by CI/CD to wire service endpoints.

---

## Section 3 – Containerization & Orchestration

### Containers 101
- Author minimal Dockerfiles with multi-stage builds, health checks, and non-root users.
- Apply image scanning (Trivy, Grype) and tagging heuristics (`v1.4.0`, `sha256`).

### Orchestration Options
- Docker Compose for local multi-service workflows.
- Kubernetes primitives (Deployment, Service, Ingress, ConfigMap, Secret) and Helm charts.
- Serverless alternatives (Cloud Run, Lambda, Azure Functions) for event-driven workloads.

### Workshop
Deploy the Module 5 capstone backend as a containerized service:
1. Build an image pipeline with cache-friendly layers.
2. Publish to a registry (GHCR, ECR, ACR).
3. Ship to Kubernetes with rolling updates and probes.

---

## Section 4 – Observability & Incident Response

### Telemetry Stack
- **Metrics:** RED/USE metrics, Prometheus scraping, alert thresholds, SLO/SLA definitions.
- **Logs:** Structured JSON, correlation IDs, centralized log aggregation (ELK, Loki).
- **Traces:** OpenTelemetry instrumentation, sampling strategies, distributed tracing viewers.

### Incident Workflow
- On-call rotations, runbooks, and blameless postmortems.
- Automation for paging, chatops commands, and status page updates.

### Drill
Simulate a latency spike:
1. Trigger alerts via load testing.
2. Trace the bottleneck through dashboards/logs.
3. Document a post-incident timeline with corrective actions.

---

## Section 5 – Security & Compliance

### Shift-Left Security
- Dependency scanning (Dependabot, Snyk), SAST/DAST, container image policies.
- Secrets detection in CI, commit hooks, and policy-as-code (OPA, Sentinel).

### Governance
- Access reviews, infrastructure drift detection, and audit trails.
- Data residency, encryption (TLS, KMS, envelope encryption) and compliance mapping (SOC 2, ISO 27001).

---

## Section 6 – Resilience & Progressive Delivery

### Deployment Strategies
- Blue/green, canary, and rolling strategies with automated rollback triggers.
- Feature flags and A/B testing to decouple deploy from release.

### Chaos & Reliability Engineering
- Inject failure (latency, packet loss, node kill) with tools like Gremlin or Chaos Mesh.
- GameDays to practice mitigation playbooks.

---

## Capstone: Production-Ready Launch
Build on Modules 4–5 by shipping a multi-service product with the following deliverables:
1. **CI/CD Pipeline:** Automated tests, security scans, deploy to staging + prod with approvals.
2. **IaC + Containers:** Terraform (or equivalent) for cloud resources; Docker images deployed via Kubernetes manifests or serverless configs.
3. **Observability:** Dashboards tracking latency, errors, saturation; alerting hooked to on-call channels.
4. **Resilience Plan:** Documented rollback plan, feature-flag strategy, and chaos test results.
5. **Security Checklist:** Dependency reports, secrets handling notes, and access reviews.

Document everything in an architecture decision record (ADR) and record a short demo walk-through explaining how the system moves from commit to production safely.
