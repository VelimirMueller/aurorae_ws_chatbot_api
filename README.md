### Python Flask GTP4ALL powered websocket chat client

- define port and host in .env
- for docker usage may need to adjust example.Dockerfile and example.compose.yml 

usage:

- open terminal and navigate to the app's root directory
- create a python3 virtual environment and activate it
- now run in terminal:

`pip install -r requirements.txt`

run as python scrippt:

`python3 app.py`

run with gunicorn:

`gunicorn --bind 0.0.0.0:5000 --workers="1" wsgi:app`

(you can use another local address or port if needed or wanted)


LICENSE:

MIT License

Copyright (c) 2023 Velimir Müller

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
