from rest_framework import serializers
from post.models import Post, Like
from user.serializers import UserSerializer


class LikeSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'user', 'post', 'created_at')


class PostSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    # likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'created_at', 'updated_at', 'user')
