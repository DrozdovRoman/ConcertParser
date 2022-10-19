from django.shortcuts import render

def home(request):
    return render(request, 'catalog/index.html')
# Create your views here.
