from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add_cocktail/', views.RecipeCreate.as_view(), name='add_cocktail'),
    path('edit_cocktail/<slug:slug>', views.RecipeUpdate.as_view(), name='edit_cocktail'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='cocktail_like'),
]