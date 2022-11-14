from Winedata.models import Winedata
from user.models import User
from Review.seriallzers import ReviewSerializer, WinedataReviewSerializer
from Review.models import Review
from . import datasave
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Winedata.serializer import ViewSerializer, ViewSearchSerializer, ViewWinedataDetail, UserReviewSerializer, RecommandReviewSerializer
from user.serializer import UserSerializer
from Winedata.running import savecosines, Editexcel
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
import webbrowser
import json
import time

# Create your views here.

class ViewSearch(APIView):
    def get(self,request):
        pagination = PageNumberPagination()
        pagination.page_size = 20
        pagination.page_query_param = 'page'

        searchword = request.GET.get('search')
        winedata = Winedata.objects.filter(Q(name__icontains=searchword)|Q(tag__icontains=searchword)|Q(content__icontains=searchword))
        p = pagination.paginate_queryset(queryset=winedata, request=request)

        serializer = ViewSearchSerializer(p, many=True)
        return Response(serializer.data)

# 추가 수정 내용
class PostViewSet(APIView):

    def get(self, request):
        pagination = PageNumberPagination()
        pagination.page_size = 20
        pagination.page_query_param = 'page'

        winedata = Winedata.objects.all()
        p = pagination.paginate_queryset(queryset=winedata, request=request)

        serializer = ViewSerializer(p, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class ViewWineType(APIView):
# 로제와인, 화이트와인, 레드와인, 스파클링와인
    def get(self, request, wine_type):
        pagination = PageNumberPagination()
        pagination.page_size = 20
        pagination.page_query_param = 'page'

        winedata = Winedata.objects.filter(tag = wine_type)
        p = pagination.paginate_queryset(queryset=winedata, request=request)

        serializer = ViewSerializer(p, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ViewRecommendWine(APIView):
    def get(self, request):
        username = request.user.username
        Review_data = Review.objects.filter(username_id = request.user.id)
        if Review_data:
            taster_name = savecosines(username)
            print(taster_name)
            wine_recommand = Winedata.objects.filter(taster_name = taster_name).order_by('-grade')
            if not wine_recommand :
                userdata = User.objects.get(username = taster_name)
<<<<<<< HEAD:tweet/views.py
                wine_recommand = Comment.objects.filter(username_id = userdata.id).order_by('-grade')

                wine_recommand = wine_recommand[:10]
                serializer = RecommandCommentSerializer(wine_recommand, many=True)

=======
                wine_recommand = Review.objects.filter(username_id = userdata.id).order_by('-grade')
                
                wine_recommand = wine_recommand[:10]
                serializer = RecommandReviewSerializer(wine_recommand, many=True)
            
>>>>>>> 40617be1473112e8ddea800cf34b716ef9dfc81c:Winedata/views.py
            else :
                wine_recommand = wine_recommand[:10]
                serializer = ViewSerializer(wine_recommand, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else :
            return Response({"message": "평가한 와인 정보가 없습니다."}, status=status.HTTP_200_OK)

class ViewWineDetail(APIView):
    def get(self, request, Winedata_id):
        wine = Winedata.objects.get(id = Winedata_id)
        serializer = ViewWinedataDetail(wine)
        print(Winedata_id)
        return Response(serializer.data, status=status.HTTP_200_OK)

<<<<<<< HEAD:tweet/views.py
    def post(self, request, wine_id):
        serializer = CommentSerializer(data = request.data)

=======
    def post(self, request, Winedata_id):
        serializer = ReviewSerializer(data = request.data)
        
>>>>>>> 40617be1473112e8ddea800cf34b716ef9dfc81c:Winedata/views.py
        if serializer.is_valid():
            serializer.save(username = request.user, winedata_id = Winedata_id)
            wine = Winedata.objects.get(id = Winedata_id)
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


class ViewReview(APIView):
    def get(self, request, Review_id):
        wine = Review.objects.get(id = Review_id)
        serializer = WinedataReviewSerializer(wine)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserReviewView(APIView):
    def get(self, request):
        pagination = PageNumberPagination()
        pagination.page_size = 10
        pagination.page_query_param = 'page'
        review = Review.objects.filter(username_id = request.user.id)
        if review:
            p = pagination.paginate_queryset(queryset=review, request=request)

            serializer = UserReviewSerializer(p, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "작성한 글이 없습니다"}, status=status.HTTP_200_OK)


class BookmarkListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        bookmarklist = Winedata.objects.filter(bookmark=request.user.id)
        if bookmarklist:
            serializer = ViewSerializer(bookmarklist, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "저장된 와인 정보가 없습니다"}, status=status.HTTP_200_OK)


class BookmarkView(APIView):
    def post(self,request,winedata_id):
        winedata = get_object_or_404(Winedata, id= winedata_id)
        if request.user in winedata.bookmark.all():
            winedata.bookmark.remove(request.user)
            return Response("북마크에 삭제되었습니다", status = status.HTTP_200_OK)
        else:
            winedata.bookmark.add(request.user)
            return Response("북마크가 저장되었습니다", status = status.HTTP_200_OK)


class SaveList(APIView):
    def get(self, request):
        file_path = "Winedata\sample.json"
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
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

                webbrowser.get(chrome_path).open(img)
<<<<<<< HEAD:tweet/views.py

                tweet = Tweet.objects.create(name = name, content=content, tag=winetag, country=country, image=img, taster_name = username, grade = grade)
                tweet.save()
=======
                
                winedata = Winedata.objects.create(name = name, content=content, tag=winetag, country=country, image=img, taster_name = username, grade = grade)
                winedata.save()
>>>>>>> 40617be1473112e8ddea800cf34b716ef9dfc81c:Winedata/views.py

                time.sleep(0.5)

        return Response("저장됨")



