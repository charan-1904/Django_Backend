from rest_framework import serializers
from . models import Blog,Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    # tags = TagSerializer(many=True)


    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['uid', 'title', 'blog_text', 'main_image', 'user', 'user_username']
        # exclude = ['created_at','updated_at']
