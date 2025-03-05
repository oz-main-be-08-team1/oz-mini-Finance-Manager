from django.urls import path

from apps.accounts.views import AccountCreateView, AccountDeleteView, AccountDetailView

app_name = "accounts"


urlpatterns = [
    path("open/", AccountCreateView.as_view(), name="account-create"),
    path("<int:pk>/", AccountDetailView.as_view(), name="account-detail"),
    path("delete/<int:pk>", AccountDeleteView.as_view(), name="account-delete"),
]
