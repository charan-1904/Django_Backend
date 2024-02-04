from django.contrib import admin
from django.urls import path
from .views import BlogView, CommentViewSet, ContactFormView,MyBlogsView,BlogByTagView,BlogListView,BlogDetailView,UpvoteBlogView, UserBlogsView,FeaturedBlogsView
# from .views import CommentViewSet, add_reply





urlpatterns = [
    path('blog/', BlogView.as_view()),
    path('MyBlogs/', MyBlogsView.as_view()),
    path('blog/<uuid:uid>/', BlogDetailView.as_view(), name='blog-detail'),
    # path('blog/tag/<str:tag_name>/', BlogByTagView.as_view(), name='blog-by-tag'),.
    path('blog/comments/<uuid:uid>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/is_featured', FeaturedBlogsView.as_view(), name = 'featured_view'),
    path('blog/upvote/<uuid:uid>/', UpvoteBlogView.as_view(), name='upvote_blog'),
    # path('blog/tag/<str:tag_name>/', BlogListView.as_view(), name='blog-list-by-tag'),
    path('blog/tag/<str:tag_name>/', BlogByTagView.as_view(), name='blog-lisby-tag'),


    # path('blog/<str:username>/', UserBlogsView.as_view(), name='user_blogs'),

    path('blog/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    # path('blog/comments/<uuid:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='comment-detail'),

    path('blog/<uuid:pk>/add_reply/', CommentViewSet.as_view({'post': 'add_reply'}), name='add-reply'),
    path('blog/<str:username>/', UserBlogsView.as_view(), name='user_blogs'),
    path('user-blogs/<str:username>/', UserBlogsView.as_view(), name='user_blogs_by_user'),


    path('blog/<uuid:blog_id>/upvote/', UpvoteBlogView.as_view(), name='upvote_blog'),
    path('contact/', ContactFormView.as_view(), name='contact-form'),



 ]  