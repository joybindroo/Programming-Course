# Module 12 – Software Testing & QA

---

## Learning Objectives
- Understand the purpose and types of testing (unit, integration, system, acceptance).
- Write effective unit tests in Python (pytest) and JavaScript (Jest).
- Apply Test‑Driven Development (TDD) workflow.
- Use code coverage tools and interpret reports.
- Automate test pipelines in CI/CD.

## Overview
Software testing ensures correctness, reliability, and maintainability. This module covers testing fundamentals, practical tooling, and how to embed quality checks into the development lifecycle.

## Key Topics
1. **Testing Pyramid** – unit, integration, UI/acceptance layers.
2. **Unit Testing** – pytest, unittest, JEST, assertions.
3. **Mocking & Stubbing** – isolate dependencies.
4. **Test‑Driven Development** – red‑green‑refactor cycle.
5. **Coverage Analysis** – `coverage.py`, `nyc`, coverage thresholds.
6. **Property‑Based Testing** – hypothesis, fast‑check.
7. **Continuous Integration** – GitHub Actions, GitLab CI, test matrix.
8. **Mutation Testing** – `mutmut`, `stryker` basics.

## Mini‑Lab
1. Write a simple **calculator** library (add, subtract, multiply, divide) in Python.
2. Create a full test suite with `pytest` covering normal cases, edge cases, and error handling.
3. Add a **coverage** step and enforce **90 %** coverage.
4. Convert the same library to JavaScript and write tests with **Jest**.
5. Set up a **GitHub Actions** workflow that runs both test suites on every push.

## Resources
- *Python Testing with pytest* – Brian Okken
- *Testing JavaScript Applications* – Kent C. Dodds
- Official docs: https://docs.pytest.org, https://jestjs.io
- Mutation testing intro: https://github.com/boxed/mutmut

---

*End of Module 12*