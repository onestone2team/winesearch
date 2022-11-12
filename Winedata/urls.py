from django.urls import path,include
from Winedata import views
from django.conf.urls.static import static
from django.conf import settings    
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('', views.PostViewSet().as_view(), name="index"),
    path('tag/<str:wine_type>/', views.ViewWineType.as_view(), name='tag_view'),
    path('recommend/', views.ViewRecommendWine.as_view(), name='recommend_view'),

    path('search/', views.ViewSearch.as_view(), name='search_view'),
    path('detail/<int:Winedata_id>/', views.ViewWineDetail.as_view(), name='detail_view'),
    path('Review/<int:review_id>/', views.ViewReview.as_view(), name='Review_view'),

    path('user/review/', views.UserReviewView.as_view(), name='user_Review'),
    path('user/bookmark/', views.BookmarkListView.as_view(), name='user_Review'),
    path('detail/<int:winedata_id>/bookmark/', views.BookmarkView.as_view(), name='bookmark_view'),
    #없애야 할 url
    path('main/', views.SaveList.as_view(), name="createWinedata"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns=format_suffix_patterns(urlpatterns)

