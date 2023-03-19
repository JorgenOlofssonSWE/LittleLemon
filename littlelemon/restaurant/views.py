from django.shortcuts import render

# Create your views here.

def index(request):
    print ('in views indec')
    return render(request, 'index.html', {})