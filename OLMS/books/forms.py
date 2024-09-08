from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publication_date', 'quantity', 'image']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }