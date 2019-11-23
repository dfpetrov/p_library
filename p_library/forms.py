from django import forms
from .models import Author, Book, BookRent, Friend
from django.forms import formset_factory

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):  
    class Meta:  
        model = Book  
        fields = '__all__'

class BookRentForm(forms.ModelForm):  
    class Meta:  
        model = BookRent
        fields = '__all__'

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = '__all__'