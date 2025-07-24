## 🧠 Aurorae Chat API 
#### Flask + GPT4All WebSocket Chat Server
___
🚧 **Project is in active development**  
A lightweight, extensible Flask backend serving real-time chat over WebSockets, powered by [GPT4All](https://github.com/nomic-ai/gpt4all). Pairs perfectly with the [Aurorae frontend client](https://github.com/VelimirMueller/aurorae-frontend).

---

## ✨ Features

- ✅ WebSocket API for real-time streaming chat
- ✅ JSON API endpoint for simple REST usage
- ✅ GTP4All backend integration (local LLMs)
- ✅ Configurable via `.env` file
- ✅ Python 3.10+ support
- ✅ Docker & `gunicorn` compatible
- ✅ Modular & extensible architecture

---

## ⚙️ Setup & Usage

### 1. 📦 Python Installation

Install Python 3.10+ and dependencies:

```bash
 sudo apt install python3.10 python3.10-venv python3.10-dev
````

Clone the repo and create a virtual environment:
```bash
 git clone https://github.com/VelimirMueller/aurorae_ws_chatbot_api.git
 cd aurorae_ws_chatbot_api
 python3.10 -m venv .venv
 source .venv/bin/activate
 pip install -r requirements.txt
```

Start the server:
```bash
  python3 app.py
```

Or with gunicorn for production:
```bash
  gunicorn --bind 0.0.0.0:5000 --workers=4 wsgi:app
```
Configure the address/port in your .env file if needed.


## 2. 🐳 Docker (Optional)

### Use Docker for containerized development:

```bash
  cp example.Dockerfile Dockerfile
  cp example.compose.yml docker-compose.yml

  # Customize .env and docker-compose if needed
  docker compose up --build
```

## 3. 🔧 Configuration
   
### Create a .env file in the project root:

```.env
  HOST=localhost
  PORT=5000
```

## 4. 🧪 Development

### Linting, Formatting & Testing:

```bash
  # Format with Black & isort
 black src tests
 isort src tests
 
 # Lint with flake8
 flake8 src tests
 
 # Run tests
 pytest
```

## 🌐 Frontend

### Looking for the UI?

A lightweight chat interface to interact easily with the ws server

👉 (Aurorae Chat Frontend -Vue)[https://github.com/VelimirMueller/aurorae_chat_frontend]


## 📄 License

MIT License © 2025 Velimir Müller
