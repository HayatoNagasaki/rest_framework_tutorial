from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class MyModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyModel
        fields = ['id', 'number']


class MyModelCreateSerializer(serializers.HyperlinkedModelSerializer):
    models = serializers.ListField()

    def update(self):
        pass

    def create(self):
        pass