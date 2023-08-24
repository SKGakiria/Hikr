from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, username, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        if not username:
            raise ValueError(_("The Username must be set"))
        user = self.model(email=email, username=username, **extra_fields)

        if not password:
            raise ValueError(_("The Password must be set"))
        if len(password) < 8:
            raise ValueError(_("The Password must be at least 8 characters long."))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, username, password, **extra_fields)


class User(AbstractUser):
    """
    Define a custom User model. Set `USERNAME_FIELD` to `email` and `REQUIRED_FIELDS` to `username` and `password`.

    attributes:
        email (str): The email of the user. Must be unique.
        username (str): The username of the user. Must be unique.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        location (str): The location of the user.
        avatar (ImageField): The avatar of the user.
    """
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=100, editable=False)
    first_name = models.CharField(max_length=40, blank=True, default="")
    last_name = models.CharField(max_length=40, blank=True, default="")
    location = models.CharField(max_length=100, blank=True, default="")
    avatar = ResizedImageField(
        size=[370, 259],
        default="users/avatars/default.png",
        upload_to="users/avatars",
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]

    class Meta:
        db_table = "users"
        verbose_name_plural = "Users"

    def __str__(self):
        """
        Returns a string representation of `User`.
        """
        return f"{self.username}: {self.email}"