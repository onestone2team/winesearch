from rest_framework import serializers
from user.models import User
import re
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
def emailvaildator(email):
    is_email = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if not is_email.fullmatch(email):
        return False
    return True

def passwordVaildator(password, password2):
    password = password.replace(' ','')
    if password != '':
        if password != password2:
            return False
        else:
            return True
    else:
        return False

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=50)
    class Meta:
        model= User
        fields= "__all__"

    def validate(self, attrs):
        password_valid= passwordVaildator(attrs['password'], attrs["password2"])
        email_valid= emailvaildator(attrs['email'])
        if email_valid == False:
            raise serializers.ValidationError("이메일을 확인해 주세요!")
        if password_valid == False:
            raise serializers.ValidationError("비밀번호를 확인해 주세요!")
        attrs.pop('password2', None)
        # del attrs['password2']
        return super().validate(attrs)

    def create(self, validated_data):
        user= super().create(validated_data)
        user.set_password(user.password)
        user.is_active= True
        user.save()
        return user

    def update(self, validated_data):
        user=  super().update(validated_data)
        user.set_password(user.password)
        user.is_active= True
        user.save()
        return user

class UserProfileInfoSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=50)
    class Meta:
        model= User
        fields= ('username', 'email', 'profile', 'profilename', 'password')

    def validate(self, attrs):
        password_valid= passwordVaildator(attrs['password'], attrs["password2"])
        email_valid= emailvaildator(attrs['email'])
        if email_valid == False:
            raise serializers.ValidationError("이메일을 확인해 주세요!")
        if password_valid == False:
            raise serializers.ValidationError("비밀번호를 확인해 주세요!")
        return super().validate(attrs)

    def update(self, instance, validated_data):
        instance.username= validated_data.get('username', instance.username)
        instance.profile= validated_data.get('profile', instance.profile)
        instance.profilename= validated_data.get('profilename', instance.profilename)
        instance.email= validated_data.get('email', instance.email)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance
