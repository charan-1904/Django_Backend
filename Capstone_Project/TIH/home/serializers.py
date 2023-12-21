from rest_framework import serializers
from . models import Blog


class BlogSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Blog
        # fields = ['uid', 'title', 'blog_text', 'main_image', 'user', 'user_username']
        exclude = ['created_at','updated_at']
