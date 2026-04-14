<div align="center">

# Aurorae Chat API

**A lightweight, real-time WebSocket chat server powered by GPT4All**

[![CI](https://github.com/VelimirMueller/aurorae_ws_chatbot_api/actions/workflows/ws_api_ci.yml/badge.svg)](https://github.com/VelimirMueller/aurorae_ws_chatbot_api/actions/workflows/ws_api_ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/VelimirMueller/aurorae_ws_chatbot_api/blob/main/LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker&logoColor=white)](#-docker)

</div>

---

> **Note:** This project is under active development. Expect breaking changes until a stable release.

## Table of Contents

- [Overview](#overview)
- [Features](#-features)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Docker](#-docker)
- [Configuration](#-configuration)
- [Development](#-development)
- [Project Structure](#-project-structure)
- [Frontend](#-frontend)
- [License](#-license)

## Overview

Aurorae Chat API is an extensible Flask backend that serves real-time chat over WebSockets, powered by [GPT4All](https://github.com/nomic-ai/gpt4all) for local LLM inference. It provides both a WebSocket endpoint for streaming responses and a JSON REST endpoint for simpler integrations.

Pairs with the [Aurorae Chat Frontend](https://github.com/VelimirMueller/aurorae_chat_frontend) for a complete self-hosted chat experience.

## Features

- **Real-time streaming** — WebSocket API for token-by-token chat responses
- **REST endpoint** — JSON API for simple request/response usage
- **Local LLM inference** — GPT4All backend, no external API keys required
- **Configurable** — Environment-based configuration via `.env`
- **Production-ready** — Gunicorn + Docker support out of the box
- **Modular architecture** — Clean separation of concerns for easy extension

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip
- (Optional) Docker & Docker Compose

### Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/VelimirMueller/aurorae_ws_chatbot_api.git
cd aurorae_ws_chatbot_api

python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Start the development server:

```bash
python3 app.py
```

For production, use Gunicorn:

```bash
gunicorn --bind 0.0.0.0:5000 --workers=4 wsgi:app
```

### Docker

Build and run with Docker Compose:

```bash
cp example.Dockerfile Dockerfile
cp example.compose.yml docker-compose.yml
cp example.env .env

# Edit .env and docker-compose.yml to match your setup
docker compose up --build
```

## Configuration

Create a `.env` file in the project root (see `example.env` for reference):

```env
HOST=localhost
PORT=5000
```

## Development

### Linting & Formatting

```bash
# Format code
black src tests
isort src tests

# Lint
flake8 src tests
```

### Testing

```bash
# Run tests with coverage
pytest --cov=src --cov-report=term-missing
```

CI runs linting and tests automatically on every push and pull request. See [`.github/workflows/ws_api_ci.yml`](.github/workflows/ws_api_ci.yml) for details.

## Project Structure

```
aurorae_ws_chatbot_api/
├── .github/workflows/   # CI pipeline
├── src/                 # Application source code
├── templates/           # HTML templates
├── tests/               # Test suite
├── app.py               # Development entry point
├── wsgi.py              # Production WSGI entry point
├── requirements.txt     # Python dependencies
├── example.Dockerfile   # Docker build template
├── example.compose.yml  # Docker Compose template
└── example.env          # Environment variable template
```

## Frontend

Looking for the UI? Check out the companion chat interface:

**[Aurorae Chat Frontend](https://github.com/VelimirMueller/aurorae_chat_frontend)** — A lightweight Vue-based client for interacting with this server.

## License

This project is licensed under the [MIT License](LICENSE).

© 2025 Velimir Müller
