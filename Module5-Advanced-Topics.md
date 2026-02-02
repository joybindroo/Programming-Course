# Module 5: Advanced Topics

This culminating module pushes beyond core programming into the practices you will encounter when shipping real products. Each section combines conceptual depth with labs that reinforce production-grade habits.

## Learning Goals
- Design resilient code that handles persistence, failures, and parallel workloads.
- Recognize when to apply established architectural patterns.
- Ship cross-platform user experiences (web, mobile, interactive media).
- Explore the full machine-learning lifecycle from data prep to deployment.

## File I/O Systems and Data Pipelines

### Core Concepts
- Compare text, binary, memory-mapped, and streaming IO plus their performance trade-offs.
- Understand how buffering layers (stdio, OS page cache, disks) influence throughput and durability guarantees.
- Track file permissions, locking semantics, and platform-specific path handling.

### Structured Data Workflows
- Parse CSV/JSON/YAML with schema validation and fallbacks when columns drift.
- Snapshot and append logs safely by combining `with` blocks, flush intervals, and atomic rename patterns.
- Implement checksum-based verification to detect silent corruption when moving artifacts between systems.

```python
from pathlib import Path
import json

def stream_events(source: Path, sink: Path) -> None:
    with source.open('r', encoding='utf-8') as reader, sink.open('a', encoding='utf-8') as writer:
        for line in reader:
            event = json.loads(line)
            writer.write(json.dumps({"id": event["id"], "status": event["status"]}) + "\n")
            writer.flush()  # keep queues short for crash safety
```

### Practice Lab
1. Build a CLI that tails sensor data and rotates files when they exceed 10 MB.
2. Extend it with JSON schema validation and dead-letter queues for malformed rows.

## Defensive Exception Handling

### Patterns
- Layered exception hierarchies (domain-level vs infrastructure) clarify recovery boundaries.
- Use `try/except/else/finally` to keep cleanup logic deterministic; log with structured context.
- Favor guard clauses and assertions near the source of truth to catch bugs early.

### Anti-Patterns to Avoid
- Swallowing exceptions (`except Exception: pass`) which hides systemic failures.
- Raising generic errors without actionable metadata.
- Mixing control flow and exceptions; prefer return values for expected branches.

### Mini Project
Refactor a legacy import script to:
1. Introduce custom exceptions (`DataValidationError`, `ExternalServiceError`).
2. Retry transient network faults with exponential backoff.
3. Emit metrics (success/failure counts) for observability dashboards.

## Concurrency and Parallelism

### Comparison Matrix
| Model | Best Use | Hazards |
| --- | --- | --- |
| Threads | IO-heavy tasks needing shared memory | Race conditions, GIL (Python) |
| Processes | CPU-bound work, isolation | IPC overhead |
| Async IO | Vast numbers of sockets/timers | Requires non-blocking libraries |

### Coordination Techniques
- Protect shared state with locks or lock-free primitives (atomic queues, ring buffers).
- Apply producer/consumer queues to decouple ingestion from processing throughput.
- Use structured concurrency patterns (task groups, supervisors) to ensure child tasks finish or cancel together.

### Exercise
Build a crawler that:
1. Kicks off async fetches for hundreds of URLs (e.g., `asyncio` + `aiohttp`).
2. Falls back to a thread pool for CPU-heavy HTML parsing.
3. Aggregates metrics and respects rate limits using tokens/leaky buckets.

## Design Patterns in Practice

### Creational
- Factory Method: switch algorithms based on configuration without leaking constructors.
- Builder: assemble complex immutable objects (e.g., deployment payloads) step-by-step.

### Structural
- Adapter: wrap third-party SDKs so the rest of your code uses a stable interface.
- Facade: expose a simplified API over subsystems (auth, billing, notifications) for other teams.

### Behavioral
- Observer/Event Bus: broadcast state changes from domain models to UI or logging.
- Strategy: swap scoring algorithms or ML inference paths without touching orchestrators.

### Pattern Studio
Choose a real feature (payment pipeline, multiplayer lobby) and document:
1. The problem statement.
2. Why a pattern fits.
3. Trade-offs introduced (complexity, testing burden).

## Web Development Deep Dive

### Backend Skills
- Model REST resources with OpenAPI specs, versioning, and pagination contracts.
- Implement layered architecture (handlers → services → repositories) to isolate logic.
- Secure APIs with JWT/OAuth flows plus rate limiting, input validation, and audit logging.

### Frontend/Full-Stack Touchpoints
- Build responsive layouts (CSS grid/flex) plus component-driven UI frameworks.
- Wire data fetching hooks with optimistic updates and background revalidation.
- Automate testing (unit + contract + end-to-end) and CI deployments to GitHub Pages or cloud apps.

### Lab
Ship a mini SaaS dashboard:
1. Postgres + REST API for subscription data.
2. Web client with charts, filters, and offline caching.
3. Observability: request tracing + uptime checks.

## Mobile App Development

### Platform Choices
- Native (Swift/Kotlin) grants first-class APIs, while cross-platform (Flutter/React Native) eases shared logic.
- Evaluate navigation stacks, state containers, and build tooling (Gradle/Xcode).

### Device Integration
- Use permission flows for camera/GPS; plan fallbacks when users decline.
- Cache data locally (SQLite/Room/Core Data) and sync opportunistically with background tasks.

### Capstone Sprint
Prototype a productivity app that:
1. Captures tasks offline and syncs when connectivity returns.
2. Sends scheduled reminders via OS notification services.
3. Tracks performance and crashes through telemetry SDKs.

## Game Development Foundations

### Core Loop
- Timestep management (`fixed_update`, `render`) keeps physics deterministic across frame rates.
- Scene graph hierarchies simplify collision checks and transforms.

### Systems to Implement
- Input mapping layer that decouples hardware keys from gameplay actions.
- Entity-component-system (ECS) or state machines for modifiable behaviors.
- Basic physics: acceleration, gravity, collision responses, tweaked via debug overlays.

### Workshop
Create a tower-defense prototype with:
1. Asset pipeline (tile maps, sprite atlases).
2. AI pathfinding (A*, wavefront).
3. Save/restore checkpoints to reinforce file IO + serialization skills.

## Machine Learning and AI

### Workflow
- Data ops: exploratory analysis, feature scaling, train/validation/test splits.
- Model development: start with baseline (linear/logistic), then iterate to trees, boosting, or neural nets.
- Evaluation: precision/recall, ROC AUC, calibration, confusion matrices.

### Responsible AI Considerations
- Track dataset provenance and bias audits.
- Implement model monitoring to detect drift and trigger retraining.
- Package models with reproducible environments (Conda, Docker) and REST inference endpoints.

### Hands-On Track
1. Build an ML notebook predicting churn from anonymized product metrics.
2. Convert it into a service with batching, caching, and tracing.
3. Automate nightly evaluation jobs that compare live metrics vs historic baselines.

## Capstone: Systems Integration Challenge
- Combine at least three topics above (e.g., mobile client ↔ web API ↔ ML scoring service).
- Document architecture decisions (ADR), error budgets, and deployment checklist.
- Present observability dashboards demonstrating throughput, latency, and failure recovery drills.
