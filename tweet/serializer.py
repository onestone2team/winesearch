from rest_framework import serializers
from tweet.models import Tweet
from comment.models import Comment
from comment.seriallzers import TweetCommentSerializer

class ViewSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Tweet
        fields = ("id","name", "image")

class ViewSearchSerializer(serializers.ModelSerializer):

    class Meta :
        model = Tweet
        fields = ("id","name","image")

class ViewTweetDetail(serializers.ModelSerializer):
    comment_set = TweetCommentSerializer(many=True, read_only=True)

    class Meta :
        model = Tweet
        fields = ("id","name","tag","image","content", "country", "comment_set","bookmark")

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta :
        model = Comment
        fields = ("content","grade")

class UserCommentSerializer(serializers.ModelSerializer):

    tweet = serializers.SerializerMethodField()

    def get_tweet(self, obj):
        return obj.tweet.id

    class Meta :
        model = Comment
        fields = ("id", "tweet","comment","grade")

class RecommandCommentSerializer(serializers.ModelSerializer):

    tweet = ViewSearchSerializer(read_only=True)

    class Meta :
        model = Comment
        fields = ("tweet","comment")

