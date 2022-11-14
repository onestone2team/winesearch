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
        fields = ("review","grade")

class UserReviewSerializer(serializers.ModelSerializer):

    winedata = serializers.SerializerMethodField()

    def get_winedata(self, obj):
        return obj.winedata.id

    class Meta :
        model = Review
        fields = ("id", "winedata","review","grade")

class RecommandReviewSerializer(serializers.ModelSerializer):

    winedata = ViewSearchSerializer(read_only=True)

    class Meta :
        model = Review
        fields = ("winedata","review")

    
    
