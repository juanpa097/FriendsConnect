from enum import Enum


class ActivityQuerys(Enum):
    QUERY_ACTIVITY_LIST = 'SELECT * ' \
                          'FROM app_activity as activity' \
                          ' LEFT JOIN app_activityuser as activityuser' \
                          ' ON activity.id = activityuser.activity_id'

    @classmethod
    def get_query_activity_list(cls):
        return cls.QUERY_ACTIVITY_LIST.value
