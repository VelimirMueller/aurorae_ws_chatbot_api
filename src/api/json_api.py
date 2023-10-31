from flask import Blueprint, request
from src.chat import single_response

json_api_bp = Blueprint('json_api', __name__)


@json_api_bp.route('/api', methods=['POST'])
def api():
    request_data = request.get_json()
    return single_response(request_data)
