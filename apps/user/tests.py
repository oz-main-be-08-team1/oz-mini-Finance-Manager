from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

# Create your tests here.
User = get_user_model()


class Test_User_Model(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="test1234")
        self.admin_user = User.objects.create_superuser(
            email="super@super.com", password="test1234"
        )

    def test_create_user(self):
        self.assertEqual(self.admin_user.is_admin, True)
        self.assertEqual(self.user.is_admin, False)
        self.assertEqual(User.objects.count(), 2)


class TokenObtainTest(APITestCase):
    def setUp(self):
        """테스트용 사용자 생성"""
        self.user = User.objects.create_user(
            email="test@example.com",
            password="testpassword",
        )
        self.user_data = {
            "email": "test2@email.com",
            "password1": "1234",
            "password2": "1234",
            "nickname": "nickname_tset",
            "name": "name_tset",
            "phone_number": "1234",
        }
        self.token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token.access_token}")

    def test_login(self):
        """JWT 토큰이 정상적으로 발급되는지 확인"""
        url = reverse("user:login")
        response = self.client.post(
            url, {"email": "test@example.com", "password": "testpassword"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("user", response.data)

    def test_signup(self):
        # Given
        url = reverse("user:signup")
        # When
        response = self.client.post(
            url,
            {
                "email": "test2@email.com",
                "password1": "1234",
                "password2": "1234",
                "nickname": "nickname_tset",
                "name": "name_tset",
                "phone_number": "1234",
            },
        )

        # Then
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(User.objects.filter(email="test2@email.com").exists())

    def test_logout(self):
        user = User.objects.create_user(email="test5@test.com", password="1234")

        self.assertTrue(User.objects.filter(email=self.user.email).exists())

        login_data = {"email": "test5@test.com", "password": "1234"}
        login_response = self.client.post(reverse("user:login"), login_data)
        access_token = login_response.data["access"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        response = self.client.post(
            reverse("user:logout"), {"refresh": login_response.data["refresh"]}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete(self):
        url = reverse("user:get_patch_delete")
        user = User.objects.create_user(email="test5@test.com", password="1234")

        login_data = {"email": "test5@test.com", "password": "1234"}
        login_response = self.client.post(reverse("user:login"), login_data)
        access_token = login_response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
