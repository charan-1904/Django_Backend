from rest_framework import serializers
from . models import Blog, Comment,Tag,Reply


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    # parent_comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False)
    replies = ReplySerializer(many=True, read_only=True)


    class Meta:
        model = Comment
        fields = '__all__'



class BlogSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    # tags = TagSerializer(many=True)


    class Meta:
        model = Blog
        # fields = '__all__'
        # fields = ['uid', 'title', 'blog_text', 'main_image', 'user', 'user_username']
        exclude = ['comments']

class BlogDSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    comments = CommentSerializer(many=True, read_only=True)



    class Meta:
        model = Blog
        fields = '__all__'



class ContactFormSerializer(serializers.Serializer):
    user_username = serializers.ReadOnlyField(source='user.username')

    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=500)