from django.urls import path
from Review import views


urlpatterns = [
    path('detail/', views.Update.as_view(), name='review'),
    path('detail/<int:Winedata_id>/<int:Review_id>/', views.Update.as_view(), name='update'),
]
