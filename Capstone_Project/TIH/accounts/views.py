from django.shortcuts import render
from rest_framework.response import Response
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
            return Response({
                'data' : {},
                'message' : 'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)




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
