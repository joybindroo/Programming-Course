# Module 7: Docker Mastery

This module delivers an end-to-end walkthrough of Docker—from installation and context management to day-two operations and delivery pipelines. Expect practical labs plus a toolbox of commands you will use daily when packaging and shipping software.

## Learning Objectives
- Install Docker Engine, verify health, and authenticate to registries securely.
- Manage contexts, images, and containers across local machines, remote hosts, or the cloud.
- Monitor resource usage, inspect runtime state, and collect diagnostics for incident response.
- Compose multi-service applications and move artifacts between environments confidently.

---

## 1. Installing & Verifying Docker

1. **Install (Linux example):**

```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker "$USER"
```
2. **Verify Engine & Client:** `docker version`
3. **Check Daemon Health:** `docker info`
4. **Log In to Registry:** `docker login registry.example.com`
5. **Log Out When Done:** `docker logout registry.example.com`

> Tip: keep `~/.docker/config.json` under source control only if it excludes credentials; use credential helpers otherwise.

---

## 2. Contexts & Environment Switching

Docker contexts let you target local, remote (SSH), or cloud endpoints without reconfiguring env vars.

- **List contexts:** `docker context ls`
- **Inspect details:** `docker context inspect default`
- **Create remote context:**

```bash
docker context create prod --docker "host=ssh://ops@prod.cluster"
```
- **Switch context:** `docker context use prod`
- **Check current:** `docker context show`

Lab: provision a remote VM, create a context via SSH, run `docker ps` to verify remote control.

---

## 3. Images & Registries

- **Search or list local caches:** `docker images`
- **Pull specific tag:** `docker pull redis:7.2-alpine`
- **Build immutable image:** `docker build -t acme/api:1.4.0 .`
- **Tag for another registry:** `docker tag acme/api:1.4.0 ghcr.io/acme/api:1.4.0`
- **Push artifact:** `docker push ghcr.io/acme/api:1.4.0`
- **Remove unused image:** `docker rmi acme/api:1.3.0`
- **Export/import tarballs:**

```bash
docker save ghcr.io/acme/api:1.4.0 -o api.tar
docker load -i api.tar
```

Practice: design a multi-stage Dockerfile that compiles code, copies artifacts into a runtime image, and publishes to GHCR.

---

## 4. Container Lifecycle Commands

| Task | Command |
| --- | --- |
| Run container interactively | `docker run -it --rm ubuntu:24.04 bash` |
| Run detatched service | `docker run -d --name web -p 8080:80 nginx:1.25` |
| List running containers | `docker ps` |
| List all (including exited) | `docker ps -a` |
| Stop gracefully | `docker stop web` |
| Start existing | `docker start web` |
| Remove container | `docker rm web` |
| Copy files | `docker cp backup.sql db:/tmp/backup.sql` |
| Execute command | `docker exec -it db psql -U postgres` |
| Inspect metadata | `docker inspect web` |

Exercise: wrap these commands into Makefile targets (`make up`, `make down`, `make logs`).

---

## 5. Observability, Stats & Cleanup

- **Tail logs:** `docker logs -f web`
- **Live resource usage:** `docker stats`
- **System disk usage:** `docker system df`
- **Aggressive cleanup:** `docker system prune --all --volumes`
- **Container-specific metrics:** `docker inspect --format '{{json .HostConfig}}' web`

Workshop: create an alert when `docker stats` shows memory over 80% for more than 1 minute (use shell scripting + `awk`).

---

## 6. Networking & Volumes

- **List networks:** `docker network ls`
- **Create bridge network:** `docker network create app-net`
- **Connect service to network:** `docker network connect app-net web`
- **List volumes:** `docker volume ls`
- **Create named volume:** `docker volume create pgdata`
- **Inspect volume:** `docker volume inspect pgdata`

Lab: run PostgreSQL with `-v pgdata:/var/lib/postgresql/data` on `app-net`, then attach an app container to query it.

---

## 7. Docker Compose & Multi-Service Apps

- **Launch stack:** `docker compose up -d`
- **View status:** `docker compose ps`
- **Stream logs:** `docker compose logs -f api`
- **Scale service:** `docker compose up -d --scale worker=3`
- **Apply config changes:** `docker compose up -d --build`
- **Remove stack:** `docker compose down --volumes --remove-orphans`

Mini-project: convert the Module 5 capstone into a Compose stack with API, worker, database, and monitoring sidecars.

---

## 8. Security & Policy Checks

- **Scan image for CVEs (example using `docker scan`):** `docker scan acme/api:1.4.0`
- **Least privilege run:** `docker run --cap-drop ALL --read-only ...`
- **Verify signatures (Docker Content Trust example):** `docker trust inspect --pretty ghcr.io/acme/api:1.4.0`

Encourage integrating scans into CI (see Module 6) so every build fails on critical CVEs.

---

## 9. Distribution & Context-Aware Deploys

- **Save runtime stats before switching:** `docker stats --no-stream`
- **Switch back to local context:** `docker context use default`
- **Deploy via remote context:** `docker --context prod compose up -d`
- **Check remote logs:** `docker --context prod compose logs -f ingress`

Capstone challenge: orchestrate a blue/green deployment using two contexts (`prod-blue`, `prod-green`), Compose stacks, and `docker context use` to flip traffic.

---

## Command Checklist (30+ references)

1. `docker version`
2. `docker info`
3. `docker login`
4. `docker logout`
5. `docker context ls`
6. `docker context inspect`
7. `docker context create`
8. `docker context use`
9. `docker context show`
10. `docker images`
11. `docker pull`
12. `docker build`
13. `docker tag`
14. `docker push`
15. `docker rmi`
16. `docker save`
17. `docker load`
18. `docker run`
19. `docker ps`
20. `docker ps -a`
21. `docker stop`
22. `docker start`
23. `docker rm`
24. `docker logs`
25. `docker exec`
26. `docker cp`
27. `docker inspect`
28. `docker stats`
29. `docker system df`
30. `docker system prune`
31. `docker network ls`
32. `docker network create`
33. `docker volume ls`
34. `docker volume create`
35. `docker compose up`
36. `docker compose logs`
37. `docker compose down`
38. `docker scan`

Keep this checklist handy when building labs or troubleshooting production workloads.
