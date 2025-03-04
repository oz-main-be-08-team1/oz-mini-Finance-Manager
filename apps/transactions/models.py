from datetime import datetime, timezone

from django.db import models

from apps.accounts.models import Account

# Create your models here.

# 거래 타입
TRANSACTION_TYPE = [
    ("DEPOSIT", "입금"),
    ("WITHDRAW", "출금"),
]

# 거래 종류
TRANSACTION_METHOD = [
    ("ATM", "ATM 거래"),
    ("TRANSFER", "계좌이체"),
    ("AUTOMATIC_TRANSFER", "자동이체"),
    ("CARD", "카드결제"),
    ("INTEREST", "이자"),
]


class Transaction_History(models.Model):
    transaction_amount = models.DecimalField(max_digits=18, decimal_places=2)
    post_transaction_amount = models.DecimalField(max_digits=18, decimal_places=2)
    transaction_detail = models.TextField(max_length=255)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE)
    transaction_method = models.CharField(max_length=20, choices=TRANSACTION_METHOD)
    transaction_timestamp = models.DateTimeField(default=datetime.now)

    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="accounts"
    )
