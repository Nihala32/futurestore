from django import forms
from bookapp.models import Books



class BookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=["bookname","author","price","qty","publisher"]
        widgets = {
            "bookname": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "qty": forms.NumberInput(attrs={"class": "form-control"}),
            "publisher": forms.TextInput(attrs={"class": "form-control"})
        }
class BookEditForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=["bookname","author","price","qty","publisher"]