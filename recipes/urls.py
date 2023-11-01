from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe'),
    path('add_recipe/', views.RecipeAdd, name='add_recipe'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='cocktail_like'),
]