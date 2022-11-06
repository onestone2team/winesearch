from django.urls import path,include
from tweet import views
from django.conf.urls.static import static
from django.conf import settings    
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('', views.tweetAPI.as_view(), name="index"),
    path('views/', views.PostViewSet.as_view(), name='View_view'),
    path('views/<str:wine_type>/', views.ViewWineType.as_view(), name='View_view'),
    path('tweetlist/', views.tweetlist.as_view(), name="tweetlist"),
    path('search/', views.search.as_view(), name="search"),
    path('main/', views.SaveList.as_view(), name="main"),
    path('main/read/<int:write_no>', views.read_tweet, name='read_tweet'), # 게시글 상세페이지 접속
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns=format_suffix_patterns(urlpatterns)

