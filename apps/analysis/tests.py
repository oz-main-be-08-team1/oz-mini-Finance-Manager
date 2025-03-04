from django.test import TestCase
from django.utils import timezone

from apps.analysis.models import Analysis
from apps.user.models import User

# Create your tests here.


class AnalysisModelTest(TestCase):

    def setUp(self):
        # Given
        self.user = User.objects.create_user(email="test", password="password")
        self.analysis_data = {
            "user": self.user,
            "analysis_target": "REVENUE",
            "period_type": "MONTHLY",
            "start_date": timezone.now().date(),
            "end_date": timezone.now().date(),
            "descriptions": "alysis test",
            "result_image": "test_image.png",
        }

    def test_analysis_creation(self):
        analysis = Analysis.objects.create(**self.analysis_data)

        self.assertEqual(analysis.user, self.user)
        self.assertEqual(analysis.analysis_target, "REVENUE")
        self.assertEqual(analysis.period_type, "MONTHLY")
        self.assertEqual(analysis.descriptions, "alysis test")
        self.assertEqual(analysis.result_image, "test_image.png")
        self.assertIsNotNone(analysis.created_at)  # 자동으로 생성
        self.assertIsNotNone(analysis.updated_at)  # 자동으로 생성
        self.assertEqual(str(analysis), str(analysis.analysis_id))

    def test_analysis_period_type_choices(self):
        #  PERIOD_TYPE 'DAILY'로 객체 생성
        analysis = Analysis.objects.create(
            user=self.user,
            analysis_target="EXPEND",
            period_type="DAILY",
            start_date=timezone.now().date(),
            end_date=timezone.now().date(),
        )

        # period_type 'DAILY'로 설정 확인
        self.assertEqual(analysis.period_type, "DAILY")

    def test_analysis_target_choices(self):
        # ANALYSIS_TARGET 'EXPEND'로 객체 생성
        analysis = Analysis.objects.create(
            user=self.user,
            analysis_target="EXPEND",
            period_type="YEARLY",
            start_date=timezone.now().date(),
            end_date=timezone.now().date(),
        )

        # analysis_target 'EXPEND'로 설정 확인
        self.assertEqual(analysis.analysis_target, "EXPEND")
