from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from tweet.models import Tweet

# Create your views here.

class ViewList(APIView):
    pass

class SaveList(APIView):
    def get(self, request):
        file_path = "tweet\sample.json"
        with open(file_path, "r") as json_file:
            json_data = json.load(json_file)
            for i in range(len(json_data)):
                name = json_data[i]["title"]
                content = json_data[i]["description"]
                tag = json_data[i]["variety"]
                country = json_data[i]["country"]
                
                tweet = Tweet.objects.create(name = name, content=content, tag=tag, country=country)
                tweet.save()

        return Response("저장됨")
    