from django.urls.conf import path

from apps.transactions.views import (
    TransactionDetailDeleteAPIView,
    TransactionListCreateView,
)

app_name = "transaction"

urlpatterns = [
    path("/", TransactionListCreateView.as_view(), name="transaction_list_create"),
    path(
        "<int:pk>/",
        TransactionDetailDeleteAPIView.as_view(),
        name="transaction_detail_delete",
    ),
]
