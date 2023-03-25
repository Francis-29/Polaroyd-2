from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('user_id', 'name', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'user_id',
            'name',
            'bio',
            'profile_pic',
            'profile_banner',
            'followers_count',
            'following_count',
        )