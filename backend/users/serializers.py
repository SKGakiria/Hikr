from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    """
    Define a UserSerializer class.
    Inherits from ModelSerializer.

    attributes:
        model (User): Model to serialize.
        fields (list): The fields to include in the serializer.
    """

    class Meta:
        model = User
        fields = ["id", "email", "username", "first_name", "last_name", "location", "avatar"]