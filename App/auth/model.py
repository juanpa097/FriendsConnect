from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import exceptions
from datetime import datetime, timedelta


class ExpiringTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid Token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or delete')

        utc_now = datetime.utcnow()
        utc_now = utc_now.replace(tzinfo=pytz.utc)

        if token.created < utc_now - timedelta(hours=24):
            raise  exceptions.AuthenticationFailed('Token has expired')

        return token.user, token