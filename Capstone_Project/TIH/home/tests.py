from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from home.models import Blog, CustomUser  # Replace 'yourapp' with your actual app name

class BlogDetailViewTest(TestCase):
    def setUp(self):
        # Create a CustomUser instance
        self.user = CustomUser.objects.create(
            username="test_user",
            # Add other required fields
        )

        # Create a Blog instance using the CustomUser instance
        self.blog = Blog.objects.create(
            uid="38e66481-421c-47d3-99dc-bd93dbaf1254",
            title="Test Blog",
            blog_text="Hello, this is a test blog",
            main_image="test_image.jpg",
            tags="test",
            user=self.user,  # Set the user field
            created_at="2024-01-29",
            # Add other fields as needed
        )

    def test_blog_detail_view(self):
        # Use Django's reverse function to get the URL for your view, providing the uid
        url = reverse('home:blog-detail', kwargs={'uid': self.blog.uid})
        # Replace 'yourapp' with your actual app name

        # Use Django's test client to simulate a GET request to the view
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Add more specific assertions based on the expected response structure and data
        # For example, check if the response contains the expected keys, data, etc.
        self.assertIn('id', response.data)
        self.assertIn('image', response.data)
        self.assertIn('title', response.data)
        # Add more assertions as needed

    def tearDown(self):
        # Clean up any resources or data created during the test
        pass
