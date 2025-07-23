from gpt4all import GPT4All
from dotenv import dotenv_values

environ = dotenv_values('.env')

api_model = GPT4All(model_name=environ['MODEL_API'], model_path='./src/model/binaries')
ws_model = GPT4All(model_name=environ['MODEL_WS'], model_path='./src/model/binaries')
