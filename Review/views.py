from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from Review.models import Review
from Review.seriallzers import ReviewSerializer


# Create your views here.
class Update(APIView):
    
    def get(self, request, Winedata_id,Review_id, format=None):
        Review = get_object_or_404(Review, id=Review_id)
        serializer = ReviewSerializer(Review)
        return Response(serializer.data)
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request, Winedata_id,Review_id, fomat=None):
        Review = get_object_or_404(Review, id=Review_id)
        serializer = ReviewSerializer(Review, data= request.data)   
    def delete(self, request, Winedata_id, Review_id, format=None):
         print(Review_id)
         review = get_object_or_404(Review, id=Review_id)
         review.delete()
         return Response({"message": "댓글이 삭제 되었습니다."},status=status.HTTP_200_OK) 
    def post(self, request, Winedata_id, Review_id, format=None):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 작성이 다 완료가 되면
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
        # 작성에 오류가 나면
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




