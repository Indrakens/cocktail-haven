from django.test import TestCase
from django.shortcuts import reverse
from .models import Recipe


class TestViews(TestCase):

    def test_get_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_recipe_detail_page(self):
        response = self.client.get(reverse('recipe', args=['test']))
        self.assertEqual(response.status_code, 302)

          
        
        