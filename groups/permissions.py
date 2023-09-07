from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    
    Source: https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#object-level-permissions
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the owner of the object.
        # Asssumes that the model instance has an `owner` attribute.
        return obj.owner == request.user