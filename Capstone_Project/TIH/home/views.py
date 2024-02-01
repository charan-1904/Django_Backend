from django.shortcuts import render
from rest_framework.response import Response

from accounts import serializers
from accounts.models import CustomUser
from .serializers import BlogDSerializer, BlogSerializer, BlogTSerializer, CommentSerializer, ReplySerializer
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
import traceback




class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # def get(self, request, *args, **kwargs):
    #     try:
    #         blogs = Blog.objects.all()

    #         blogs = Blog.objects.all()

    #     # Construct the response for each blog in the desired format
    #         blogs_data = []
    #         for blog in blogs:
    #             blog_data = {
    #                 "id": blog.uid,
    #                 "image": f"{blog.main_image}" if blog.main_image else "",
    #                 "title": blog.title,
    #                 "post_link": str(blog.uid),
    #                 "tag_link": blog.tags,
    #                 "tag": blog.tags,
    #                 "date": blog.created_at.strftime("%d %B"),  # Format date as needed
    #                 "votes": 0,  # You may adjust this based on your logic
    #                 "user_username": blog.user.username if blog.user else "",
    #             }
    #             blogs_data.append(blog_data)    

    #         blogs = Blog.objects.all()

    #         # If search parameter is provided, apply the filter
    #         if request.GET.get('search'):
    #             search = request.GET.get('search')
    #             search_terms = [term.strip() for term in search.split('$')]

    #             # Construct a single condition using the logical OR operator
    #             conditions = Q()
    #             for term in search_terms:
    #                 conditions |= Q(title__icontains=term) | Q(user__username__icontains=term) | Q(blog_text__icontains=term)

    #             # Apply the constructed condition to filter the queryset
    #             blogs = blogs.filter(conditions)

    #         # Sort the queryset by a specific field, for example, 'created_at'
    #         blogs = blogs.order_by('created_at')


    #         search_blogs_data = []
    #         for blog in blogs:
    #             search_blog_data = {
    #                 "id": blog.uid,
    #                 "image": f"{blog.main_image}" if blog.main_image else "",
    #                 "title": blog.title,
    #                 "post_link": str(blog.uid),
    #                 "tag_link": blog.tags,
    #                 "tag": blog.tags,
    #                 "date": blog.created_at.strftime("%d %B"),  # Format date as needed
    #                 "votes": 0,  # You may adjust this based on your logic
    #                 "user_username": blog.user.username if blog.user else "",
    #             }
    #             search_blogs_data.append(search_blog_data)

    #         # Include the filtered blogs data in the main blogs_data
    #         blogs_data += search_blogs_data


    #         # Print the count of filtered blogs
    #         print(blogs.count())

    #         # Paginate the blogs
    #         page_number = request.GET.get('page', 1)
    #         paginator = Paginator(blogs, 5)

    #         try:
    #             paginated_blogs = paginator.page(page_number)
    #         except Exception as e:
    #             print(e)
    #             paginated_blogs = paginator.page(paginator.num_pages)

    #         # Serialize the paginated blogs
    #         serializer = BlogSerializer(paginated_blogs, many=True)

    #         # Return the response
    #         return Response({
    #             'data': blogs_data,
    #             'message': 'Blogs fetched successfully'
    #         }, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         print(e)
    #         return Response({
    #             'data': [],
    #             'message': 'Something went wrong'
    #         }, status=status.HTTP_400_BAD_REQUEST)




    # def get(self, request, *args, **kwargs):
    #     try:
    #         # Fetch all blogs
    #         blogs = Blog.objects.all()

    #         # Construct the response for each blog in the desired format
    #         blogs_data = []
    #         for blog in blogs:
    #             blog_data = {
    #                 "id": blog.uid,
    #                 "image": f"{blog.main_image}" if blog.main_image else "",
    #                 "title": blog.title,
    #                 "post_link": str(blog.uid),
    #                 "tag_link": blog.tags,
    #                 "tag": blog.tags,
    #                 "date": blog.created_at.strftime("%d %B %Y %H:%M"),
    #                 "votes": 0,  # You may adjust this based on your logic
    #                 "user_username": blog.user.username if blog.user else "",
    #             }
    #             blogs_data.append(blog_data)

    #         # Fetch all blogs again for applying search conditions
    #         blogs = Blog.objects.all()
    #         blogs_data = sorted(blogs_data, key=lambda x: x['date'], reverse=True)


    #         # If search parameter is provided, apply the filter
    #         if request.GET.get('search'):
    #             search = request.GET.get('search')
    #             search_terms = [term.strip() for term in search.split('$')]

    #             # Construct a single condition using the logical OR operator
    #             conditions = Q()
    #             for term in search_terms:
    #                 conditions |= Q(title__icontains=term) | Q(user__username__icontains=term) | Q(blog_text__icontains=term)

    #             # Apply the constructed condition to filter the queryset
    #             blogs = blogs.filter(conditions)

    #             # Construct the response for each filtered blog in the desired format
    #             blogs_data = []
    #             for blog in blogs:
    #                 search_blog_data = {
    #                     "id": blog.uid,
    #                     "image": f"{blog.main_image}" if blog.main_image else "",
    #                     "title": blog.title,
    #                     "post_link": str(blog.uid),
    #                     "tag_link": blog.tags,
    #                     "tag": blog.tags,
    #                     "date": blog.created_at.strftime("%d %B"),  # Format date as needed
    #                     "votes": blog.upvotes,  # You may adjust this based on your logic
    #                     "user_username": blog.user.username if blog.user else "",
    #                 }
    #                 blogs_data.append(search_blog_data)
                

    #             # Include the filtered blogs data in the main blogs_data
    #             # blogs_data += blogs_data

    #         # Sort the queryset by a specific field, for example, 'created_at'
    #         blogs = blogs.order_by('-created_at')

    #         # Print the count of filtered blogs
    #         print(blogs.count())

    #         # Paginate the blogs_data
    #         page_number = request.GET.get('page', 2)
    #         paginator = Paginator(blogs_data, 20)

    #         try:
    #             paginated_blogs_data = paginator.page(page_number)
    #         except Exception as e:
    #             print(e)
    #             paginated_blogs_data = paginator.page(paginator.num_pages)

    #         # Return the response with paginated blogs_data
    #         return Response({
    #             'data': paginated_blogs_data.object_list,  # Use object_list to get the paginated data
    #             'message': 'Blogs fetched successfully'
    #         }, status=status.HTTP_200_OK)

    #     except Exception as e:
    #         print(e)
    #         return Response({
    #             'data': [],
    #             'message': 'Something went wrong'
    #         }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            # Fetch all blogs
            blogs = Blog.objects.all()

            # Construct the response for each blog in the desired format
            blogs_data = []
            for blog in blogs:
                blog_data = {
                    "id": blog.uid,
                    "image": f"{blog.main_image}" if blog.main_image else "",
                    "title": blog.title,
                    "post_link": str(blog.uid),
                    "tag_link": blog.tags,
                    "tag": blog.tags,
                    "date": blog.created_at.strftime("%d %B %Y %H:%M"),
                    "votes": 0,  # You may adjust this based on your logic
                    "user_username": blog.user.username if blog.user else "",
                }
                blogs_data.append(blog_data)

            # If search parameter is provided, apply the filter
            if request.GET.get('search'):
                search = request.GET.get('search')
                search_terms = [term.strip() for term in search.split('$')]

                # Construct a single condition using the logical OR operator
                conditions = Q()
                for term in search_terms:
                    conditions |= Q(title__icontains=term) | Q(user__username__icontains=term) | Q(summary__icontains=term)

                # Apply the constructed condition to filter the queryset
                blogs = blogs.filter(conditions)

                # Construct the response for each filtered blog in the desired format
                blogs_data = []
                for blog in blogs:
                    search_blog_data = {
                        "id": blog.uid,
                        "image": f"{blog.main_image}" if blog.main_image else "",
                        "title": blog.title,
                        "post_link": str(blog.uid),
                        "tag_link": blog.tags,
                        "tag": blog.tags,
                        "date": blog.created_at.strftime("%d %B"),  # Format date as needed
                        "votes": blog.upvotes,  # You may adjust this based on your logic
                        "user_username": blog.user.username if blog.user else "",
                    }
                    blogs_data.append(search_blog_data)

            # Sort the blogs_data by date in descending order
            blogs_data = sorted(blogs_data, key=lambda x: x['date'], reverse=True)

            # Return the response with all blogs_data
            return Response({
                'data': blogs_data,
                'message': 'Blogs fetched successfully'
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                'data': [],
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)


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



    #



    # def patch(self, request):
    #     try:
    #         data = request.data
    #         blog = Blog.objects.filter(uid=data.get('uid'))

    #         if not blog.exists():
    #             return Response({
    #                 'data': {},
    #                 'message': 'Invalid blog UID'
    #             }, status=status.HTTP_400_BAD_REQUEST)

    #         if request.user != blog[0].user:
    #             return Response({
    #                 'data': {},
    #                 'message': 'You are not authorized to do this'
    #             }, status=status.HTTP_400_BAD_REQUEST)

    #         serializer = BlogSerializer(blog[0], data=data, partial=True)

    #         if not serializer.is_valid():
    #             return Response({
    #                 'data': serializer.errors,
    #                 'message': 'Something went wrong'
    #             }, status=status.HTTP_400_BAD_REQUEST)

    #         serializer.save()
    #         return Response({
    #             'data': serializer.data,
    #             'message': "Blog updated successfully"
    #         }, status=status.HTTP_201_CREATED)

        # except Exception as e:
        #     print(e)
        #     return Response({
        #         'data': {},
        #         'message': 'Something went wrong'
        #     }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def patch(self, request):
        try:
            data = request.data
            print("Request Data:", data)

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
                print("Serializer Errors:", serializer.errors)
                return Response({
                    'data': serializer.errors,
                    'message': 'Validation errors'
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            print("Updated Blog Data:", serializer.data)

            return Response({
                'data': serializer.data,
                'message': "Blog updated successfully"
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            print("Exception:", e)
            print(traceback.format_exc())  # Print the full traceback
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
            blogs = Blog.objects.filter(user=request.user)

            if request.GET.get('search'):
                search = request.GET.get('search')
                blogs = blogs.filter(
                    Q(title__icontains=search) | 
                    Q(summary__icontains=search) | 
                    Q(user__username__icontains=search)
                )

            # Instantiate the serializer with the request data
            serializer = BlogSerializer(data=blogs, many=True)

            # Validate the serializer
            serializer.is_valid()
            # usernames = [blog['user_username'] for blog in serializer.data]
            unique_usernames = set(blog.user.username for blog in blogs)

                        # usernames = [blog['user_username'] for blog in serializer.data]

            # Convert usernames list to a single string if needed
            usernames_str = ', '.join(unique_usernames)


            return Response({
                'username': usernames_str,
                'data': serializer.data,
                'message': 'Blogs fetched successfully'
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.generics import ListAPIView
# class BlogByTagView(ListAPIView):
#     serializer_class = BlogTSerializer
    
#     def get_queryset(self):
#         tag_name = self.kwargs.get('tag_name')
        
#         if tag_name:
#             blog = Blog.objects.filter(tags__iexact=tag_name)
#             # Filter the queryset based on the tag_name
#             return Response({
#                 'data': blog,
#                 'meessage' : "Blogs fetched successfully"
#             }, status=status.HTTP_200_OK)
#         else:
#             # Return all blogs if no tag_name is provided
#             return Blog.objects.all()
        
        # blogs_data = []
        # for blog in blogs:
        #     search_blog_data = {
        #         "id": blog.uid,
        #         "image": f"{blog.main_image}" if blog.main_image else "",
        #         "title": blog.title,
        #         "post_link": str(blog.uid),
        #         "tag_link": blog.tags,
        #         "tag": blog.tags,
        #         "date": blog.created_at.strftime("%d %B"),  # Format date as needed
        #         "votes": blog.upvotes,  # You may adjust this based on your logic
        #         "user_username": blog.user.username if blog.user else "",
        #     }
        #     blogs_data.append(search_blog_data)
        #     return blogs_data


class BlogByTagView(ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = BlogTSerializer
    
    def get_queryset(self):
        tag_name = self.kwargs.get('tag_name')

        if not tag_name:
            # If tag_name is not provided, return a custom response
            return Blog.objects.none()  # or return an empty queryset

        queryset = Blog.objects.filter(tags__iexact=tag_name)

        # Check if the user is authorized (replace this with your authorization logic)
        # if not self.request.user.is_authorized:
        #     return Blog.objects.none()  # or return an empty queryset

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            # Return a custom response if the queryset is empty
            return Response({
                'data': {},
                'message': 'You are not authorized to do this or the tag name is not provided',
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'data': serializer.data,
            'message': 'Blogs fetched successfully',
        }, status=status.HTTP_200_OK)


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
        

from rest_framework import serializers
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

# class BlogDetailView(APIView):
#     def get(self, request, *args, **kwargs):
#         uid = kwargs.get('uid')
        


#         try:
#             blog = get_object_or_404(Blog, uid=uid)
#             serializer = BlogDSerializer(blog)
            
#             return Response({
#                 'data': serializer.data,
#                 'message': 'Blog fetched successfully'
#             }, status=status.HTTP_200_OK)

#         except Exception as e:
#             print(e)
#             return Response({
#                 'data': [],
#                 'message': 'Something went wrong'
#             }, status=status.HTTP_400_BAD_REQUEST)

#         # blog = Blog.objects.get(uid=uid)
#         # user_serializer = CustomUserSerializer(blog.user)

#         #     # Construct the response in the desired format
#         # response_data = {
#         #     "id": blog.uid,
#         #     "image": f"{blog.main_image}" if blog.main_image else "",
#         #     "title": blog.title,
#         #     "post_link": str(blog.uid),
#         #     "tag_link": blog.tags,
#         #     "tag": blog.tags,
#         #     "date": blog.created_at.strftime("%d %B"),  # Format date as needed
#         #     "votes": 0,  # You may adjust this based on your logic
#         #     "user_username": user_serializer.data['username'],  # Include only the username field
#         # }

#         # return Response(response_data)
        
#     # 
        
#     def post(self, request, *args, **kwargs):
#         uid = kwargs.get('uid')

#         try:
#             blog = get_object_or_404(Blog, uid=uid)
#             user = request.user  # Assuming the user is authenticated

#             # Extract comment data from the request
#             comment_text = request.data.get('text')
#             parent_comment_id = request.data.get('parent_comment_id')

#             # Create a new comment instance
#             comment = Comment.objects.create(user=user, text=comment_text)

#             # If it's a reply, create a new reply instance
#             if parent_comment_id:
#                 parent_comment = get_object_or_404(Comment, uid=parent_comment_id)
#                 reply_text = request.data.get('text')  # Extract reply text
#                 reply = Reply.objects.create(comment=parent_comment, text=reply_text)

#             # Add the comment to the blog's comments
#             blog.comments.add(comment)

#             # Serialize the updated blog
#             serializer = BlogDSerializer(blog)

#             return Response({
#                 'data': serializer.data,
#                 'message': 'Comment posted successfully'
#             }, status=status.HTTP_201_CREATED)

#         except Exception as e:
#             print(e)
#             return Response({
#                 'data': [],
#                 'message': 'Something went wrong'
#             }, status=status.HTTP_400_BAD_REQUEST)
        

from django.contrib.auth import get_user_model


CustomUser = get_user_model()

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

    def post(self, request, *args, **kwargs):
        uid = kwargs.get('uid')

        try:
            blog = get_object_or_404(Blog, uid=uid)
            user = request.user  # Assuming the user is authenticated

            # Extract comment data from the request
            comment_text = request.data.get('add_comment')
            parent_comment_id = request.data.get('parent_comment_id')

            # Create a new comment instance
            comment = Comment.objects.create(user=user, add_comment=comment_text)

            # If it's a reply, create a new reply instance
            if parent_comment_id:
                parent_comment = get_object_or_404(Comment, uid=parent_comment_id)
                reply_text = request.data.get('add_reply')  # Extract reply text
                reply = Reply.objects.create(comment=parent_comment, user=user, add_reply=reply_text)

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
        
from rest_framework import viewsets
from rest_framework.decorators import action


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogDSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # @action(detail=True, methods=['post'])
    # def add_reply(self, request, pk=None):
    #     comment = self.get_object()
        
    #     reply_text = request.data.get('text', '')
    #     user = request.user
    #     reply = Reply.objects.create(comment=comment, text=reply_text)
    #     reply_serializer = ReplySerializer(reply)
    #     return Response({'reply': reply_serializer.data}, status=201)
    @action(detail=True, methods=['post'])
    def add_reply(self, request, pk=None):
        comment = self.get_object()
        reply_text = request.data.get('add_reply', '')

        # Assuming you have access to the user making the reply, you can get it from the request
        user = request.user

        # Create the Reply instance with the user
        reply = Reply.objects.create(comment=comment, user=user, add_reply=reply_text)

        reply_serializer = ReplySerializer(reply)
        return Response({'reply': reply_serializer.data}, status=201)
    


class UpvoteBlogView(APIView):
    def post(self, request, blog_id):
        try:
            blog = Blog.objects.get(uid=blog_id)
            blog.upvotes += 1
            blog.save()
            return Response({'message': 'Upvoted successfully'}, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            return Response({'message': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
        



from .serializers import ContactFormSerializer
from django.core.mail import send_mail


class ContactFormView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            # Process the form data
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']
            user = request.user 

            # Perform actions, e.g., send an email
            send_mail(
                f"New Contact Form Submission from {name}",
                f"From: {name}\nEmail: {email}\nMessage: {message}\nUser: {user}",
                'scharan621@gmail.com',  # Replace with your email
                ['scharan621@gmail.com'],  # Replace with the recipient's email
                fail_silently=False,
            )

            return Response({'message': 'Form submitted successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
        


class UserBlogsView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Fetch user based on the provided username
            username = self.kwargs.get('username')
            user = get_object_or_404(CustomUser, username=username)

            # Fetch blogs related to the user
            blogs = Blog.objects.filter(user=user)

            # If search parameter is provided, apply the filter
            if request.GET.get('search'):
                search = request.GET.get('search')
                search_terms = [term.strip() for term in search.split('$')]

                # Construct a single condition using the logical OR operator
                conditions = Q()
                for term in search_terms:
                    conditions |= Q(title__icontains=term) | Q(user__username__icontains=term) | Q(summary__icontains=term)

                # Apply the constructed condition to filter the queryset
                blogs = blogs.filter(conditions)

            # Construct the response for each blog in the desired format
            blogs_data = []
            usernames = []
            for blog in blogs:
                blog_data = {
                    "id": blog.uid,
                    "image": f"{blog.main_image}" if blog.main_image else "",
                    "title": blog.title,
                    "post_link": str(blog.uid),
                    "tag_link": blog.tags,
                    "tag": blog.tags,
                    "date": blog.created_at.strftime("%d %B %Y %H:%M"),
                    "votes": 0,  # You may adjust this based on your logic
                    "user_username": blog.user.username if blog.user else "",
                }
                blogs_data.append(blog_data)
                usernames.append(blog_data['user_username'])  # Append username to the list


            # Sort the blogs_data by date in descending order
            blogs_data = sorted(blogs_data, key=lambda x: x['date'], reverse=True)
            # usernames = [blog['user_username'] for blog in serializer.data]
                        # usernames = [blog['user_username'] for blog in serializer.data]

            # Convert usernames list to a single string if needed
            usernames_str = ', '.join(usernames)

            # Return the response with all blogs_data
            return Response({
                'username': blog_data['user_username'],
                'data': blogs_data,
                'message': 'Blogs fetched successfully'
            }, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                'data': [],
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
