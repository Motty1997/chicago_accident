from database.connect import daily, weekly, monthly


def count_accident_by_day(date, area):
    count = daily.find_one({'date': date, 'area': area}).get('total_accidents', 0)
    if count is None:
        return 0
    return count


def count_accident_by_week(date, area):
    count = weekly.find_one({'week_start': date, 'area': area}).get('total_accidents', 0)
    if count is None:
        return 0
    return count


def count_accident_by_month(month, area):
    count = monthly.find_one({'month': month, 'area': area}).get('total_accidents', 0)
    if count is None:
        return 0
    return count
