from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('email', 'id', 'first_name', 'last_name', 'phone')


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    pass


class CurrentUserSerializer(serializers.ModelSerializer):
    pass