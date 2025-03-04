# Generated by Django 5.1.6 on 2025-03-04 08:41

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Analysis",
            fields=[
                ("analysis_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "analysis_target",
                    models.CharField(
                        choices=[("REVENUE", "Revenue"), ("EXPEND", "Expend")],
                        max_length=10,
                    ),
                ),
                (
                    "period_type",
                    models.CharField(
                        choices=[
                            ("DAILY", "Daily"),
                            ("WEEKLY", "Weekly"),
                            ("MONTHLY", "Monthly"),
                            ("YEARLY", "Yearly"),
                        ],
                        max_length=10,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "descriptions",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "result_image",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="analysis",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "분석",
                "verbose_name_plural": "분석 목록",
            },
        ),
    ]
