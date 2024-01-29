from django.contrib import admin
from django.urls import path
from .views import BlogView, CommentViewSet,MyBlogsView,BlogByTagView,BlogListView,BlogDetailView,UpvoteBlogView
# from .views import CommentViewSet, add_reply





urlpatterns = [
    path('blog/', BlogView.as_view()),
    path('MyBlogs/', MyBlogsView.as_view()),
    path('blog/<uuid:uid>/', BlogDetailView.as_view(), name='blog-detail'),
    # path('blog/tag/<str:tag_name>/', BlogByTagView.as_view(), name='blog-by-tag'),.
    path('blog/comments/<uuid:uid>/', BlogDetailView.as_view(), name='blog-detail'),


    path('blog/tag/<str:tag_name>/', BlogListView.as_view(), name='blog-list-by-tag'),


    path('blog/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    # path('blog/comments/<uuid:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='comment-detail'),

    path('blog/comments/<uuid:pk>/add_reply/', CommentViewSet.as_view({'post': 'add_reply'}), name='add-reply'),


    path('blog/<uuid:blog_id>/upvote/', UpvoteBlogView.as_view(), name='upvote_blog'),


 ]  