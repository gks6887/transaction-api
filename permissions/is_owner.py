from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if obj.__class__.__name__ == "User":
            return request.user.id == obj.id
        return  request.user.id == obj.user.id