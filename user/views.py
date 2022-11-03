from rest_framework.views import APIView
from user.models import User
from rest_framework import status
from rest_framework.response import Response
from user.serializer import UserSerializer, UserProfileInfoSerializer
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
        # print(request.password)
        # password = request.password
        # password2 = request.password2
        # if password != password2:
        #     return Response({"message": "비밀번호가 다릅니다!"}, status=status.HTTP_400_BAD_REQUEST)
        # else:


class UserProfileInfoView(APIView):
    def put(self, request):
        user = User.objects.get(id=request.user.id)
        user_info = request.data
        for key, value in user_info.items():
            if not value:
                user_info.pop(key)
        serializer = UserProfileInfoSerializer(user, data=user_info, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "변경 완료!"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

