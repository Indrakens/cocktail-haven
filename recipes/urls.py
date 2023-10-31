from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('recipeadd/', views.RecipeAdd.as_view(), name='recipeadd'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='cocktail_like'),
]