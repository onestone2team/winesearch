from tweet.models import Tweet
from user.models import User
from . import datasave



from tweet.serializer import ViewSerializer
from user.serializer import UserSerializer

from django.db.models import Q
from django.shortcuts import render,redirect
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import generics

from bs4 import BeautifulSoup as BS    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import time

# Create your views here.

class tweetAPI(APIView):
    def get(self, request,fromat=None):
        UserModels=User.objects.all()
        UserModels=UserSerializer(UserModels,many=True)
        return render(request,"search.html")
        # return Response(UserModels.data)
    def post(self,request,format=None):
        Serializers =UserSerializer(data=request.data)
        if Serializers.is_valid():
            Serializers.save()
            return Response(Serializers.data)
        else:
            print(Serializers.errors)
        return Response()


class tweetlist(APIView):
    def get(self,request,format=None):
        searchs=Tweet.objects.all()
        Serializers=ViewSerializer(searchs,many=True)
        return Response(Serializers.data)
    def post(self,request,format=None):
        Serializers =ViewSerializer(data=request.data)
        if Serializers.is_valid():
            Serializers.save()
            return Response(Serializers.data)
        else:
            print(Serializers.errors)
        return Response()
        
class search(APIView):
    def get(self,request):
        queryset = Tweet.objects.all()
        searchword = request.GET.get('search')
        print(searchword)
        if searchword:
            queryset=queryset.filter(Q(name__icontains=searchword)|Q(tag__icontains=searchword)|Q(content__icontains=searchword))
        serializers=ViewSerializer(queryset,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

class test():
    def get(request):
        return ('search.html')
        
        
# 추가 수정 내용
class PostViewSet(APIView):
    
    def get(self, request):
        pagination = PageNumberPagination()
        pagination.page_size = 20
        pagination.page_query_param = 'page'

        winedata = Tweet.objects.all()
        p = pagination.paginate_queryset(queryset=winedata, request=request)

        serializer = ViewSerializer(p, many=True)

        return Response(serializer.data)

class ViewWineType(APIView):
# 로제와인, 화이트와인, 레드와인, 스파클링와인 
    def get(self, request, wine_type):
        pagination = PageNumberPagination()
        pagination.page_size = 20
        pagination.page_query_param = 'page'

        winedata = Tweet.objects.filter(tag = wine_type)
        p = pagination.paginate_queryset(queryset=winedata, request=request)

        serializer = ViewSerializer(p, many=True)
        return Response(serializer.data)

class SaveList(APIView):
    def get(self, request):
        file_path = "tweet\sample.json"
        with open(file_path, "r") as json_file:
            json_data = json.load(json_file)
            url = "https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl"
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get(url)

            for i in range(len(json_data)):
                name = json_data[i]["title"]
                content = json_data[i]["description"]
                # 와인 구분 시스템
                tag = json_data[i]["variety"]
                data = tag.split(" ")
                result = data[0]
                winetag = datasave.searchwine(result)

                country = json_data[i]["country"]

                elem = driver.find_element(By.NAME, "q")
                elem.clear()
                elem.send_keys(name)
                elem.send_keys(Keys.RETURN)
                html = driver.page_source
                soup = BS(html,features="html.parser")

                div_img = soup.select_one('.bRMDJf')
                img = div_img.select_one('img')['src']
                
                tweet = Tweet.objects.create(name = name, content=content, tag=winetag, country=country, image=img)
                tweet.save()
                time.sleep(0.5)

        return Response("저장됨")

