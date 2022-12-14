from rest_framework.views import APIView
from user.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from user.serializer import UserSerializer, UserProfileInfoSerializer, UserProfileView


# from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
class UserView(APIView):
    def post(self, request):
        serializer= UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "가입 완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileInfoView(APIView):
    def get(self, request):
        user = get_object_or_404(User, id=request.user.id)
        serializer = UserProfileView(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request):
        user = User.objects.get(id=request.user.id)
        user_info = dict()
        for key, value in request.data.items():
            if value:
                user_info.update({key:value})
        serializer = UserProfileInfoSerializer(user, data=user_info, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "변경 완료!"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = get_object_or_404(User, id=request.user.id)
        user.delete()
        return Response("삭제되었습니다!", status=status.HTTP_204_NO_CONTENT)


class UserLogout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "로그아웃"}, status=status.HTTP_200_OK)


    





