from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest

from src.chat import single_response

json_api_bp = Blueprint("json_api", __name__)


@json_api_bp.route("/api", methods=["POST"])
def api():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    try:
        request_data = request.get_json()
        if request_data is None:
            return jsonify({"error": "Empty or malformed JSON"}), 400
    except BadRequest:
        return jsonify({"error": "Malformed JSON"}), 400

    return single_response(request_data)
