from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

from authentication.services.querysets import CustomUserQueryset

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, write_only=True, required=True)
    confirm_password = serializers.CharField(max_length=100, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'confirm_password']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return super().validate(attrs)

    def create(self, validated_data):
        user = CustomUserQueryset.create_user(username=validated_data['username'],
                                              email=validated_data['email'],
                                              password=validated_data['password'])

        return user



# maybe needed
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = ProfileSerializer(self.user).data

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True, max_length=255)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)