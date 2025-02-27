from django.shortcuts import render
from .models import Dealer

# Create your views here.

def show_dealers(request):
    dealers = Dealer.objects.all()
    context = {'dealers': dealers}
    return render(request, 'dealers.html', context=context)