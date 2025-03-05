from rest_framework import serializers

from apps.transactions.models import Transaction_History


class Transaction_Create_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction_History
        fields = "__all__"


class Transaction_Update_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction_History
        fields = [
            "transaction_amount",
            "post_transaction_amount",
            "transaction_detail",
            "transaction_type",
            "transaction_method",
        ]
