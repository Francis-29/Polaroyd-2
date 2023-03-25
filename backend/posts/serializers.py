from rest_framework import serializers
from .models import Post, Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'id',
            'user',
            'post',
            'date_added'
        )
        depth = 1


class PostSerializer(serializers.ModelSerializer):
    like_set = LikeSerializer(many=True, required=False)
    class Meta:
        model = Post
        fields = (
            'user',
            'id',
            'caption',
            'date_added',
            'image',
            'like_set'
        )