from django.contrib import admin
from django.urls import path
from .views import BlogView,MyBlogsView
urlpatterns = [
    path('blog/', BlogView.as_view()),
    path('MyBlogs/', MyBlogsView.as_view())
 ]