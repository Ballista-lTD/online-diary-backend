from django.contrib.auth.models import User, Group

from rest_framework import serializers
from .models import Tokens


# first we define the serializers


class GetTokensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokens
        fields = ['user', 'phone_number', 'access_code', 'avatar', 'roles', 'access_code']
        extra_kwargs = {'user': {'read_only': True}, 'access_code': {'read_only': True}, 'roles': {'read_only': True}}


class UserSerializer(serializers.ModelSerializer):
    tokens = GetTokensSerializer(many=False, read_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', "first_name", "last_name", 'tokens')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)
