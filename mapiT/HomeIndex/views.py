from django.shortcuts import render

# Create your views here.

def indexHomePageRender(request): 
    context = {}
    return render(request, 'HomePage.html', context)