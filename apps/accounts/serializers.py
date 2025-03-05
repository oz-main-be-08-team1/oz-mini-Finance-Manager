from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
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

    def create(self, validated_data):
        validated_data["balance"] = 0.00
        return super().create(validated_data)
