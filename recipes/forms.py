from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']  # Pouze pole 'text', protože 'recipe' nastavíme ve view
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Zadejte poznámku...'}),
        }
        labels = {
            'text': 'Poznámka',
        }