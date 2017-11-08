from django import forms
from .models import Calories

class CaloriesForm(forms.Form):
    food_item = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Toit',
        }),
        required=False
    )
    calories = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Kalorid (100g)'
        }),
        required=False
    )
