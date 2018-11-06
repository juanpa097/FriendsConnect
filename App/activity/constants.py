from enum import Enum


class ActivityQuerys(Enum):
    QUERY_ACTIVITY_LIST_FIRST_PART = \
        '  SELECT *,' \
        'S4.user_suscribe_id is not NULL as ' \
        'is_current_user_subscribed ' \
        ' FROM ' \
        '( ' \
        ' SELECT description, begin_date, end_date, ' \
        ' activity.id, location, ' \
        '   max_participants, name, imageT.file as image, ' \
        'userd.username as author, date_created, ' \
        'visibility ' \
        '    FROM "App_activity" as activity ' \
        '    LEFT JOIN "App_activityuser" as activityuser ' \
        '    ON activity.id = activityuser.activity_id ' \
        '    LEFT JOIN "App_image" as imageT ' \
        '    ON activity.image_id = imageT.id ' \
        '    LEFT JOIN "auth_user" as userd ' \
        '    ON activityuser.user_id = userd.id ' \
        '    WHERE activityuser.rol = 0 ' \
        ') as S1 ' \
        'LEFT JOIN ' \
        '( ' \
        'SELECT  activity.id as id , COUNT(' \
        'activityuser.activity_id) as participants ' \
        '	FROM "App_activity" as activity ' \
        '	LEFT JOIN "App_activityuser" as activityuser ' \
        '	ON activity.id = activityuser.activity_id ' \
        '	GROUP BY activity.id ' \
        ') as S2 ' \
        'ON S1.id = S2.id ' \
        'LEFT JOIN ' \
        '( ' \
        'SELECT  activity.id as id , COUNT(' \
        'commentT.activity_id) as comments ' \
        '	FROM "App_activity" as activity ' \
        '	LEFT JOIN "App_comment" as commentT ' \
        '	ON activity.id = commentT.activity_id ' \
        '   GROUP BY activity.id ' \
        ')' \
        ' as S3 ON S1.id = S3.id ' \
        'LEFT JOIN ' \
        '( ' \
        '    select activity.id as id,' \
        ' activityuser.user_id  as user_suscribe_id ' \
        'FROM "App_activity" as activity ' \
        'LEFT JOIN "App_activityuser" as activityuser ' \
        'ON activity.id = activityuser.activity_id ' \
        'WHERE activityuser.user_id = '
    QUERY_ACTIVITY_LIST_SECOND_PART = \
        ' GROUP BY activity.id, activityuser.user_id ' \
        ') as S4 ' \
        'ON ' \
        'S1.id = S4.id '

    @classmethod
    def get_query_activity_list(cls, user_id):
        user_id = int(user_id).__str__()
        return cls.QUERY_ACTIVITY_LIST_FIRST_PART.value + \
               user_id + \
               cls.QUERY_ACTIVITY_LIST_SECOND_PART.value

    QUERY_ACTIVITY_LIST_BY_USER_FIRST_PART = \
        '  SELECT *,' \
        'S4.user_suscribe_id is not NULL as ' \
        'is_current_user_subscribed ' \
        ' FROM ' \
        '( ' \
        '    select activity.id as id,' \
        ' activityuser.user_id  as user_suscribe_id ' \
        'FROM "App_activity" as activity ' \
        'LEFT JOIN "App_activityuser" as activityuser ' \
        'ON activity.id = activityuser.activity_id ' \
        'WHERE activityuser.user_id = '

    QUERY_ACTIVITY_LIST_BY_USER_SECOND_PART = \
        ') as S4 ' \
        'LEFT JOIN ' \
        '( ' \
        ' SELECT description, begin_date, end_date, ' \
        ' activity.id, location, ' \
        '   max_participants, name, imageT.file as image, ' \
        'userd.username as author, date_created, ' \
        'visibility ' \
        '    FROM "App_activity" as activity ' \
        '    LEFT JOIN "App_activityuser" as activityuser ' \
        '    ON activity.id = activityuser.activity_id ' \
        '    LEFT JOIN "App_image" as imageT ' \
        '    ON activity.image_id = imageT.id ' \
        '    LEFT JOIN "auth_user" as userd ' \
        '    ON activityuser.user_id = userd.id ' \
        '    WHERE activityuser.rol = 0 ' \
        ') as S1 ' \
        ' ON S1.id = S4.id ' \
        'LEFT JOIN ' \
        '( ' \
        'SELECT  activity.id as id , COUNT(' \
        'activityuser.activity_id) as participants ' \
        '	FROM "App_activity" as activity ' \
        '	LEFT JOIN "App_activityuser" as activityuser ' \
        '	ON activity.id = activityuser.activity_id ' \
        '	GROUP BY activity.id ' \
        ') as S2 ' \
        'ON S1.id = S2.id ' \
        'LEFT JOIN ' \
        '( ' \
        'SELECT  activity.id as id , COUNT(' \
        'commentT.activity_id) as comments ' \
        '	FROM "App_activity" as activity ' \
        '	LEFT JOIN "App_comment" as commentT ' \
        '	ON activity.id = commentT.activity_id ' \
        '   GROUP BY activity.id ' \
        ')' \
        ' as S3 ON S1.id = S3.id '

    @classmethod
    def get_query_activity_list_by_user(cls, user_id):
        user_id = int(user_id).__str__()
        return cls.QUERY_ACTIVITY_LIST_BY_USER_FIRST_PART.value + \
            user_id + \
            cls.QUERY_ACTIVITY_LIST_BY_USER_SECOND_PART.value

    QUERY_ACTIVITY_LIST_BY_USER_OWN_FIRST_PART = \
        '  SELECT *,' \
        'S4.user_suscribe_id is not NULL as ' \
        'is_current_user_subscribed ' \
        ' FROM ' \
        '( ' \
        '    select activity.id as id,' \
        ' activityuser.user_id  as user_suscribe_id ' \
        'FROM "App_activity" as activity ' \
        'LEFT JOIN "App_activityuser" as activityuser ' \
        'ON activity.id = activityuser.activity_id ' \
        'WHERE activityuser.user_id = '

    QUERY_ACTIVITY_LIST_BY_USER_OWN_SECOND_PART = \
        ' AND activityuser.rol = 0 ' \
        ') as S4 ' \
        'LEFT JOIN ' \
        '( ' \
        ' SELECT description, begin_date, end_date, ' \
        ' activity.id, location, ' \
        '   max_participants, name, imageT.file as image, ' \
        'userd.username as author, date_created, ' \
        'visibility ' \
        '    FROM "App_activity" as activity ' \
        '    LEFT JOIN "App_activityuser" as activityuser ' \
        '    ON activity.id = activityuser.activity_id ' \
        '    LEFT JOIN "App_image" as imageT ' \
        '    ON activity.image_id = imageT.id ' \
        '    LEFT JOIN "auth_user" as userd ' \
        '    ON activityuser.user_id = userd.id ' \
        '    WHERE activityuser.rol = 0 ' \
        ') as S1 ' \
        ' ON S1.id = S4.id ' \
        'LEFT JOIN ' \
        '( ' \
        'SELECT  activity.id as id , COUNT(' \
        'activityuser.activity_id) as participants ' \
        '	FROM "App_activity" as activity ' \
        '	LEFT JOIN "App_activityuser" as activityuser ' \
        '	ON activity.id = activityuser.activity_id ' \
        '	GROUP BY activity.id ' \
        ') as S2 ' \
        'ON S1.id = S2.id ' \
        'LEFT JOIN ' \
        '( ' \
        'SELECT  activity.id as id , COUNT(' \
        'commentT.activity_id) as comments ' \
        '	FROM "App_activity" as activity ' \
        '	LEFT JOIN "App_comment" as commentT ' \
        '	ON activity.id = commentT.activity_id ' \
        '   GROUP BY activity.id ' \
        ')' \
        ' as S3 ON S1.id = S3.id '

    @classmethod
    def get_query_activity_list_by_user_own(cls, user_id):
        user_id = int(user_id).__str__()
        return cls.QUERY_ACTIVITY_LIST_BY_USER_OWN_FIRST_PART.value + \
               user_id + \
               cls.QUERY_ACTIVITY_LIST_BY_USER_OWN_SECOND_PART.value
