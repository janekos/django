from django.shortcuts import render
from django.forms.formsets import formset_factory

from .forms import CaloriesForm
from .models import Calories

# Create your views here.

def index(request):
    return render(request, 'base.html')

def calories_view(request):
    form_set = formset_factory(CaloriesForm)

    context = {
        'calories_formset': form_set,
        'data': Calories.objects.all()
    }

    return render(request, 'calories.html', context)