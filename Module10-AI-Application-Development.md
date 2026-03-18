# AI Application Development with Python

## Expanded Content

### Architecture Overview

- **Client Layer**: CLI or web UI built with `argparse` or `FastAPI`.
- **Service Layer**: Python modules that wrap LLM provider APIs, handling authentication, request throttling, and response parsing.
- **Model Layer**: Prompt templates, few‑shot examples, and function‑calling schemas stored as JSON/YAML for easy reuse.
- **Deployment Layer**: Dockerfile, `docker-compose` for multi‑service setups (API + Ollama), and CI pipelines for automated testing.

### Detailed Code Samples

#### 1. Generic LLM Client Wrapper
```python
import os, httpx
from typing import Any, Dict

class LLMClient:
    def __init__(self, base_url: str, api_key: str, model: str):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.model = model
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        self.client = httpx.Client(timeout=30.0)

    def chat(self, messages: list[Dict[str, str]], **kwargs) -> Dict[str, Any]:
        payload = {"model": self.model, "messages": messages, **kwargs}
        resp = self.client.post(f"{self.base_url}/v1/chat/completions", json=payload, headers=self.headers)
        resp.raise_for_status()
        return resp.json()
```

#### 2. OpenAI Specific Helper
```python
from .base import LLMClient

openai = LLMClient(
    base_url="https://api.openai.com",
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-4o-mini",
)

response = openai.chat([
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain quantum computing in one paragraph."},
])
print(response["choices"][0]["message"]["content"])  # noqa: E501
```

#### 3. Streaming Responses (OpenAI)
```python
import sys
for chunk in openai.client.stream("/v1/chat/completions", json={"model": "gpt-4o-mini", "messages": [{"role": "user", "content": "Write a haiku about AI."}], "stream": True}, headers=openai.headers):
    if data := chunk.get("choices")[0].get("delta").get("content"):
        sys.stdout.write(data)
        sys.stdout.flush()
```

### Deployment with Ollama (Local Model)
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

```yaml
# docker-compose.yml
version: "3.9"
services:
  ollama:
    image: ollama/ollama
    ports:
      - "11434:11434"
  app:
    build: .
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
    depends_on:
      - ollama
    ports:
      - "8000:8000"
```

### Security & Privacy Checklist
- Store API keys in `.env` and never commit them.
- Use rate‑limit back‑off and exponential retries.
- Validate and sanitize user inputs before sending to LLMs.
- Log only non‑PII content; redact sensitive fields.
- For production, run behind a firewall and enable TLS on any custom endpoints.

### Testing Strategies
- **Unit Tests**: Mock `httpx` responses with `respx`.
- **Integration Tests**: Spin up a local Ollama container and run end‑to‑end queries.
- **Contract Tests**: Verify that the JSON schema of responses matches expected structures.

### Suggested Further Reading
- OpenAI Function Calling guide
- Retrieval‑Augmented Generation (RAG) patterns
- Prompt engineering best practices (Chain‑of‑Thought, ReAct)

---
*This module is a work‑in‑progress. Contributions are welcome!*

## Overview

This module covers how to build intelligent applications in Python using large‑language model (LLM) APIs from providers such as **OpenAI**, **Google Gemini**, **OpenRouter**, and **Ollama**. You will learn to:

- Authenticate and call LLM endpoints securely.
- Prompt‑engineer for reliable, controllable outputs.
- Stream responses and handle token limits.
- Combine multiple models (e.g., retrieval‑augmented generation).
- Deploy locally with Ollama or in the cloud with managed APIs.
- Build simple UI/CLI wrappers and integrate with FastAPI or Flask.

## Learning Objectives

1. Set up API keys and environment variables for each provider.
2. Write reusable Python client wrappers using `httpx`/`requests`.
3. Implement prompt templates, few‑shot examples, and function calling.
4. Stream and batch‑process completions, handling errors and rate limits.
5. Build a small end‑to‑end AI app (e.g., a chatbot or code‑assistant).
6. Containerize the app with Docker and optionally run locally with Ollama.

## Suggested Labs

- **Lab 1:** Call OpenAI's `chat/completions` endpoint to build a simple Q&A bot.
- **Lab 2:** Switch the same code to Gemini's `generateContent` API.
- **Lab 3:** Use OpenRouter to route prompts to multiple models and compare costs/latency.
- **Lab 4:** Run an Ollama model locally and integrate it with a FastAPI service.
- **Lab 5:** Add function calling / tool use (e.g., a weather lookup) with OpenAI.

## Resources

- OpenAI API docs: https://platform.openai.com/docs/api-reference
- Google Gemini API docs: https://ai.google.dev/gemini-api/docs
- OpenRouter API docs: https://openrouter.ai/docs
- Ollama docs: https://ollama.com/docs
- Python libraries: `httpx`, `pydantic`, `fastapi`, `python-dotenv`

---
*This module is a work‑in‑progress. Contributions are welcome!*