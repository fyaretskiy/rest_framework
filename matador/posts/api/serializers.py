from rest_framework import serializers

from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_id', 'user_id', 'title', 'body')
