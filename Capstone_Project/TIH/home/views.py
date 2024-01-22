from django.shortcuts import render
from rest_framework.response import Response
from .serializers import BlogDSerializer, BlogSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import  IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Blog, Comment, Reply
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db import connections
from django.db.models import F
from django.http import JsonResponse



class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # def get(self, request):
    #     try:
    #         # Assuming 'created_at' is a field in your Blog model
    #         random_blogs = Blog.objects.raw([
    #             {
    #                 '$match': {
    #                     'title': {'$regex': request.GET.get('search', ''), '$options': 'i'}
    #                     # Add other conditions for blog_text and user__username if needed
    #                 }
    #             },
    #             {
    #                 '$addFields': {
    #                     'random_order': {'$rand': {}}
    #                 }
    #             },
    #             {
    #                 '$sort': {'random_order': 1}
    #             },
    #             {
    #                 '$limit': 5
    #             }
    #         ])

    #         serializer = BlogSerializer(random_blogs, many=True)

    #         return JsonResponse({
    #             'data': serializer.data,
    #             'message': 'Random blogs fetched successfully'
    #         }, status=status.HTTP_201_CREATED)
    #     except Exception as e:
    #         print(e)
    #         return JsonResponse({
    #             'data': [],
    #             'message': 'Something went wrong'
    #         }, status=status.HTTP_400_BAD_REQUEST)






#     def get(self, request):
#         try:
#             # blogs = Blog.objects.filter(user = request.user)
#             blogs = Blog.objects.all().order_by('?')
#             if request.GET.get('search'):
#                 search = request.GET.get('search')
#                 # blogs = blogs.filter(Q(title__icontains = search) | Q(blog_text__icontains = search) | Q(username__icontains = search))
#                 blogs = blogs.filter(
#     Q(title__icontains=search) | 
#     Q(blog_text__icontains=search) | 
#     Q(user__username__icontains=search)
# )

#             page_number = request.GET.get('page', 1)
#             paginator = Paginator(blogs, 5)
#             serializer = BlogSerializer(paginator.page(page_number), many = True)
#             # serializer = BlogSerializer(blogs, many = True)
#             return Response({
#                 'data' : serializer.data,
#                 'message' : 'blogs fetched successfully'
#             },status = status.HTTP_201_CREATED)
#         except Exception as e:
             
#              print(e)
#              return Response({
#                     'data' : serializer.errors,
#                     'message' : 'something went wrong'
#                 }, status = status.HTTP_400_BAD_REQUEST)  
    # def get(self, request):
    #    def get(self, request):




    # def get(self, request):
    #     try:
    #         blogs = Blog.objects.all().order_by('?')

    #         if request.GET.get('search'):
    #             search = request.GET.get('search')  
    #             search_terms = [term.strip() for term in search.split('$')]
    #             print(search)
    #             print(search_terms)

    #             # Construct a dynamic Q object to combine multiple conditions
    #             conditions = Q()
    #             for term in search_terms:
    #                 conditions &= (
    #                     Q(title__icontains=term) |
    #                     Q(user__username__icontains=term)
    #                 )

    #             # Apply the constructed conditions to filter the queryset
    #             blogs = blogs.filter(conditions)


    #         page_number = request.GET.get('page', 1)
    #         paginator = Paginator(blogs, 5)
    #         serializer = BlogSerializer(paginator.page(page_number), many=True)

    #         return Response({
    #             'data': serializer.data,
    #             'message': 'blogs fetched successfully'
    #         }, status=status.HTTP_201_CREATED)

    #     except Exception as e:
    #         print(e)
    #         return Response({
    #             'data': serializer.errors,
    #             'message': 'something went wrong'
    #         }, status=status.HTTP_400_BAD_REQUEST)
        



        
        
    # def get_by_uid(self, request, uid):
    #     try:
    #         blog = get_object_or_404(Blog, uid=uid)
    #         serializer = BlogSerializer(blog)
            
    #         return Response({
    #             'data': serializer.data,
    #             'message': 'blog fetched successfully'
    #         }, status=status.HTTP_200_OK)

    #     except Exception as e:
    #         print(e)
    #         return Response({
    #             'data': [],
    #             'message': 'something went wrong'
    #         }, status=status.HTTP_400_BAD_REQUEST)

    # # Modify this method
    # def get(self, request, *args, **kwargs):
    #     uid = self.kwargs.get('uid')
    #     if uid:
    #         return self.get_by_uid(request, uid)
    #     else:
    #         # Call the 'get' method on the superclass (APIView)
    #         return super().get(request, *args, **kwargs)




    # def get(self, request, *args, **kwargs):
    #     uid = kwargs.get('uid')
        
    #     if uid:
    #         return self.get_by_uid(request, uid)
    #     else:
    #         try:
    #             blogs = Blog.objects.all()

    #             if request.GET.get('search'):
    #                 search = request.GET.get('search')  
    #                 search_terms = [term.strip() for term in search.split('$')]
    #                 print(search)
    #                 print(search_terms)

    #                 # Construct a dynamic Q object to combine multiple conditions
    #                 conditions = Q()
    #                 for term in search_terms:
    #                     conditions &= (
    #                         Q(title__icontains=term) |
    #                         Q(user__username__icontains=term)
    #                     )

    #                 # Apply the constructed conditions to filter the queryset
    #                 blogs = blogs.filter(conditions)

    #             page_number = request.GET.get('page', 1)
    #             paginator = Paginator(blogs, 5)
    #             serializer = BlogSerializer(paginator.page(page_number), many=True)

    #             return Response({
    #                 'data': serializer.data,
    #                 'message': 'blogs fetched successfully'
    #             }, status=status.HTTP_201_CREATED)

    #         except Exception as e:
    #             print(e)
    #             return Response({
    #                 'data': [],
    #                 'message': 'something went wrong'
    #             }, status=status.HTTP_400_BAD_REQUEST)

    # def get_by_uid(self, request, uid):
    #     try:
    #         blog = get_object_or_404(Blog, uid=uid)
    #         serializer = BlogSerializer(blog)
            
    #         return Response({
    #             'data': serializer.data,
    #             'message': 'blog fetched successfully'
    #         }, status=status.HTTP_200_OK)

    #     except Exception as e:
    #         print(e)
    #         return Response({
    #             'data': [],
    #             'message': 'something went wrong'
    #         }, status=status.HTTP_400_BAD_REQUEST)



    def get(self, request, *args, **kwargs):
        try:
            blogs = Blog.objects.all()

            if request.GET.get('search'):
                search = request.GET.get('search')  
                search_terms = [term.strip() for term in search.split('$')]
                print(search)
                print(search_terms)

                # Construct a dynamic Q object to combine multiple conditions
                conditions = Q()
                for term in search_terms:
                    conditions &= (
                        Q(title__icontains=term) |
                        Q(user__username__icontains=term)
                    )

                # Apply the constructed conditions to filter the queryset
                blogs = blogs.filter(conditions)

            page_number = request.GET.get('page', 1)
            paginator = Paginator(blogs, 5)
            serializer = BlogSerializer(paginator.page(page_number), many=True)

            return Response({
                'data': serializer.data,
                'message': 'Blogs fetched successfully'
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                'data': [],
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)


    # def post(self, request):
    #     try:
    #         data = request.data
    #         print(request.user)
    #         data['user'] = request.user.id 
    #         serializer = BlogSerializer(data = data)

    #         if not serializer.is_valid():
    #             return Response({
    #                 'data' : serializer.errors,
    #                 'message' : 'something went wrong'
    #             }, status = status.HTTP_400_BAD_REQUEST)
    #         serializer.save()

    #         return Response({
    #             'data' : serializer.data,
    #             "message": "Blog post created successfully"
    #             }, status=status.HTTP_201_CREATED)
        
    #     except Exception as e:
    #         print(e)
    #         return Response({
    #                 'data' : serializer.errors,
    #                 'message' : 'something went wrong'
    #             }, status = status.HTTP_400_BAD_REQUEST) 

    def post(self, request):
        try:
            data = request.data.copy()  # Create a mutable copy of QueryDict
            print(request.user)
            data['user'] = request.user.id 
            serializer = BlogSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()

            return Response({
                'data': serializer.data,
                "message": "Blog post created successfully"
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({
                'data': [],
                'message': 'something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)



    # def post(self, request):
    #     try:
    #         data = request.data
    #         data['user'] = request.user.id 
    #         serializer = BlogSerializer(data=data)

    #         if not serializer.is_valid():
    #             return Response({
    #                 'data': serializer.errors,
    #                 'message': 'Validation error. Please check your data.'
    #             }, status=status.HTTP_400_BAD_REQUEST)
            
    #         serializer.save()

    #         return Response({
    #             'data': serializer.data,
    #             'message': 'Blog post created successfully'
    #         }, status=status.HTTP_201_CREATED)
        
    #     except Exception as e:
    #         print(e)  # Log the exception for debugging
    #         return Response({
    #             'data': 'Internal server error.',
    #             'message': 'Something went wrong.'
    #         }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def patch(self, request):
    #     try:
    #         data = request.data 
    #         blog = Blog.objects.filter(uid = data.get('uid'))

    #         if not blog.exists():
    #             return Response({
    #                 'data' : {},
    #                 'message' : 'invalid blog uid'
    #             }, status = status.HTTP_400_BAD_REQUEST)  
    #         if request.user != blog[0].user:
    #             return Response({
    #                 'data' : {},
    #                 'message' : 'you are not authorized to do this'
    #             }, status = status.HTTP_400_BAD_REQUEST)  
    #         serializer = BlogSerializer(blog[0],data =data, partial = True)

    #         if not serializer.is_valid():
    #             return Response({
    #                 'data' : serializer.errors,
    #                 'message' : 'something went wrong'
    #             }, status = status.HTTP_400_BAD_REQUEST) 
    #         serializer.save()
    #         return Response({
    #             'data' : serializer.data,
    #             'message' : "blog updated succesfully" 
    #         }, status=status.HTTP_201_CREATED)
 

    #     except Exception as e:
    #         print(e)
    #         return Response({
    #                 'data' : [],
    #                 'message' : 'something went wrong'
    #             }, status = status.HTTP_400_BAD_REQUEST) 
        



    def patch(self, request):
        try:
            data = request.data
            blog = Blog.objects.filter(uid=data.get('uid'))

            if not blog.exists():
                return Response({
                    'data': {},
                    'message': 'Invalid blog UID'
                }, status=status.HTTP_400_BAD_REQUEST)

            if request.user != blog[0].user:
                return Response({
                    'data': {},
                    'message': 'You are not authorized to do this'
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer = BlogSerializer(blog[0], data=data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response({
                'data': serializer.data,
                'message': "Blog updated successfully"
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                'data': {},
                'message': 'Something went wrong'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request):
        try:
            data = request.data 
            blog = Blog.objects.filter(uid = data.get('uid'))

            if not blog.exists():
                return Response({
                    'data' : {},
                    'message' : 'invalid blog uid'
                }, status = status.HTTP_400_BAD_REQUEST)  
            if request.user != blog[0].user:
                return Response({
                    'data' : {},
                    'message' : 'you are not authorized to do this'
                }, status = status.HTTP_400_BAD_REQUEST)  
            blog[0].delete()
            return Response({
                'data':{},
                'message' : "blog deleted successfully"
            },status=status.HTTP_202_ACCEPTED)

 

        except Exception as e:
            print(e)
            return Response({
                    'data' : [],
                    'message' : 'something went wrong'
                }, status = status.HTTP_400_BAD_REQUEST) 
        

class MyBlogsView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        try:
            blogs = Blog.objects.filter(user = request.user)
            if request.GET.get('search'):
                search = request.GET.get('search')
                # blogs = blogs.filter(Q(title__icontains = search) | Q(blog_text__icontains = search) | Q(username__icontains = search))
                blogs = blogs.filter(
    Q(title__icontains=search) | 
    Q(blog_text__icontains=search) | 
    Q(user__username__icontains=search)
)
            serializer = BlogSerializer(blogs, many = True)
            return Response({
                'data' : serializer.data,
                'message' : 'blogs fetched successfully'
            },status = status.HTTP_201_CREATED)
        except Exception as e:
             
             print(e)
             return Response({
                    'data' : serializer.errors,
                    'message' : 'something went wrong'
                }, status = status.HTTP_400_BAD_REQUEST)  


from rest_framework.generics import ListAPIView

class BlogByTagView(ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        tag_name = self.kwargs.get('tag_name')
        if tag_name:
            return Blog.objects.filter(tags__name=tag_name)
        else:
            return Blog.objects.all()

# class BlogListView(APIView):
#     def get(self, request, *args, **kwargs):
#         try:
#             tag_name = self.kwargs.get('tag_name')  # Assuming your URL pattern includes the tag name parameter
#             blogs = Blog.objects.all()

#             if tag_name:
#                 blogs = blogs.filter(tags__contains=[tag_name])

#             if request.GET.get('search'):
#                 search = request.GET.get('search')
#                 search_terms = [term.strip() for term in search.split('$')]

#                 # Construct a dynamic Q object to combine multiple conditions
#                 conditions = Q()
#                 for term in search_terms:
#                     conditions &= (
#                         Q(title__icontains=term) |
#                         Q(user__username__icontains=term)
#                     )

#                 # Apply the constructed conditions to filter the queryset
#                 blogs = blogs.filter(conditions)

#             page_number = request.GET.get('page', 1)
#             paginator = Paginator(blogs, 5)
#             serializer = BlogSerializer(paginator.page(page_number), many=True)

#             return Response({
#                 'data': serializer.data,
#                 'message': 'Blogs fetched successfully'
#             }, status=status.HTTP_200_OK)

#         except Exception as e:
#             print(e)
#             return Response({
#                 'data': [],
#                 'message': 'Something went wrong'
#             }, status=status.HTTP_400_BAD_REQUEST)
        


class BlogListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            tag_name = self.kwargs.get('tag_name')
            blogs = Blog.objects.all()

            if tag_name:
                # Use __icontains for TextField
                blogs = blogs.filter(tags__icontains=tag_name)

            if request.GET.get('search'):
                search = request.GET.get('search')
                search_terms = [term.strip() for term in search.split('$')]

                # Construct a dynamic Q object to combine multiple conditions
                conditions = Q()
                for term in search_terms:
                    conditions &= (
                        Q(title__icontains=term) |
                        Q(user__username__icontains=term)
                    )

                # Apply the constructed conditions to filter the queryset
                blogs = blogs.filter(conditions)

            page_number = request.GET.get('page', 1)
            paginator = Paginator(blogs, 5)
            serialized_blogs = BlogSerializer(paginator.page(page_number), many=True).data

            return Response({
                'data': serialized_blogs,
                'message': 'Blogs fetched successfully'
            }, status=status.HTTP_200_OK)

        except Blog.DoesNotExist:
            return Response({
                'data': [],
                'message': 'No blogs found'
            }, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # logger.error(f"An error occurred: {e}")
            return Response({
                'data': [],
                'message': 'Something went wrong'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



class BlogDetailView(APIView):
    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uid')

        try:
            blog = get_object_or_404(Blog, uid=uid)
            serializer = BlogDSerializer(blog)
            
            return Response({
                'data': serializer.data,
                'message': 'Blog fetched successfully'
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                'data': [],
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
        
    # def post(self, request, *args, **kwargs):
    #     uid = kwargs.get('uid')

    #     try:
    #         blog = get_object_or_404(Blog, uid=uid)
    #         user = request.user  # Assuming the user is authenticated

    #         # Extract comment data from the request
    #         comment_text = request.data.get('text')
    #         parent_comment_id = request.data.get('parent_comment_id')  # If you want to support replies

    #         # Create a new comment instance
    #         comment = Comment.objects.create(user=user, text=comment_text)

    #         # If it's a reply, set the parent_comment
    #         if parent_comment_id:
    #             parent_comment = get_object_or_404(Comment, id=parent_comment_id)
    #             comment.parent_comment = parent_comment
    #             comment.save()

    #         # Add the comment to the blog's comments
    #         blog.comments.add(comment)

    #         serializer = BlogDSerializer(blog)
            
    #         return Response({
    #             'data': serializer.data,
    #             'message': 'Comment posted successfully'
    #         }, status=status.HTTP_201_CREATED)

    #     except Exception as e:
    #         print(e)
    #         return Response({
    #             'data': [],
    #             'message': 'Something went wrong'
    #         }, status=status.HTTP_400_BAD_REQUEST)
        

    # def post(self, request, *args, **kwargs):
    #     uid = kwargs.get('uid')

    #     try:
    #         blog = get_object_or_404(Blog, uid=uid)
    #         user = request.user  # Assuming the user is authenticated

    #         # Extract comment data from the request
    #         comment_text = request.data.get('text')
    #         parent_comment_id = request.data.get('parent_comment_id')  # If you want to support replies

    #         # Create a new comment instance
    #         comment = Comment.objects.create(user=user, text=comment_text)

    #         # If it's a reply, set the parent_comment
    #         if parent_comment_id:
    #             parent_comment = get_object_or_404(Comment, uid=parent_comment_id)
    #             comment.parent_comment = parent_comment
    #             comment.save()

    #         # Add the comment to the blog's comments
    #         blog.comments.add(comment)

    #         serializer = BlogDSerializer(blog)
            
    #         return Response({
    #             'data': serializer.data,
    #             'message': 'Comment posted successfully'
    #         }, status=status.HTTP_201_CREATED)

    #     except Exception as e:
    #         print(e)
    #         return Response({
    #             'data': [],
    #             'message': 'Something went wrong'
    #         }, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request, *args, **kwargs):
        uid = kwargs.get('uid')

        try:
            blog = get_object_or_404(Blog, uid=uid)
            user = request.user  # Assuming the user is authenticated

            # Extract comment data from the request
            comment_text = request.data.get('text')
            parent_comment_id = request.data.get('parent_comment_id')

            # Create a new comment instance
            comment = Comment.objects.create(user=user, text=comment_text)

            # If it's a reply, create a new reply instance
            if parent_comment_id:
                parent_comment = get_object_or_404(Comment, uid=parent_comment_id)
                reply_text = request.data.get('text')  # Extract reply text
                reply = Reply.objects.create(comment=parent_comment, text=reply_text)

            # Add the comment to the blog's comments
            blog.comments.add(comment)

            # Serialize the updated blog
            serializer = BlogDSerializer(blog)

            return Response({
                'data': serializer.data,
                'message': 'Comment posted successfully'
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({
                'data': [],
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
    