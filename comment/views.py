from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from comment.models import Comment
from comment.seriallzers import CommentSerializer


# Create your views here.

# 조회, 작성
@api_view(['GET', 'POST'])
def review(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
         serializer.save()
         return Response(serializer.errors, status=status.HTTP_201_CREATED) #작성이 다 완료가 되면 
        else:
           print(serializer.errors) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 작성에 오류가 나면


#수정,삭제
@api_view(['GET', 'PUT', 'DELETE'])
def update(request, tweet_id):
    if request.method == 'GET':
      comment = get_object_or_404(Comment, id=tweet_id)
      serializer = CommentSerializer(comment)
      return Response(serializer.data)
    elif request.method == 'PUT':
        comment = get_object_or_404(Comment, id=tweet_id)
        serializer = CommentSerializer(comment, data= request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
    elif request.method == 'DELETE':
        comment = get_object_or_404(Comment, id=tweet_id)
        comment.delete()
        return Response(status=status.HTTP_200_OK)
           
           
            

