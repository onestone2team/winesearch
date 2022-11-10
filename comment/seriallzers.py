from rest_framework import serializers
from comment.models import Comment
from user.models import User
from user.serializer import CommentProfileView


class CommentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Comment
        fields = ("id","comment","grade")



class TweetCommentSerializer(serializers.ModelSerializer):
    username = CommentProfileView(read_only=True)

    class Meta :
        model = Comment
        fields = ("id","username","comment","grade","created_time")

