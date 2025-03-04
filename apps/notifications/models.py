from django.db import models
from django.utils.timezone import now

from apps.user.models import User  # User 모델 import

# Create your models here.


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)

    class Meta:
        verbose_name = "알림"
        verbose_name_plural = f"{verbose_name} 목록"

    def __str__(self):
        return self.notification_id
