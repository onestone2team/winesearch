from rest_framework import serializers
from user.models import User
from rest_framework.validators import UniqueValidator
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= "__all__"

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
    class Meta:
        model= User
        fields= ('username', 'email', 'profile', 'profilename', 'password')

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.profile = validated_data.get('profile', instance.profile)
        instance.profilename = validated_data.get('profilename', instance.profilename)
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
