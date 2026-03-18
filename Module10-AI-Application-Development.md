# AI Application Development with Python

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