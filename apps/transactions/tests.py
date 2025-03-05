from http.client import responses

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls.base import reverse
from rest_framework import status
from rest_framework.test import APITestCase

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


class Test_Transaction_APIView(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test5@test.com", password="1234")
        login_data = {"email": "test5@test.com", "password": "1234"}
        login_response = self.client.post(reverse("user:login"), login_data)
        access_token = login_response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        self.account = Account.objects.create(
            user=self.user,
            account_number="123456789",
            bank_code="001",
            account_type="LOAN",
            balance=100,
        )

        self.transaction = {
            "account": self.account.id,
            "transaction_amount": 10.0,
            "post_transaction_amount": 5.0,
            "transaction_detail": "Test",
            "transaction_type": "DEPOSIT",
            "transaction_method": "ATM",
        }

    def test_create_view(self):
        url = reverse("transaction:transaction_list_create")
        response = self.client.post(url, self.transaction)

        self.assertTrue(
            Transaction_History.objects.filter(transaction_detail="Test").exists()
        )
        self.assertEqual(response.data["transaction_detail"], "Test")

    def test_list_view(self):
        url = reverse("transaction:transaction_list_create")
        response = self.client.post(url, self.transaction)

        url = reverse("transaction:transaction_list_create")
        responses = self.client.get(url)

        self.assertEqual(responses.status_code, status.HTTP_200_OK)
        self.assertEqual(len(responses.data), 1)
        self.assertIn("transaction_detail", responses.data[0])
        self.assertIn("transaction_amount", responses.data[0])

    def test_patch_view(self):
        url = reverse("transaction:transaction_list_create")
        response = self.client.post(url, self.transaction)

        print(response.data)
        transaction_id = response.data.get("id")

        url = reverse(
            "transaction:transaction_detail_delete", kwargs={"pk": transaction_id}
        )

        patch_response = self.client.patch(url, {"transaction_detail": "수정됨"})

        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_response.data["transaction_detail"], "수정됨")

    def test_delete_view(self):
        url = reverse("transaction:transaction_list_create")
        response = self.client.post(url, self.transaction)

        print(response.data)
        transaction_id = response.data.get("id")

        url = reverse(
            "transaction:transaction_detail_delete", kwargs={"pk": transaction_id}
        )
        delete_response = self.client.delete(url)

        self.assertEqual(delete_response.status_code, status.HTTP_200_OK)
        self.assertEqual(delete_response.data["msg"], "deleted")
