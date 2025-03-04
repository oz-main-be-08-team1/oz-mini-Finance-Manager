from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.accounts.models import Account

# Create your tests here.
User = get_user_model()


class Test_Account_Model(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="test")
        self.account = {
            "user": self.user,
            "account_number": "123456789",
            "bank_code": "001",
            "account_type": "LOAN",
            "balance": 100,
        }

    def test_account_create(self):
        account = Account.objects.create(**self.account)
        self.assertEqual(account.account_number, "123456789")
        self.assertEqual(Account.objects.count(), 1)
