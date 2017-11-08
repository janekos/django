from django.shortcuts import render
from django.forms.formsets import formset_factory

from .forms import CaloriesForm
from .models import Calories

# Create your views here.

def index(request):
    return render(request, 'base.html')

def calories_view(request):
    form_set = formset_factory(CaloriesForm)

    if request.method == 'POST' and 'submit_items' in request.POST:
        calories_formset = form_set(request.POST)
        if calories_formset.is_valid():
            data = []
            for form in calories_formset:
                food_item = form.cleaned_data.get('food_item')
                calories = form.cleaned_data.get('calories')
                if food_item and calories 

    context = {
        'calories_formset': form_set,
        'data': Calories.objects.all()
    }

    return render(request, 'calories.html', context)