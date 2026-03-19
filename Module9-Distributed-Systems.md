# Distributed Systems (Module 9)

---

## 📚 Overview

Distributed systems are collections of independent computers that appear to the user as a **single coherent system**.  They enable **scalability**, **fault‑tolerance**, and **geographic distribution**—key requirements for modern cloud‑native applications.

In this module we will:

1. **Explain core challenges** (latency, partial failures, concurrency, security).
2. **Explore consistency models** and the **CAP theorem**.
3. **Dive into consensus algorithms** (Raft, Paxos) and coordination services.
4. **Cover communication patterns** (RPC, gRPC, REST, messaging queues, WebSockets).
5. **Design a micro‑service‑based application** using Docker, Docker‑Compose, and a service‑discovery tool.
6. **Implement practical examples** in Python (gRPC, etcd client, RabbitMQ producer/consumer).
7. **Discuss monitoring, testing, and deployment** best‑practices.

---

## 1️⃣ Core Challenges of Distributed Systems

| Challenge | Why it matters | Typical mitigation |
|-----------|----------------|--------------------|
| **Network latency & bandwidth** | Remote calls are slower than in‑process calls. | Caching, request coalescing, locality‑aware placement. |
| **Partial failures** | Some nodes may fail while others keep working. | Heartbeats, retries, circuit‑breakers, graceful degradation. |
| **Concurrency & ordering** | Multiple nodes may update the same data simultaneously. | Consensus protocols, version vectors, conflict‑free replicated data types (CRDTs). |
| **Data partitioning & replication** | Need to split data across nodes while keeping copies consistent. | Sharding, quorum reads/writes, eventual consistency. |
| **Security** | Data in transit and at rest must be protected. | Mutual TLS, token‑based auth (OAuth2/JWT), zero‑trust networking. |
| **Observability** | Hard to debug a system spread across many machines. | Distributed tracing (OpenTelemetry), metrics (Prometheus), logs aggregation (ELK). |

---

## 2️⃣ Consistency Models & the CAP Theorem

### 2.1 Consistency Models

| Model | Guarantees | Typical use‑cases |
|-------|------------|-------------------|
| **Strong consistency** | All reads see the latest write (linearizability). | Financial transactions, inventory systems. |
| **Sequential consistency** | Operations appear in a total order that respects program order per client. | Multi‑player games where order matters but latency can be tolerated. |
| **Read‑your‑writes** | A client always sees its own writes. | User‑profile updates. |
| **Eventual consistency** | Updates propagate asynchronously; eventually all replicas converge. | Social feeds, DNS, caching layers. |
| **Causal consistency** | Writes that are causally related are seen in order; concurrent writes may be seen in any order. | Collaborative editing (Google Docs). |

### 2.2 CAP Theorem

> **C**onsistency, **A**vailability, **P**artition tolerance – you can only have two of the three in a distributed system.

| System | Guarantees | Example |
|--------|------------|---------|
| **CP** (Consistency + Partition tolerance) | Strong consistency, may sacrifice availability during partitions. | Traditional relational DBs (PostgreSQL with synchronous replication). |
| **AP** (Availability + Partition tolerance) | Always available, may return stale data. | DynamoDB, Cassandra (eventual consistency). |
| **CA** (Consistency + Availability) – *Impossible* in the presence of network partitions. |

---

## 3️⃣ Consensus & Coordination Services

### 3.1 Consensus Algorithms

* **Paxos** – The classic algorithm; complex to implement correctly.
* **Raft** – Simpler, leader‑based protocol; widely used (etcd, Consul, RethinkDB).
* **Zab** – ZooKeeper’s protocol, similar to Paxos.

#### Raft in a nutshell
1. **Leader election** – Nodes vote; the candidate with majority becomes leader.
2. **Log replication** – Leader appends entries to its log and replicates to followers.
3. **Safety** – A majority must agree before a log entry is committed.

### 3.2 Coordination Services

| Service | Primary purpose | Language bindings |
|---------|----------------|-------------------|
| **ZooKeeper** | Configuration, naming, leader election, distributed locks. | Java, C, Python (`kazoo`). |
| **etcd** | Key‑value store with strong consistency (Raft). | Go, Python (`etcd3`), Java (`jetcd`). |
| **Consul** | Service discovery, health checking, KV store. | Go, Python (`python-consul2`), Java (`consul-client`). |

---

## 4️⃣ Communication Patterns

### 4.1 Synchronous RPC
* **gRPC** – HTTP/2, protobuf, bi‑directional streaming.
* **Thrift** – Multi‑language, supports many transports.

### 4.2 Asynchronous Messaging
* **Message queues** – RabbitMQ, Apache Kafka, NATS.
* **Pub/Sub** – Google Pub/Sub, AWS SNS/SQS.

### 4.3 REST & HTTP APIs
* Simpler, language‑agnostic, cache‑friendly.
* Use OpenAPI/Swagger for contract‑first design.

### 4.4 Real‑time WebSockets
* Low‑latency, full‑duplex communication for chat, live dashboards.

---

## 5️⃣ Microservices Architecture

### 5.1 Core Patterns
| Pattern | Description | Typical tooling |
|---------|-------------|-----------------|
| **Service Discovery** | Dynamically locate service instances. | Consul, etcd, Eureka, Kubernetes DNS. |
| **API Gateway** | Single entry point, request routing, auth, rate‑limiting. | Kong, Traefik, Envoy, AWS API GW. |
| **Circuit Breaker** | Prevent cascading failures when a downstream service is unhealthy. | Hystrix (Java), Polly (.NET), Resilience4j, `pybreaker`. |
| **Sidecar Proxy** | Deploy a proxy alongside each service for observability & security. | Envoy, Linkerd, Istio. |
| **Saga / Orchestration** | Manage distributed transactions without two‑phase commit. | Temporal, Camunda, custom orchestrator. |

### 5.2 Docker‑Compose Example (3‑service app)

```yaml
# docker-compose.yml – a minimal microservice stack
version: "3.9"
services:
  api:
    build: ./api            # Flask‑based HTTP API
    ports:
      - "5000:5000"
    environment:
      - SERVICE_NAME=api
    depends_on:
      - redis
      - consul
    command: python -m api.main

  worker:
    build: ./worker        # Background consumer (RabbitMQ)
    environment:
      - SERVICE_NAME=worker
    depends_on:
      - rabbitmq
      - consul
    command: python -m worker.main

  consul:
    image: hashicorp/consul:1.15
    command: agent -dev -client=0.0.0.0
    ports:
      - "8500:8500"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  rabbitmq:
    image: rabbitmq:3-management
    ports:
      - "5672:5672"
      - "15672:15672"
```

*Each service registers itself with Consul on startup (see code snippets below).*

---

## 6️⃣ Practical Code Examples (Python)

### 6.1 gRPC Hello World

**proto file (`hello.proto`)**
```proto
syntax = "proto3";
package hello;

service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}
```

**Server (`server.py`)**
```python
import grpc
from concurrent import futures
import hello_pb2, hello_pb2_grpc

class GreeterServicer(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloReply(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
```

**Client (`client.py`)**
```python
import grpc
import hello_pb2, hello_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name='Nanobot'))
        print('Server replied:', response.message)

if __name__ == '__main__':
    run()
```

> **Tip:** Use `python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto` to generate the Python stubs.

---

### 6.2 etcd Key‑Value Store Interaction

```python
import etcd3
import time

# Connect to a local etcd node (default port 2379)
client = etcd3.client(host='localhost', port=2379)

# Put a key
client.put('config/feature_flag', 'true')
print('Wrote key')

# Get the key
value, meta = client.get('config/feature_flag')
print('Read value:', value.decode())

# Watch for changes (runs in background thread)
def watch_callback(event):
    print('Watch event:', event.key.decode(), event.value.decode())

watch_id = client.add_watch_callback('config/feature_flag', watch_callback)

# Simulate a change after a few seconds
time.sleep(3)
client.put('config/feature_flag', 'false')

# Keep the script alive briefly to see the watch event
time.sleep(2)
client.cancel_watch(watch_id)
```

---

### 6.3 RabbitMQ Producer / Consumer (Pub/Sub)

**Producer (`producer.py`)**
```python
import pika
import json
import uuid

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

msg = {'id': str(uuid.uuid4()), 'level': 'info', 'msg': 'Hello from Nanobot'}
channel.basic_publish(exchange='logs', routing_key='', body=json.dumps(msg))
print('Sent:', msg)
connection.close()
```

**Consumer (`consumer.py`)**
```python
import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_set('logs', exchange_type='fanout')
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)

print('Waiting for messages...')

def callback(ch, method, properties, body):
    msg = json.loads(body)
    print('Received:', msg)

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
```

---

### 6.4 Service Registration with Consul (Flask API)

```python
import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({'status': 'ok'})

def register_service():
    consul_host = os.getenv('CONSUL_HOST', 'localhost')
    service_id = f"api-{os.getpid()}"
    payload = {
        "ID": service_id,
        "Name": "api",
        "Address": "127.0.0.1",
        "Port": 5000,
        "Check": {
            "HTTP": f"http://127.0.0.1:5000/ping",
            "Interval": "10s"
        }
    }
    r = requests.put(f'http://{consul_host}:8500/v1/agent/service/register', json=payload)
    print('Consul registration status:', r.status_code)

if __name__ == '__main__':
    register_service()
    app.run(host='0.0.0.0', port=5000)
```

---

## 7️⃣ Observability & Testing

| Concern | Tooling |
|---------|---------|
| **Metrics** | Prometheus (exporters for Python: `prometheus_client`). |
| **Tracing** | OpenTelemetry SDK → Jaeger or Zipkin UI. |
| **Logging** | Structured JSON logs → Loki + Grafana. |
| **Chaos testing** | `chaos-mesh`, `Gremlin`, or simple `tc` network delay scripts. |
| **Contract testing** | Pact (consumer‑driven contracts) for REST/gRPC. |

### Example: Exposing Prometheus metrics in Flask
```python
from prometheus_client import Counter, generate_latest
from flask import Flask, Response

app = Flask(__name__)
REQUESTS = Counter('http_requests_total', 'Total HTTP requests')

@app.before_request
def before():
    REQUESTS.inc()

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')
```

---

## 8️⃣ Deployment on Kubernetes (High‑level)

```yaml
# k8s/deployment.yaml – Deploy the API service with a sidecar Envoy proxy
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: myorg/api:latest
          ports:
            - containerPort: 5000
        - name: envoy
          image: envoyproxy/envoy:v1.28-latest
          args: ["-c", "/etc/envoy/envoy.yaml"]
          volumeMounts:
            - name: envoy-config
              mountPath: /etc/envoy
      volumes:
        - name: envoy-config
          configMap:
            name: envoy-config
---
apiVersion: v1
kind: Service
metadata:
  name: api
spec:
  selector:
    app: api
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
```

*The sidecar proxy handles TLS termination, retries, and observability without modifying the application code.*

---

## ✅ Summary Checklist

- [ ] Understand latency, partial failures, and concurrency.
- [ ] Distinguish consistency models and apply CAP theorem reasoning.
- [ ] Explain Raft vs. Paxos and when to use etcd/Consul/ZooKeeper.
- [ ] Choose appropriate communication style (gRPC, REST, messaging).
- [ ] Build a Docker‑Compose microservice stack with service discovery.
- [ ] Write a simple gRPC service, an etcd client, and a RabbitMQ producer/consumer.
- [ ] Add Prometheus metrics and OpenTelemetry tracing.
- [ ] Deploy to Kubernetes with sidecar proxies for resilience.

---

*Feel free to contribute improvements via pull‑requests. Happy building!*
## Expanded Content

### In‑Depth Overview
This module provides a comprehensive deep‑dive into the subject, covering theoretical foundations, practical implementations, and industry‑standard best practices.

### Detailed Topics
- Core concepts with formal definitions and mathematical underpinnings where applicable.
- Real‑world use‑cases and case studies.
- Comparative analysis of alternative approaches and trade‑offs.

### Hands‑On Labs
1. **Lab 1:** Implement a reference solution from scratch, focusing on clean architecture and testability.
2. **Lab 2:** Extend the solution with advanced features, optimizing for performance and scalability.
3. **Lab 3:** Deploy the solution using CI/CD pipelines and containerization.

### Advanced Topics
- Performance profiling and optimization techniques.
- Security considerations and threat modeling.
- Integration with cloud services and orchestration tools.

### Further Reading
- Authoritative textbooks, research papers, and official documentation links.
- Community resources, tutorials, and open‑source projects.

### Summary & Takeaways
A concise recap of key points, best‑practice guidelines, and next‑step recommendations for continued learning.

