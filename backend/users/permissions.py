from rest_framework import permissions

class IsSelfOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow users to edit their own details.
    
    Source: https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to user themselves.
        return obj == request.user