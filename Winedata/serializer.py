from rest_framework import serializers
from Winedata.models import Winedata
from Review.models import Review
from Review.seriallzers import WinedataReviewSerializer

class ViewSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Winedata
        fields = ("id","name", "image")

class ViewSearchSerializer(serializers.ModelSerializer):

    class Meta : 
        model = Winedata
        fields = ("id","name","image")

class ViewWinedataDetail(serializers.ModelSerializer):
    review_set = WinedataReviewSerializer(many=True, read_only=True)

    class Meta :
        model = Winedata
        fields = ("id","name","tag","image","content", "country", "review_set","bookmark")

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta :
        model = Review
        fields = ("Review","grade")

class UserReviewSerializer(serializers.ModelSerializer):

    Winedata = serializers.SerializerMethodField()

    def get_Winedata(self, obj):
        return obj.Winedata.id

    class Meta :
        model = Review
        fields = ("id", "Winedata","Review","grade")

class RecommandReviewSerializer(serializers.ModelSerializer):

    winedata = ViewSearchSerializer(read_only=True)

    class Meta :
        model = Review
        fields = ("Winedata","Review")

    
    
