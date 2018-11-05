from enum import Enum


class ActivityQuerys(Enum):
    QUERY_ACTIVITY_LIST = 'SELECT description, begin_date, end_date, ' \
                          'activity.id, ' \
                          'location, max_participants, name, ' \
                          'image.file as \'image\', ' \
                          'activityuser.user_id as author, ' \
                          'date_created, visibility ' \
                          'FROM app_activity as activity ' \
                          'LEFT JOIN app_activityuser as activityuser ' \
                          'ON activity.id = activityuser.activity_id ' \
                          'LEFT JOIN app_image as image ' \
                          'ON activity.id = image.id ' \
                          'LEFT JOIN app_user as user ' \
                          'ON activityuser.user_id = user.id' \
                          'WHERE activityuser.rol = 0 '

    @classmethod
    def get_query_activity_list(cls):
        return cls.QUERY_ACTIVITY_LIST.value
