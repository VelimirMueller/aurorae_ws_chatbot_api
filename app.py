from dotenv import dotenv_values
# Initialize Flask
from flask import Flask
from flask_cors import CORS
from flask_sock import Sock

# Initialize routes and api
from src.routes import home_bp
from src.api import json_api_bp

# Initialize model
from src.model import ws_model
from src.chat import chat_session

# load ..env variables
environ = dotenv_values('.env')

# Initialize basic flask app with websockets and cors headers set
app = Flask(__name__)
cors = CORS(app)
print('app initialised')

# Initialize routes
app.register_blueprint(home_bp)
print('routes initialised')

# Initialize API
app.register_blueprint(json_api_bp)
print('api initialised')

# Initialize websocket
sock = Sock(app)


@sock.route('/api_ws')
def api_ws(sock):
    with ws_model.chat_session():
        while True:
            chat_session(sock.receive(), ws_model, sock)


print('websocket initialised: ' + str(sock))

# Run automatically when executed as script but not when imported as module
if __name__ == "__main__":
    app.run(host=environ['HOST'], port=environ['PORT'])
