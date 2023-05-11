from rest_framework import serializers
from post.models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts', 'comments']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='comment-detail')

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'short_description', 'text', 'is_draft', 'author', 'comments']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), source='post', required=False)

    class Meta:
        model = Comment
        fields = ['url', 'id', 'message', 'author', 'post_id']
