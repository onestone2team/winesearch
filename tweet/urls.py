from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('main/', views.SaveList.as_view(), name='article_view'),
    path('save/', views.ViewList.as_view(), name='View_view'),
]