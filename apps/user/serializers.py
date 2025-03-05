from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response

User=get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user  # self.context.get("request").user를 사용하는 것도 고려 가능
        data["user"] = {
            "email": user.email,
            "nickname": user.nickname,
            "name": user.name,
            "phone_number": user.phone_number,
        }
        return data

class SignupSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "nickname", "name", "phone_number","is_active")

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError({"password": "비밀번호가 일치하지 않습니다."})
        return data

    def create(self, validated_data):

        validated_data.pop("password2")
        user = User.objects.create_user(email=validated_data["email"], password=validated_data["password1"])
        user.nickname = validated_data.get("nickname", "")
        user.name = validated_data.get("name", "")
        user.phone_number = validated_data.get("phone_number", "")
        user.save()

        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "nickname", "name", "phone_number"]