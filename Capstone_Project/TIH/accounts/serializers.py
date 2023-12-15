from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        if User.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError('Username is taken.')
        return data

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'].lower()  # Use lower() to ensure case-insensitive uniqueness
        )
        user.set_password(validated_data['password'])
        user.save()  # Save the user object to persist changes
        return user


from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'message': 'User not found', 'field_errors': {'username': 'User not found'}})

        return data

    def get_jwt_token(self, data):
        user = authenticate(username=data['username'], password=data['password'])

        if not user:
            return {'message': 'Invalid credentials', 'data': {}}

        refresh = RefreshToken.for_user(user)

        return {
            'message': 'Login success',
            'data': {'token': {'refresh': str(refresh), 'access': str(refresh.access_token)}}
        }



# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         if not User.objects.filter(username=data['username']).exists():
#             raise serializers.ValidationError('account not found')
#         return data

#     def get_jwt_token(self, data):
#         user = authenticate(username=data['username'], password=data['password'])

#         if not user:
#             return {'message': 'invalid credentials', 'data': {}}
#         refresh = RefreshToken.for_user(user)

#         return {'message': 'login success',
#                 'data': {'token': {'refresh': str(refresh), 'access': str(refresh.access_token), }}}



