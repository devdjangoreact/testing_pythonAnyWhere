from django.urls import path, re_path

from .views import TestListView, TestDetail, SetTestListView, SetTestDetail, TestWithSetView
from .views import CategoryDetail, CategoryList, HashTagList, HashTagDetail
from .views import TestListList, TestListDetail, SetTestListList, SetTestListDetail

urlpatterns = [
    
    path("category/", CategoryList.as_view()),
    path("category/<int:pk>/", CategoryDetail.as_view()),

    path("hashtag/", HashTagList.as_view()),
    path("hashtag/<int:pk>/", HashTagDetail.as_view()),    
    
    path("test/", TestListView.as_view()),
    path("test/<int:pk>/", TestDetail.as_view()),

    path("settest/", SetTestListView.as_view()),
    path("settest/<int:pk>/", SetTestDetail.as_view()),
    
    path("testwithset", TestWithSetView.as_view()),
    
    path("testlist/", TestListList.as_view()),
    path("testlist/<int:pk>/", TestListDetail.as_view()),
    
    path("settestlist/", SetTestListList.as_view()),
    path("settestlist/<int:pk>/", SetTestListDetail.as_view()),
]
