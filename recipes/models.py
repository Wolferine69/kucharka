from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)  # Název kategorie, např. "Do pekárny"
    slug = models.SlugField(unique=True)  # Pro URL, např. "do-pekarni"

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='recipe_ingredients')  # Vazba na recept
    name = models.CharField(max_length=100)  # Název ingredience, např. "Mouka"
    quantity = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Množství, např. 500 nebo 1
    unit = models.CharField(max_length=50, blank=True, null=True)  # Jednotka, např. "g", "hrnek"

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.name}"

class Recipe(models.Model):
    title = models.CharField(max_length=200)  # Název receptu
    categories = models.ManyToManyField(Category, related_name='recipes')  # Více kategorií
    instructions = models.TextField()  # Postup přípravy
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)  # Obrázek receptu
    created_at = models.DateTimeField(auto_now_add=True)  # Datum vytvoření

    def __str__(self):
        return self.title

class Note(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='notes')  # Vazba na recept
    text = models.TextField()  # Text poznámky

    def __str__(self):
        return f"Poznámka k {self.recipe}"