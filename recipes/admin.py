from django.contrib import admin
from .models import Category, Recipe, RecipeIngredient, Note

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class NoteInline(admin.TabularInline):
    model = Note
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    filter_horizontal = ('categories',)
    inlines = [RecipeIngredientInline, NoteInline]

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'text')