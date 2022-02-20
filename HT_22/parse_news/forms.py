from django import forms
from .models import Category


category_list = [(i, i) for i in Category.objects.all()]

class SelectCategory(forms.Form):
    selected_cat = forms.CharField(label="", max_length=20, widget=forms.Select(choices=category_list))


