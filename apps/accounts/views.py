from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import Account
from apps.accounts.serializers import AccountSerializer

# Create your views here.


class AccountCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"msg": "신규 계좌 생성"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        account = get_object_or_404(Account, pk=pk, user=request.user)
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        account = get_object_or_404(Account, pk=pk, user=request.user)
        account.delete()
        return Response({"message": "Deleted successfully."}, status=status.HTTP_200_OK)
