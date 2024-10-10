from repository.times_repository import count_accident_by_day, count_accident_by_week, count_accident_by_month


def test_count_accident_by_day():
    count = count_accident_by_day('2023-09-05', '225')
    assert count


def test_count_accident_by_week():
    count = count_accident_by_week('2023-09-05', '225')
    assert count


def test_count_accident_by_month():
    count = count_accident_by_month('9', '225')
    assert count
