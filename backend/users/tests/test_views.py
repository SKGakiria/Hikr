from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

class UserViewsTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="testpassword"
        )
        self.login_url = reverse("knox_login")
        self.register_url = reverse("user-register")
        self.user_list_url = reverse("user-list")
        self.user_detail_url = reverse("user-detail", args=[self.user.pk])

    # def test_user_registration(self):
    #     """
    #     Test user registration.
    #     """
    #     data = {
    #         "email": "newuser@example.com",
    #         "username": "newuser",
    #         "password": "newpassword"
    #     }
    #     response = self.client.post(self.register_url, data)
    #     # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(User.objects.count(), 2)
    #     self.assertEqual(response.data["username"], "newuser")

    def test_user_login(self):
        """
        Test user login.
        """
        data = {
            "email": "test@example.com",
            "password": "testpassword"
        }
        response = self.client.post(self.login_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    def test_user_list(self):
        """
        Test listing all users.
        """
        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        print(response.data, "///////////////////////////////")
        print(response.data[2], "///////////////////////////////")
        self.assertEqual(response.data["username"], "testuser")

    def test_user_detail(self):
        """
        Test retrieving a user's details.
        """
        response = self.client.get(self.user_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testuser")

    def test_user_update(self):
        """
        Test updating a user's details.
        """
        data = {
            "first_name": "Updated",
            "last_name": "User"
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(self.user_detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "Updated")
        self.assertEqual(self.user.last_name, "User")

    def test_user_delete(self):
        """
        Test deleting a user.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.user_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
