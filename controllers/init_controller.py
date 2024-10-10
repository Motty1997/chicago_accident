from flask import Blueprint, jsonify
from repository.csv_repository import init_accidents


init = Blueprint('init', __name__)


@init.route('/', methods=['POST'])
def init_accidents_route():
    result = init_accidents()
    if result is None:
        return jsonify({"error": " Not completed the query"}), 400
    return jsonify({"Success": "Its completed successfully"})
