from tweet.models import Tweet
from user.models import User
from comment.seriallzers import CommentSerializer, TweetCommentSerializer
from comment.models import Comment
from . import datasave
from django.shortcuts import render,redirect
from django.http import HttpResponse
from tweet.serializer import ViewSerializer, ViewSearchSerializer, ViewTweetDetail, UserCommentSerializer, RecommandCommentSerializer
from user.serializer import UserSerializer
from tweet.running import savecosines, Editexcel
from django.db.models import Q
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
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
        
class ViewSearch(APIView):
    def get(self,request):
        pagination = PageNumberPagination()
        pagination.page_size = 20
        pagination.page_query_param = 'page'

        searchword = request.GET.get('search')
        winedata = Tweet.objects.filter(Q(name__icontains=searchword)|Q(tag__icontains=searchword)|Q(content__icontains=searchword))
        p = pagination.paginate_queryset(queryset=winedata, request=request)

        serializer = ViewSearchSerializer(p, many=True)
        return Response(serializer.data)
        
# 추가 수정 내용
class PostViewSet(APIView):
    
    def get(self, request):
        pagination = PageNumberPagination()
        pagination.page_size = 20
        pagination.page_query_param = 'page'

        winedata = Tweet.objects.all()
        p = pagination.paginate_queryset(queryset=winedata, request=request)

        serializer = ViewSerializer(p, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class ViewWineType(APIView):
# 로제와인, 화이트와인, 레드와인, 스파클링와인 
    def get(self, request, wine_type):
        pagination = PageNumberPagination()
        pagination.page_size = 20
        pagination.page_query_param = 'page'

        winedata = Tweet.objects.filter(tag = wine_type)
        p = pagination.paginate_queryset(queryset=winedata, request=request)

        serializer = ViewSerializer(p, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ViewRecommendWine(APIView):
    def get(self, request):
        username = request.user.username
        comment_data = Comment.objects.filter(id = request.user.id)
        if comment_data:
            taster_name = savecosines(username)
            print(taster_name)
            wine_recommand = Tweet.objects.filter(taster_name = taster_name).order_by('-grade')

            if not wine_recommand :
                userdata = User.objects.get(username = taster_name)
                wine_recommand = Comment.objects.filter(id = userdata.id).order_by('-grade')
                wine_recommand = wine_recommand[:10]
                serializer = RecommandCommentSerializer(wine_recommand, many=True)
            
            else :
                wine_recommand = wine_recommand[:10]
                serializer = ViewSerializer(wine_recommand, many=True)
                
            return Response(serializer.data, status=status.HTTP_200_OK)
        else :
            return Response({"message": "평가한 와인 정보가 없습니다."}, status=status.HTTP_200_OK)

class ViewWineDetail(APIView):
    def get(self, request, wine_id):
        wine = Tweet.objects.get(id = wine_id)
        serializer = ViewTweetDetail(wine)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, wine_id):
        serializer = CommentSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save(username = request.user, tweet_id = wine_id)
            wine = Tweet.objects.get(id = wine_id)
            point = serializer.data['grade']
            title = wine.name
            country = wine.country
            taster_name = request.user.username
            
            new_data = {
                "title":title,
                "points":point,
                "country":country,
                "taster_name":taster_name
            }
            Editexcel(new_data)
            return Response({"message": "댓글 등록 완료!"}, status=status.HTTP_201_CREATED) #작성이 다 완료가 되면
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 작성에 오류가 나면
            

class ViewComment(APIView):
    def get(self, request, comment_id):
        wine = Comment.objects.get(id = comment_id)
        serializer = TweetCommentSerializer(wine)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class UserCommentView(APIView):
    def get(self, request):
        pagination = PageNumberPagination()
        pagination.page_size = 10
        pagination.page_query_param = 'page'
        comment = Comment.objects.filter(id = request.user.id)
        if comment:
            p = pagination.paginate_queryset(queryset=comment, request=request)

            serializer = UserCommentSerializer(p, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "작성한 글이 없습니다"}, status=status.HTTP_200_OK)
        

class BookmarkListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        bookmarklist = Tweet.objects.filter(bookmark=request.user.id)
        if bookmarklist:
            serializer = ViewSerializer(bookmarklist, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "저장된 와인 정보가 없습니다"}, status=status.HTTP_200_OK)


class BookmarkView(APIView):
    def post(self,request,wine_id):
        tweet = get_object_or_404(Tweet, id= wine_id)
        if request.user in tweet.bookmark.all():
            tweet.bookmark.remove(request.user)
            return Response("북마크에 삭제되었습니다", status = status.HTTP_200_OK)
        else:
            tweet.bookmark.add(request.user)
            return Response("북마크가 저장되었습니다", status = status.HTTP_200_OK)


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
                username = json_data[i]["taster_name"]
                grade = json_data[i]["points"]
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
                
                tweet = Tweet.objects.create(name = name, content=content, tag=winetag, country=country, image=img, taster_name = username, grade = grade)
                tweet.save()

                time.sleep(0.5)

        return Response("저장됨")


