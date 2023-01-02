from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = ('email', 'id', 'first_name', 'last_name', 'phone', 'image')


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    image = serializers.ImageField(required=False)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'id', 'email', 'image', 'password')
