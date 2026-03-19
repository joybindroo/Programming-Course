# Module 13 – Security Engineering

---

## Learning Objectives
- Identify common security threats and the OWASP Top 10.
- Apply secure coding practices for input validation, authentication, and cryptography.
- Perform threat modeling and security testing (static analysis, dependency scanning).
- Secure container images and CI pipelines.
- Understand secret management and least‑privilege principles.

## Overview
Security must be baked into software from the start. This module introduces core concepts, practical tools, and workflows to build resilient, attack‑resistant applications.

## Key Topics
1. **OWASP Top 10** – injection, broken auth, XSS, etc.
2. **Secure Coding** – input sanitization, parameterized queries, password hashing (bcrypt, Argon2).
3. **Threat Modeling** – STRIDE, attack trees, data flow diagrams.
4. **Static & Dynamic Analysis** – Bandit, SonarQube, OWASP ZAP.
5. **Container Security** – image scanning (Trivy, Snyk), minimal base images, user namespaces.
6. **Secret Management** – Vault, GitHub Secrets, environment‑variable hygiene.
7. **Security in CI/CD** – gate checks, dependency‑check, signed artifacts.
8. **Compliance Basics** – GDPR, PCI‑DSS, secure development lifecycle (SDL).

## Mini‑Lab
1. Harden a small Flask API: add input validation, use `flask‑talisman` for headers, store passwords with `argon2-cffi`.
2. Scan the Dockerfile with **Trivy** and fix identified vulnerabilities.
3. Create a **GitHub Actions** workflow that runs **Bandit** and **Trivy** on every PR.
4. Perform a simple **threat model** using a data‑flow diagram and list mitigations.

## Resources
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- *Secure Coding in Python* – Brett Slatkin (O'Reilly)
- *Web Application Security* – Andrew Hoffman
- Trivy docs: https://github.com/aquasecurity/trivy
- GitHub Actions security guide: https://docs.github.com/en/actions/security-guides

---

*End of Module 13*