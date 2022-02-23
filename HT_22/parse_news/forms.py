from django import forms
from .models import Category

from django.db.utils import OperationalError



class SelectCategory(forms.Form):
    selected_cat = forms.ChoiceField(label='')

    def __init__(self, *args, **kwargs):
        super(SelectCategory, self).__init__(*args, **kwargs)
        self.fields['selected_cat'].choices = Category.objects.values_list('cus_cat', 'cus_cat')






