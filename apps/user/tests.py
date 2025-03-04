from django.contrib.auth import get_user_model
from django.test import TestCase

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
