from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('recipecreate/', views.RecipeCreate.as_view(), name='recipecreate'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='cocktail_like'),
]