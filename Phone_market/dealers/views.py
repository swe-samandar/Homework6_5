from django.shortcuts import render

# Create your views here.

def show_dealers(request):
    return render(request, 'dealers.html')