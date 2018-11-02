from enum import Enum


class EmailTemplates(Enum):
    RESET_PASSWORD = dict(
        template='reset_password.html',
        subject='Reset Password'
    )

    @classmethod
    def get_reset_password(cls):
        return cls.RESET_PASSWORD.value
