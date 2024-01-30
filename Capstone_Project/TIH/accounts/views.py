from django.shortcuts import render
from rest_framework.response import Response

# from accounts.models import CustomUser
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data = data)
            if not serializer.is_valid():
                return Response({
                    'data' : serializer.errors,
                    'message' : 'something went wrong'
                }, status = status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({
                'data' :{},
                'message' : 'your account is created'
            }, status = status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({
                'data' : {},
                'message' : 'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

CustomUser = get_user_model()


class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)

            if serializer.is_valid():
                response = serializer.get_jwt_token(serializer.validated_data)
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong'
                }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': 'Internal Server Error'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def forgot_password(request):
        if request.method == 'POST':
            email = request.POST.get('email', '')
            user = CustomUser.objects.filter(email=email).first()
    
            if user:
                # Generate a unique token and save it to the user model
                token = get_random_string(length=32)
                user.reset_password_token = token
                user.save()
    
                # Send the password reset email with the token
                reset_link = f"http://127.0.0.1:8000/accounts/reset_password/{token}/"
    
                send_mail(
                    'Reset Password',
                    f'Click the following link to reset your password: {reset_link}',
                    settings.DEFAULT_FROM_EMAIL,
                    [user.email],
                    fail_silently=False,
                )
                return Response({'message': 'reset successful'}, status=status.HTTP_200_OK)
    
            else:
                error_message = "No user found with this email address."
                return Response({'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        return Response({'message': 'reset successful'}, status=status.HTTP_200_OK)



# class LogoutView(APIView):
#     def post(self, request):
#         response=Response()
#         response.delete_cookie('sessionid')
#         response.data = {
#             'message' : "success"
#         }
#         return response



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')

            if not refresh_token:
                return Response({'error': 'Refresh token is required.'}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

CustomUser = get_user_model()

class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email', '')
        user = CustomUser.objects.filter(email=email).first()

        if user:
            # Generate a unique token and save it to the user model
            token = get_random_string(length=32)
            user.reset_password_token = token
            user.save()

            # Send the password reset email with the token
            reset_link = f"http://127.0.0.1:8000/accounts/reset_password/{token}/"

            send_mail(
                'Reset Password',
                f'Click the following link to reset your password: {reset_link}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            return Response({'detail': 'Password reset email sent successfully.'}, status=status.HTTP_200_OK)

        else:
            return Response({'error_message': 'No user found with this email address.'}, status=status.HTTP_404_NOT_FOUND)

