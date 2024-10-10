from database.connect import daily, weekly, monthly


def count_accident_by_day(date, area):
    count = daily.find({'data': date, 'area': area})['injuries']['total_accidents']
    return count


def count_accident_by_week(date, area):
    count = weekly.find({'week_start': date, 'area': area})['injuries']['total_accidents']
    return count


def count_accident_by_month(month, area):
    count = monthly.find({'month': month, 'area': area})['injuries']['total_accidents']
    return count
