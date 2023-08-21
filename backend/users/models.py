from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
# from django.urls import reverse
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
        user = self.model(email=email, username=username, **extra_fields)
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
    """
    email = models.EmailField(max_length=255, unique=True)
    location = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=100, editable=False)
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

    # def get_absolute_url(self):
    #     return reverse("user", args=[self.username])

    def email_exists(self):
        """
        Check if email exists in database. Returns True if exists, False otherwise.
        """
        return User.objects.filter(email=self.email).exists()

    def username_exists(self):
        """
        Check if username exists in database. Returns True if exists, False otherwise.
        """
        return User.objects.filter(username=self.username).exists()