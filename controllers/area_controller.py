from flask import Blueprint, jsonify, request
from repository.area_repository import get_count_of_area_accidents, get_reason_of_area_accidents, \
    get_statistic_area_accidents


areas = Blueprint('area', __name__)


@areas.route('/count', methods=['GET'])
def get_count_of_area_accidents_route():
    area = request.args.get('area')
    if not area:
        return jsonify({"error": "Area parameter is required"}), 400
    result = get_count_of_area_accidents(area)
    if result is None:
        return jsonify({"error": f"No data found for area: {area}"}), 404
    return jsonify({"total_injuries": result})


@areas.route('/contributing-factors', methods=['GET'])
def get_reason_of_area_accidents_route():
    area = request.args.get('area')
    if not area:
        return jsonify({"error": "Area parameter is required"}), 400
    result = get_reason_of_area_accidents(area)
    if result is None:
        return jsonify({"error": f"No data found for area: {area}"}), 404
    return jsonify({"contributing_factors": result})


@areas.route('/statistics', methods=['GET'])
def get_statistic_area_accidents_route():
    area = request.args.get('area')
    if not area:
        return jsonify({"error": "Area parameter is required"}), 400
    result = get_statistic_area_accidents(area)
    if result is None:
        return jsonify({"error": f"No data found for area: {area}"}), 404
    return jsonify({"injuries": result})