from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class UserModelTestCase(TestCase):

    def test_create_user(self):
        """
        Test creating a new user.
        """
        user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="testpassword"
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("testpassword"))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

    # def test_create_user_invalid_email(self):
    #     """
    #     Test creating a user with an invalid email raises an error.
    #     """
    #     with self.assertRaises(ValidationError):
    #         User.objects.create_user(email=None, username="testuser", password="testpassword")

    # def test_create_user_short_password(self):
    #     """
    #     Test creating a user with a password shorter than 8 characters raises an error.
    #     """
    #     with self.assertRaises(ValidationError):
    #         User.objects.create_user(email="test@example.com", username="testuser", password="short")

    # def test_create_superuser(self):
    #     """
    #     Test creating a superuser.
    #     """
    #     admin_user = User.objects.create_superuser(
    #         email="admin@example.com",
    #         username="adminuser",
    #         password="adminpassword"
    #     )
    #     self.assertEqual(admin_user.email, "admin@example.com")
    #     self.assertEqual(admin_user.username, "adminuser")
    #     self.assertTrue(admin_user.check_password("adminpassword"))
    #     self.assertTrue(admin_user.is_staff)
    #     self.assertTrue(admin_user.is_superuser)
    #     self.assertTrue(admin_user.is_active)

    # def test_create_superuser_not_staff(self):
    #     """
    #     Test creating a superuser without is_staff=True raises an error.
    #     """
    #     with self.assertRaises(ValidationError):
    #         User.objects.create_superuser(
    #             email="admin@example.com",
    #             username="adminuser",
    #             password="adminpassword",
    #             is_staff=False
    #         )

    # def test_create_superuser_not_superuser(self):
    #     """
    #     Test creating a superuser without is_superuser=True raises an error.
    #     """
    #     with self.assertRaises(ValidationError):
    #         User.objects.create_superuser(
    #             email="admin@example.com",
    #             username="adminuser",
    #             password="adminpassword",
    #             is_superuser=False
    #         )
