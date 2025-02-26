from django.shortcuts import render
from .models import Phone

# Create your views here.

def main(request):
    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, 'main.html', context=context)

def phone_detail(request, pk):
    phone = Phone.objects.get(id=pk)
    context = {'phone': phone}
    return render(request, 'phone_detail.html', context=context)