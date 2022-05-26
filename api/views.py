from django.contrib.auth.models import User, Group
from django.utils.decorators import method_decorator
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, StreamingHttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import *
from .serializers import *
from .models import *
from .viewsets import *


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, permission_classes=permission_classes, methods=['get'], url_path='multiple-create')
    def add_model(self, request, pk=None):
        return Response({"status": "success"})

    @action(detail=False, permission_classes=permission_classes, methods=['get'], url_path='play')
    def just_play(self, request, pk=None):
        return Response({'status': 'just play success!'})


class TestModelViewSet(OwnersViewSet, viewsets.ModelViewSet):
    model = TestModel
    queryset = model.objects.all()
    serializer_class = TestModelSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
