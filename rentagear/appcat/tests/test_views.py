from django.test import TestCase, Client
from django.urls import reverse
from appcat.models import Gear, Post
import json
class TestViews(TestCase):
    def test_post_list_view (self):
        client=Client()
        response=client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'appcat/home.html')