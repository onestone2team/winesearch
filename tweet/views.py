from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
import json
from bs4 import BeautifulSoup as BS    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tweet.serializer import ViewSerializer
from tweet.models import Tweet
from . import datasave
import time
import googletrans
from rest_framework import generics




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

    def get(self, request):
        pass

# 데이터 저장용 CLASS 배포 시 안씀
translator = googletrans.Translator()

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

