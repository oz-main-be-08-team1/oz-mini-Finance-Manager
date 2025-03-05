from gc import get_objects

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.transactions.models import Transaction_History
from apps.transactions.serializers import (
    Transaction_Create_Serializer,
    Transaction_Update_Serializer,
)

# Create your views here.


class TransactionListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transaction_list = Transaction_History.objects.filter(
            account__user=request.user
        ).select_related("account")
        serializer = Transaction_Update_Serializer(transaction_list, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = Transaction_Create_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetailDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        transaction_id = self.kwargs.get("pk")
        user_accounts = self.request.user.accounts.all()

        # 🔹 해당 계좌와 연결된 거래 기록 조회
        return get_object_or_404(
            Transaction_History, id=transaction_id, account__in=user_accounts
        )

    def get(self, request, *args, **kwargs):
        transaction = self.get_object()
        serializer = Transaction_Create_Serializer(transaction)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        transaction = self.get_object()
        serializer = Transaction_Update_Serializer(
            transaction, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        transaction = self.get_object()
        transaction.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_200_OK)
