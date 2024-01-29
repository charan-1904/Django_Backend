from datetime import timezone
from django.http import JsonResponse
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser 


class RegisterSerializer(serializers.Serializer):
    # first_name = serializers.CharField()
    # last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    employee_id = serializers.IntegerField()
    email = serializers.CharField()

    def validate(self, data):
        if CustomUser.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError('Username is taken.')
        if CustomUser.objects.filter(employee_id=data["employee_id"]).exists():
            raise serializers.ValidationError('Employee ID is taken.')
        if CustomUser.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError('email ID is taken.')
        
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create(
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name'],
            username=validated_data['username'].lower(),
            employee_id=validated_data['employee_id'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


from django.utils import timezone






class LoginSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()
    password = serializers.CharField()

    # def validate(self, data):
    #     employee_id = data.get('employee_id')
    #     password = data.get('password')

    #     user = CustomUser.objects.filter(employee_id=employee_id).first()

    #     if not user:
    #         raise serializers.ValidationError({'message': 'User not found', 'field_errors': {'employee_id': 'User not found'}})

    #     if not user.check_password(password):
    #         raise serializers.ValidationError({'message': 'Invalid credentials', 'field_errors': {'password': 'Invalid password'}})

    #     return data




    def validate(self, data):
        employee_id = data.get('employee_id')
        password = data.get('password')

        print(f"Attempting login with employee_id: {employee_id}")

        user = CustomUser.objects.filter(employee_id=employee_id).first()

        if not user:
            print(f"User not found for employee_id: {employee_id}")
            raise serializers.ValidationError({'message': 'User not found', 'field_errors': {'employee_id': 'User not found'}})

        if not user.check_password(password):
            print(f"Invalid password for user with employee_id: {employee_id}")
            raise serializers.ValidationError({'message': 'Invalid credentials', 'field_errors': {'password': 'Invalid password'}})

        print(f"Login successful for user with employee_id: {employee_id}")
        return data


    def get_jwt_token(self, data):
        user = CustomUser.objects.filter(employee_id=data['employee_id']).first()

        if not user:
            return {'message': 'User not found', 'data': {}}

        # refresh = RefreshToken.for_user(user)

        # return {
        #     'message': 'Login success',
        #     'data': {'token': {'refresh': str(refresh), 'access': str(refresh.access_token)}}
        # }

        access_token = RefreshToken.for_user(user).access_token
        expires_at = timezone.now() + timezone.timedelta(seconds=3600)
        return {
            "message": "Login success",
            "data": {
                "token": {
                    "access": str(access_token),  # Convert to string
                    "expires_at": expires_at.timestamp(),  # Include expiration timestamp
                }
            }
        }
        # return JsonResponse(response_data)





