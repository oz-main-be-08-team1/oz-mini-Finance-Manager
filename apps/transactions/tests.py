from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.accounts.models import Account
from apps.transactions.models import Transaction_History

# Create your tests here.
User = get_user_model()


class Test_Transaction_Model(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="test")
        self.account = Account.objects.create(
            user=self.user,
            account_number="123456789",
            bank_code="001",
            account_type="LOAN",
            balance=100,
        )
        self.transaction = {
            "account": self.account,
            "transaction_amount": 10.0,
            "post_transaction_amount": 5.0,
            "transaction_detail": "Test",
            "transaction_type": "DEPOSIT",
            "transaction_method": "ATM",
        }

    def test_transaction_create(self):
        transaction = Transaction_History.objects.create(**self.transaction)
        self.assertEqual(transaction.transaction_type, "DEPOSIT")
        self.assertEqual(Transaction_History.objects.count(), 1)
