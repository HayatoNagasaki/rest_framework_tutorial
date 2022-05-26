from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, model_obj):
        return model_obj.user.id == request.user.id
