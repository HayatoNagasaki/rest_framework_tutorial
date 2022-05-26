from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:group-detail")

    class Meta:
        model = Group
        fields = ['url', 'name']


class TestModelSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.IntegerField(source='user.id')

    class Meta:
        model = TestModel
        fields = ['id', 'user_id', 'number']

    def create(self, validated_data):
        return TestModel(**validated_data)
