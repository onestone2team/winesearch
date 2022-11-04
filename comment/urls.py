from django.urls import path
from . import views


urlpatterns = [
    path('detail/', views.review, name='review'),
    path('detail/<int:tweet_id>/', views.update, name='update'),
]
