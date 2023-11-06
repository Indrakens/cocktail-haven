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

    def test_get_add_cocktail_page(self):
        response = self.client.get(reverse('add_cocktail'))
        self.assertEqual(response.status_code, 302)

    def test_edit_cocktail(self):
        response = self.client.get(f'/edit_cocktail/')
        self.assertEqual(response.status_code, 302)

    def test_delete_cocktail(self):
        response = self.client.get(f'/delete_cocktail/')
        self.assertEqual(response.status_code, 302)        
        