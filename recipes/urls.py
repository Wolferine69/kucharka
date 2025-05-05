from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>/', views.category_recipes, name='category_recipes'),
    path('category/<slug:category_slug>/recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]