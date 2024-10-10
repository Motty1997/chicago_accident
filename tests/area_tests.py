from repository.area_repository import (get_all_areas, get_count_of_area_accidents, get_reason_of_area_accidents,
                                        get_statistic_area_accidents)


def test_get_all_areas():
    areas = get_all_areas()
    assert len(areas) == 277

def test_get_count_of_area_accidents():
    count = get_count_of_area_accidents('225')
    assert count > 0

def test_get_reason_of_area_accidents():
    reason = get_reason_of_area_accidents('225')
    assert len(reason) > 0

def test_get_statistic_area_accidents():
    statistic = get_statistic_area_accidents('225')
    assert len(statistic) > 0
