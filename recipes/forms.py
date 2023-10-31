from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Recipe, Comment 
from django import forms


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'name',
            'slug',
            'user',
            'featured_image',
            'serving',
            'time',
            'description',
            'ingredients',
            'directions'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',) 