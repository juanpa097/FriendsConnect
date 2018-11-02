import os
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from pytz import utc
from random import randint
from .model import CodeValidate


class IsExpiredMixin:
    DURATION = 0

    def _is_expired(self, obj):
        now = datetime.utcnow().replace(tzinfo=utc)
        if obj.created < now - timedelta(seconds=self.DURATION):
            return True
        return False


# TODO - verify when use
class CodeIsExpiredMixin(IsExpiredMixin):
    DURATION = int(os.environ.get('CODE_DURATION', 300))


class CodeGenMixin:

    def _create_random_code(self):

        code = str(
            randint(
                100000,
                999999
            )
        )
        return code

    def _generate_code(self, user):
        code = self._create_random_code()
        try:
            old_reset = CodeValidate.objects.get(
                user_id=user.id
            )
            old_reset.delete()
        except CodeValidate.DoesNotExist:
            pass
        CodeValidate.objects.create(
            user=user,
            code=code
        )
        return code

    def generate_password_reset_code(self, user):
        return self._generate_code(user)

    def generate_user_validate_code(self, user):
        return self._generate_code(user)


class ValidationCode:

    def validate_code(self, username, code):
        user = get_object_or_404(User, username=username)
        code = get_object_or_404(CodeValidate, code=code, user=user)
        user.validate = True
        user.save()
        code.delete()
