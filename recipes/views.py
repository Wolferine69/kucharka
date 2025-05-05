from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Recipe
from .forms import NoteForm  # Import formuláře


def home(request):
    categories = Category.objects.all()
    return render(request, 'recipes/home.html', {'categories': categories})


def category_recipes(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    recipes = category.recipes.all()
    return render(request, 'recipes/category_recipes.html', {'category': category, 'recipes': recipes})


def recipe_detail(request, category_slug, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, categories__slug=category_slug)

    # Zpracování formuláře pro přidání poznámky
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)  # Vytvoří objekt, ale ještě neuloží
            note.recipe = recipe  # Nastaví vazbu na recept
            note.save()  # Uloží poznámku
            return redirect('recipe_detail', category_slug=category_slug, recipe_id=recipe_id)  # Znovu načte stránku
    else:
        form = NoteForm()  # Prázdný formulář pro GET požadavek

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'category_slug': category_slug,
        'form': form  # Předáme formulář do šablony
    })