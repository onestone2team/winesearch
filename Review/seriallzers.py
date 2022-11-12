from rest_framework import serializers
from Review.models import Review
from user.models import User
from user.serializer import ReviewProfileView


class ReviewSerializer(serializers.ModelSerializer):
    class Meta :
        model = Review
        fields = ("id","Review","grade")



class WinedataReviewSerializer(serializers.ModelSerializer):
    username = ReviewProfileView(read_only=True)

    class Meta :
        model = Review
        fields = ("id","username","Review","grade","created_time")

