from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from comment.models import Comment
from comment.seriallzers import CommentSerializer


# Create your views here.
class ReviewList(APIView):
    def get(self, request, format=None):
         comments = Comment.objects.all()
         serializer = CommentSerializer(comments, many=True)
         return Response(serializer.data)
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED) #작성이 다 완료가 되면
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 작성에 오류가 나면




class Update(APIView):
    
    def get(self, request, tweet_id,comment_id, format=None):
        comment = get_object_or_404(Comment, id=comment_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request, tweet_id,comment_id, fomat=None):
        comment = get_object_or_404(Comment, id=comment_id)
        serializer = CommentSerializer(comment, data= request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, tweet_id, comment_id, format=None):
         comment = get_object_or_404(Comment, id=comment_id)
         comment.delete()
         return Response({"message": "댓글이 삭제 되었습니다."},status=status.HTTP_200_OK) 


