from enum import Enum


class EmailTemplates(Enum):
    RESET_PASSWORD = dict(
        path='reset_password.html',
        subject='Reset Password'
    )
    CREATE_USER = dict(
        path='create_user.html',
        subject='You are welcome'
    )

    @classmethod
    def get_reset_password(cls):
        return cls.RESET_PASSWORD.value

    @classmethod
    def get_create_user(cls):
        return cls.CREATE_USER.value
