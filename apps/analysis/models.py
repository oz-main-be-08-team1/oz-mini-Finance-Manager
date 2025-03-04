from django.db import models
from django.utils.timezone import now

from apps.user.models import User  # User 모델을 import

# Create your models here.


class Analysis(models.Model):
    class AnalysisTarget(models.TextChoices):
        REVENUE = "REVENUE", "Revenue"
        EXPEND = "EXPEND", "Expend"

    class PeriodType(models.TextChoices):
        DAILY = "DAILY", "Daily"
        WEEKLY = "WEEKLY", "Weekly"
        MONTHLY = "MONTHLY", "Monthly"
        YEARLY = "YEARLY", "Yearly"

    analysis_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="analysis")
    analysis_target = models.CharField(max_length=10, choices=AnalysisTarget.choices)
    period_type = models.CharField(max_length=10, choices=PeriodType.choices)
    start_date = models.DateField()
    end_date = models.DateField()
    descriptions = models.CharField(max_length=255, blank=True, null=True)
    result_image = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "분석"
        verbose_name_plural = f"{verbose_name} 목록"

    def __str__(self):
        return f"{self.analysis_id}"
