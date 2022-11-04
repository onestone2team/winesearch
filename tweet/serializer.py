from rest_framework import serializers
from tweet.models import Tweet

class ViewSerializer(serializers.ModelSerializer):
    class Meta :
        model = Tweet
        fields = "__all__"