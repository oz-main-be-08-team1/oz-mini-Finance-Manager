from rest_framework.authentication import BaseAuthentication
from rest_framework_simplejwt.tokens import AccessToken
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class CookieJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        access_token = request.COOKIES.get("access_token")
        if not access_token:
            return None

        try:
            token = AccessToken(access_token)
            user = User.objects.get(id=token["user_id"])
            return user, None
        except Exception:
            return None