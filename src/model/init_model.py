from dotenv import dotenv_values
from gpt4all import GPT4All

environ = dotenv_values(".env")

api_model = GPT4All(model_name=environ["MODEL_API"], model_path="./src/model/binaries")
ws_model = GPT4All(model_name=environ["MODEL_WS"], model_path="./src/model/binaries")
