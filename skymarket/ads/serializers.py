from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from ads.models import Ad, Comment
from users.serializers import CustomUserSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('pk', 'image', 'title', 'price', 'description')


class AdSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(source='author.phone')
    author_first_name = serializers.CharField(source='author.first_name')
    author_last_name = serializers.CharField(source='author.last_name')
    author_id = serializers.IntegerField(source='author.id')

    class Meta:
        model = Ad
        fields = ('pk', 'image', 'title', 'price', 'description', 'phone',
                  'author_first_name', 'author_last_name', 'author_id')


class AdDetailSerializer(serializers.ModelSerializer):
    pass
