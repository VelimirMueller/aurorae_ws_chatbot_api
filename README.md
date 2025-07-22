### Python Flask GTP4ALL powered websocket chat client (still in development)

- define port and host in .env
- for docker usage may need to adjust example.Dockerfile and example.compose.yml 

usage:

install python 3.10 first
```bash
 sudo apt install python3.10 python3.10-venv python3.10-dev
```

- open terminal and navigate to the app's root directory
- create a python3 virtual environment and activate it
- now run in terminal:

`pip install -r requirements.txt`

run as python scrippt:

`python3 app.py`

run with gunicorn:

`gunicorn --bind 0.0.0.0:5000 --workers="4" wsgi:app`

(you can use another local address or port if needed or wanted)

Check out the aurorae frontend client here: https://github.com/VelimirMueller/aurorae-frontend
