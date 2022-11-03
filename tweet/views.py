from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from tweet.models import Tweet
from bs4 import BeautifulSoup as BS    
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tweet.serializer import ViewSerializer
from . import datasave
import time
import googletrans
translator = googletrans.Translator()

# Create your views here.

class ViewList(APIView):
    def get(self, request):
        
        winedata = Tweet.objects.all()
        serializer = ViewSerializer(winedata, many=True)
        wineset = serializer.data
        wineclass = []
        for i in wineset:
            tagedata=i['tag']
            data = tagedata.split(" ")
            result = data[0]
            tag = datasave.searchwine(result)
            print(tag)
        

        return Response(serializer.data, status=status.HTTP_200_OK)

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

