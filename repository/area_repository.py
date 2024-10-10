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


def create_index():
    areas.create_index({'area': 1})
    executionStats = (areas
                      .find({'area': '225'})
                      .hint({'area': 1})
                      .explain()['executionStats'])
    return executionStats
print(create_index())

def drop_index():
    areas.drop_indexes()
    executionStats = (areas
                       .find({'area': '225'})
                       .explain()['executionStats'])
    return executionStats
print(drop_index())
