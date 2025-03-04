from django.test import TestCase

from apps.notifications.models import Notification
from apps.user.models import User

# Create your tests here.


class NotificationModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="test", password="password")
        self.notification_data = {
            "user": self.user,
            "message": "test massage",
            "is_read": False,
        }

    def test_notification_creation(self):
        # 객체 생성
        notification = Notification.objects.create(**self.notification_data)

        # 객체가 생성 확인
        self.assertEqual(notification.user, self.user)
        self.assertEqual(
            notification.message, "test massage"
        )  # message가 올바른지 확인
        self.assertFalse(
            notification.is_read
        )  # is_read가 기본값 False로 설정되었는지 확인
        self.assertIsNotNone(notification.created_at)  # 자동 설정
        self.assertEqual(
            str(notification), str(notification.notification_id)
        )  # notification_id 반환해야 함

    def test_notification_is_read_default(self):
        # 'is_read` default 확인
        notification = Notification.objects.create(
            user=self.user, message="Test default is_read"
        )

        # `is_read`가 False로 설정되었는지 확인
        self.assertFalse(notification.is_read)

    def test_notification_str(self):
        # When: 알림 객체를 생성
        notification = Notification.objects.create(
            user=self.user, message="Test message2"
        )

        # notification_id를 반환하는지 확인
        self.assertEqual(str(notification), str(notification.notification_id))
