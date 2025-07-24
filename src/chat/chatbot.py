from flask import jsonify

from src.model import api_model


def single_response(user_input):
    with api_model.chat_session():
        print("json_fired: /api")
        print("generating_model")

        while True:
            try:
                ai = api_model.generate(str(user_input))

                response = {
                    "data": {
                        "request": user_input,
                        "server_response": "Received request, answering with json",
                        "ai_response": ai,
                    }
                }

                return jsonify(response)

            except Exception as ModelGenerationError:
                print(ModelGenerationError)
                response = {"error": {"error": str(ModelGenerationError)}}

                return jsonify(response)


def chat_session(user_input, model, socket):
    if user_input == "exit":
        socket.send("printing previous chat session, restarting session")
        socket.send(model.current_chat_session)
    else:
        print("generating websocket message: ")
        ai_answer = model.generate(user_input)
        socket.send(ai_answer)
