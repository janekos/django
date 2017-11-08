from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'base.html')

def manyToManyTable(request):
    
    return render(
        request,
        'app/manyToManyTable.html',
        {
            'title':'manytomany'
        }
    )