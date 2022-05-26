from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime
import json

from .permissions import *


class OwnersViewSet:
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def list(self, request):
        queryset = self.queryset.filter(user=request.user)
        context = {
            'request': request,
        }
        serializer = self.serializer_class(queryset, many=True, context=context)
        return Response(serializer.data)

    def create(self, request):
        validated_data = request.data
        response = []
        if type(validated_data).__name__ == 'QueryDict':
            validated_data = json.loads([key for key in validated_data.keys()][0])

        if type(validated_data).__name__ == 'list':
            for data in validated_data:
                instance = self.model(**data)
                self.create_processor(request, instance)
                instance.created_at = datetime.now()
                instance.updated_at = datetime.now()
                instance.save()
                response.append(self.serializer_class(instance, context={'request': request}).data)

        elif type(validated_data).__name__ == 'dict':
            instance = self.model(**validated_data)
            self.create_processor(request, instance)
            instance.created_at = datetime.now()
            instance.updated_at = datetime.now()
            instance.save()
            response.append(self.serializer_class(instance, context={'request': request}).data)

        return Response(response)

    def create_processor(self, request, instance):
        pass

    @action(detail=False, permission_classes=permission_classes, methods=['post'], url_path='update')
    def multiple_update(self, request, pk=None):
        validated_data = request.data
        response = []
        if type(validated_data).__name__ == 'QueryDict':
            validated_data = json.loads([key for key in validated_data.keys()][0])

        for data in validated_data:
            instance = self.queryset.filter(user=request.user, id=data['id']).first()
            if instance is not None:
                for attr, value in data.items():
                    setattr(instance, attr, value)
                self.update_processor(request, instance)
                instance.save()
                response.append(self.serializer_class(instance, context={'request': request}).data)
        return Response(response)

    def update(self, request, pk):
        validated_data = request.data
        instance = self.queryset.filter(user=request.user, id=pk).first()
        response = {}
        if type(validated_data).__name__ == 'QueryDict':
            validated_data = json.loads([key for key in validated_data.keys()][0])

        if instance is None:
            response['status'] = 'failed'
        else:
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            self.update_processor(request, instance)
            instance.save()
            response = validated_data
        return Response(response)

    def update_processor(self, request, instance):
        pass

    @action(detail=False, permission_classes=permission_classes, methods=['post'], url_path='delete')
    def multiple_delete(self, request, pk=None):
        validated_data = request.data
        response = []
        if type(validated_data).__name__ == 'QueryDict':
            validated_data = json.loads([key for key in validated_data.keys()][0])

        for data in validated_data:
            instance = self.queryset.filter(user=request.user, id=data['id']).first()
            if instance is not None:
                self.delete_processor(request, instance)
                instance.delete()
        return Response(response)

    def destroy(self, request, pk):
        instance = self.queryset.filter(user=request.user, id=pk).first()
        if instance is not None:
            self.delete_processor(request, instance)
            instance.delete()
        return Response()

    def delete_processor(self, request, instance):
        pass
