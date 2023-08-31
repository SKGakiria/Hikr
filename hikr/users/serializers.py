from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework.validators import UniqueValidator
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Define a UserSerializer class.
    Inherits from ModelSerializer.

    attributes:
        model (User): Model to serialize.
        fields (list): The fields to include in the serializer.
    """

    class Meta:
        model = User
        fields = ["url", "id", "email", "username", "first_name", "last_name", "location", "avatar"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Define a UserRegistrationSerializer class.
    Inherits from ModelSerializer.
    """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    
    class Meta:
        model = User
        fields = ["email", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        user = User.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class CustomAuthTokenSerializer(serializers.Serializer):
    """
    Custom authentication token serializer.
    Basically a simple altered versoin of the default AuthTokenSerializer.
    Allows login only through email.
    """
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Invalid Credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs