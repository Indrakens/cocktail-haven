from django.test import TestCase
from django.urls import reverse, resolve
from .views import (RecipeList, RecipeCreate, RecipeUpdate, RecipeDelete, RecipeDetail, RecipeLike)


class TestUrls(TestCase):

    def test_home_url_resolves(self):
        """
        Redirects to home page
        """
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, RecipeList)

    def test_add_cocktail_url_resolves(self):
        """
        Redirects to add-cocktail-form page
        """
        url = reverse('add_cocktail')
        self.assertEqual(resolve(url).func.view_class, RecipeCreate)

    def test_edit_cocktail_url_resolves(self):
        """
        Redirects to add-cocktail-form page
        """
        url = reverse('edit_cocktail', args=['slug'])
        self.assertEqual(resolve(url).func.view_class, RecipeUpdate) 

    def test_delete_cocktail_url_resolves(self):
        """
        Redirects to 403 page
        """
        url = reverse('delete_cocktail', args=['slug'])
        self.assertEqual(resolve(url).func.view_class, RecipeDelete)

    def test_recipe_detail_url_resolves(self):
        """
        Redirects to recipe page
        """
        url = reverse('recipe', args=['slug'])
        self.assertEqual(resolve(url).func.view_class, RecipeDetail) 

    def test_recipe_like_url_resolves(self):
        """
        Redirects to recipe page
        """
        url = reverse('cocktail_like', args=['slug'])
        self.assertEqual(resolve(url).func.view_class, RecipeLike)                  