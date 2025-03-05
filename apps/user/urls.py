from django.urls.conf import path

from apps.user.views import (CustomTokenObtainView, LogoutView, ProfileView,
                             SignupView)

app_name = "user"

urlpatterns = [
    path("login/", CustomTokenObtainView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="get_patch_delete"),
    # path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh")
]
