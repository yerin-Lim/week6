from rest_framework import permissions

class IsAuthorOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
        

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'DELETE':
            return request.user.is_superuser
            
        if request.method == 'PUT':
            return obj.author == request.user