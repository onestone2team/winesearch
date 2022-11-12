from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from Review.models import Review
from Review.seriallzers import ReviewSerializer


# Create your views here.
class ReviewList(APIView):
    def get(self, request, format=None):
         Reviews = Review.objects.all()
         serializer = ReviewSerializer(Reviews, many=True)
         return Response(serializer.data)
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED) #작성이 다 완료가 되면
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 작성에 오류가 나면




class Update(APIView):
    
    def get(self, request, Winedata_id,Review_id, format=None):
        Review = get_object_or_404(Review, id=Review_id)
        serializer = ReviewSerializer(Review)
        return Response(serializer.data)
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request, Winedata_id,Review_id, fomat=None):
        Review = get_object_or_404(Review, id=Review_id)
        serializer = ReviewSerializer(Review, data= request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, Winedata_id, Review_id, format=None):
         print(Review_id)
         review = get_object_or_404(Review, id=Review_id)
         review.delete()
         return Response({"message": "댓글이 삭제 되었습니다."},status=status.HTTP_200_OK) 


