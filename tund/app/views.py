from django.shortcuts import render
from django.forms.formsets import formset_factory
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse

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
                if food_item and calories and no_duplicates(data, food_item):
                    object = Calories(food_item=food_item, calories=calories)
                    try:
                        entry = Calories.objects.get(food_item=food_item)
                    except ObjectDoesNotExist:
                        data.append(object)
                    else:
                        entry.calories = calories
                        entry.save()
            Calories.objects.bulk_create(data)
            return HttpResponseRedirect(reverse('calories'))
    context = {
        'calories_formset': form_set,
        'data': Calories.objects.all()
    }

    return render(request, 'calories.html', context)

def no_duplicates(data, food_item):
    for item in data:
        if item.food_item == food_item:
            return False
    return True
