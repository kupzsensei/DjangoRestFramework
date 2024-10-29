from rest_framework import serializers
from .models import Post, PostComment
from core.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = Post
        fields = ['id','created_by' , 'description' , 'media_link' , 'post_comment']
        depth = 1

   

class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['created_by' , 'description' , 'media_link']

class AddCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ['comment' , 'post' , 'created_by']
        