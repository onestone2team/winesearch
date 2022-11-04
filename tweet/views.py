from django.http import HttpResponse
from tweet.models import TweetModel
from user.models import UserModel
from django.db.models import Q
from tweet.serializers import searchSerializers
from user.serializers import userSerializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render,redirect
from rest_framework import status
# Create your views here.

class tweetAPI(APIView):
    def get(self, request,fromat=None):
        UserModels=UserModel.objects.all()
        UserModels=userSerializers(UserModels,many=True)
        return render(request,"search.html")
        # return Response(UserModels.data)
    def post(self,request,format=None):
        Serializers =userSerializers(data=request.data)
        if Serializers.is_valid():
            Serializers.save()
            return Response(Serializers.data)
        else:
            print(Serializers.errors)
        return Response()


class tweetlist(APIView):
    def get(self,request,format=None):
        searchs=TweetModel.objects.all()
        Serializers=searchSerializers(searchs,many=True)
        return Response(Serializers.data)
    def post(self,request,format=None):
        Serializers =searchSerializers(data=request.data)
        if Serializers.is_valid():
            Serializers.save()
            return Response(Serializers.data)
        else:
            print(Serializers.errors)
        return Response()
class search(APIView):
    def get(self,request):
        queryset = TweetModel.objects.all()
        searchword = request.GET.get('search')
        print(searchword)
        if searchword:
            queryset=queryset.filter(Q(name__icontains=searchword)|Q(tag__icontains=searchword)|Q(content__icontains=searchword))
        serializers=searchSerializers(queryset,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

class test():
    def get(request):
        return ('search.html')
























        # UserModels=UserModel.objects.all()
        # UserModels=userSerializers(UserModels,many=True)
        # search_keyword = request.POST['search']
        # print(search_keyword)
        # if not search_keyword:
        #     return render(request, 'search.html', {'name': UserModels})
        # else:
        #     if len(search_keyword) >= 2 :
        #         searched = TweetModel.objects.filter(Q(name__icontains=search_keyword)|Q(tag__icontains=search_keyword))              
        #         for i in searched:
        #             print(searched)
        #         return render(request, 'search.html',{'searched': searched})
        #     if len(search_keyword) <= 1:
        #         return render(request, 'search.html', {'name': UserModels})












    # if request.method == "POST":
    #     search_keyword = request.POST['search']
    #     print(search_keyword)
    #     if not search_keyword:
    #         return redirect('/main')
    #     else:
    #         if len(search_keyword) >= 2 :
    #             searched = TweetModel.objects.filter(Q(name__icontains=search_keyword)|Q(tags__icontains=search_keyword))              
    #             for i in searched:
    #                 print(searched)
    #             return render(request, 'tweet/searhed.html',{'searched': searched})
    #         if len(search_keyword) <= 1:
    #             return redirect('/main')