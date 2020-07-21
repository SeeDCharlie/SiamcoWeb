from django.shortcuts import render

# Create your views here.

def homeLoggin(request):
    return render(request, 'homeLoggin.html') 

