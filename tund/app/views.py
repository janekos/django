from django.shortcuts import render
from . import utils
from . import models
# Create your views here.

def index(request):
    return render(request, 'base.html')

def manyToManyTable(request):
    
    utils.save_omanikud(utils.read_from_file("http://www.tlu.ee/~jankos/andmed/omanikud.txt"))
    utils.save_raamatud(utils.read_from_file("http://www.tlu.ee/~jankos/andmed/raamatud.txt"))
    
    omanikud = models.omanikud.objects.all()
    raamatud = models.raamatud.objects.all()
    
    return render(
        request,
        'manyToManyTable.html',
        {
            'title':'manytomany',
            'omanikud': omanikud,
            'raamatud': raamatud,
        }
    )