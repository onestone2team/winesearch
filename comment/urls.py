from django.urls import path
from comment import views


urlpatterns = [
    path('detail/', views.ReviewList.as_view(), name='review'),
    path('detail/<int:tweet_id>/<int:comment_id>/', views.Update.as_view(), name='update'),
]
