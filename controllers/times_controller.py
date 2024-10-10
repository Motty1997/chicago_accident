from flask import Blueprint, jsonify, request
from repository.times_repository import count_accident_by_day, count_accident_by_week, count_accident_by_month


times = Blueprint('time', __name__)


@times.route('/day', methods=['GET'])
def count_accident_by_day_route():
    date = request.args.get('date')
    area = request.args.get('area')
    if date is None or area is None:
        return jsonify({"error": "One of 'date' or 'area' parameters are required"}), 400
    result = count_accident_by_day(date, area)
    if result is None:
        return jsonify({"error": f"No data found for date: {date} and area: {area}"}), 404
    return jsonify({"count": result})


@times.route('/week', methods=['GET'])
def count_accident_by_week_route():
    week_start = request.args.get('week_start')
    area = request.args.get('area')
    if not week_start or not area:
        return jsonify({"error": "One of 'week_start' or 'area' parameters are required"}), 400
    result = count_accident_by_week(week_start, area)
    if not result:
        return jsonify({"error": f"No data found for week_start: {week_start} and area: {area}"}), 404
    return jsonify({"count": result})


@times.route('/month', methods=['GET'])
def count_accident_by_month_route():
    month = request.args.get('month')
    area = request.args.get('area')
    if not month or not area:
        return jsonify({"error": "One of 'month' or 'area' parameters are required"}), 400
    result = count_accident_by_month(month,area)
    if not result:
        return jsonify({"error": f"No data found for month: {month} and area: {area}"}), 404
    return jsonify({"count": result})
