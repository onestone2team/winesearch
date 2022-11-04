from django.urls import path,include
from tweet import views
from django.conf.urls.static import static
from django.conf import settings    
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('', views.tweetAPI.as_view(), name="index"),
    path('tweetlist/', views.tweetlist.as_view(), name="tweetlist"),
    path('search/', views.search.as_view(), name="search"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns=format_suffix_patterns(urlpatterns)