from django.contrib import admin
from django.urls import path
from .views import BlogView,MyBlogsView,BlogByTagView,BlogListView
urlpatterns = [
    path('blog/', BlogView.as_view()),
    path('MyBlogs/', MyBlogsView.as_view()),
    path('blog/<uuid:uid>/', BlogView.as_view(), name='blog-detail'),
    # path('blog/tag/<str:tag_name>/', BlogByTagView.as_view(), name='blog-by-tag'),

    path('blog/tag/<str:tag_name>/', BlogListView.as_view(), name='blog-list-by-tag'),

 ]  