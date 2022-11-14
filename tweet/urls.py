from django.urls import path,include
from tweet import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    path('', views.PostViewSet().as_view(), name="index"),
    path('tag/<str:wine_type>/', views.ViewWineType.as_view(), name='tag_view'),
    path('recommend/', views.ViewRecommendWine.as_view(), name='recommend_view'),

    path('search/', views.ViewSearch.as_view(), name='search_view'),
    path('detail/<int:wine_id>/', views.ViewWineDetail.as_view(), name='detail_view'),
    path('comment/<int:comment_id>/', views.ViewComment.as_view(), name='comment_view'),

    path('user/review/', views.UserCommentView.as_view(), name='user_comment'),
    path('user/bookmark/', views.BookmarkListView.as_view(), name='user_comment'),
    path('detail/<int:wine_id>/bookmark/', views.BookmarkView.as_view(), name='bookmark_view'),
    #없애야 할 url
    path('main/', views.SaveList.as_view(), name="createtweet"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns=format_suffix_patterns(urlpatterns)

