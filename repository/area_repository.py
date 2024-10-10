from bson import ObjectId
from database.connect import areas


def get_all_areas():
    return areas.find().to_list()

def get_count_of_area_accidents(area):
    count = areas.find_one({'area': area})['injuries']['total']
    return count

def get_reason_of_area_accidents(area):
    reason = areas.find_one({'area': area})['contributing_factors']
    return reason

def get_statistic_area_accidents(area):
    statistic = areas.find_one({'area': area})['injuries']
    return statistic
