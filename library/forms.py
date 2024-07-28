# library/forms.py
from django import forms
from .models import Library, Book, Category, Member


class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['name']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'library']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'library', 'is_available']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'library', 'borrowed_books']
