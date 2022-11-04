from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [

    path('main/', views.SaveList.as_view(), name='article_view'),
    path('views/', views.PostViewSet.as_view(), name='View_view'),
    path('views/<str:wine_type>/', views.ViewWineType.as_view(), name='View_view'),

]