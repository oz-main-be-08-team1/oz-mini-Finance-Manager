from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    account_number = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = [
            "id",
            "account_number",
            "bank_code",
            "account_type",
            "balance",
            "user",
        ]
        read_only_fields = ["balance", "user"]

    """계좌번호 뒷4자리 마스킹"""

    def get_account_number(self, instance):
        account_number = instance.account_number
        if len(account_number) >= 4:
            return account_number[:-4] + "****"
        return account_number

    def create(self, validated_data):
        validated_data["balance"] = 0.00
        return super().create(validated_data)
