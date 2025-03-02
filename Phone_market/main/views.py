from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone
from .forms import PhoneForm

# Create your views here.

def main(request):
    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, 'main.html', context=context)

def phone_detail(request, pk):
    phone = Phone.objects.get(id=pk)
    context = {'phone': phone}
    return render(request, 'phone/phone_detail.html', context=context)

def phone_create(request):
    if request.method == 'POST':
        phone = Phone()
        phone.brand = request.POST.get('brand', '')
        phone.model = request.POST.get('model', '')
        phone.color = request.POST.get('color', '')
        phone.storage_capacity = request.POST.get('storage_capacity', '')
        phone.price = request.POST.get('price', 0)
        phone.release_date = request.POST.get('release_date', '')
        phone.screen_size = request.POST.get('screen_size', '')
        phone.battery_capacity = request.POST.get('battery_capacity', 0)
        phone.processor = request.POST.get('processor', '')
        phone.camera_resolution = request.POST.get('camera_resolution', '')
        phone.processor = request.POST.get('processor', '')
        phone.image = request.FILES.get('image', '')
        phone.save()

        # brand = request.POST['brand']
        # model = request.POST['model']
        # color = request.POST['color']
        # storage_capacity = request.POST['storage_capacity']
        # price = request.POST['price']
        # release_date = request.POST['release_date']
        # screen_size = request.POST['screen_size']
        # battery_capacity = request.POST['battery_capacity']
        # processor = request.POST['processor']
        # camera_resolution = request.POST['camera_resolution']
        # processor = request.POST['processor']
        # image = request.FILES['image']

        # Phone.objects.create(
        #     brand=brand,
        #     model=model,
        #     color=color,
        #     storage_capacity=storage_capacity,
        #     price=price,
        #     release_date=release_date,
        #     screen_size=screen_size,
        #     battery_capacity=battery_capacity,
        #     camera_resolution=camera_resolution,
        #     processor=processor,
        #     image=image
        # )
        return redirect('main')
    return render(request, 'phone/phone_create.html', {'phone': 'phone'})


def phone_update(request, pk):
    phone = Phone.objects.get(id=pk)
    if request.method == 'POST':
        phone.brand = request.POST.get('brand', phone.brand)
        phone.model = request.POST.get('model', phone.model)
        phone.color = request.POST.get('color', phone.color)
        phone.storage_capacity = request.POST.get('storage_capacity', phone.storage_capacity)
        phone.price = request.POST.get('price',phone.price)
        phone.release_date = request.POST.get('release_date', phone.release_date)
        phone.screen_size = request.POST.get('screen_size', phone.screen_size)
        phone.battery_capacity = request.POST.get('battery_capacity', phone.battery_capacity)
        phone.processor = request.POST.get('processor', phone.processor)
        phone.camera_resolution = request.POST.get('camera_resolution', phone.camera_resolution)
        phone.processor = request.POST.get('processor', phone.processor)
        phone.image = request.FILES.get('image', phone.image)
        phone.save()
        return redirect('phone-detail', pk=pk)
    return render(request, 'phone/phone_update.html', {'phone': phone})


def phone_delete(request, pk):
    phone = get_object_or_404(Phone, id=pk)

    if request.method == "POST":
        phone.delete()
        return redirect('main')
    return render(request, 'phone/phone_delete.html', {'phone': phone})


def phone_create_form(request):
    form = PhoneForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('main')
    return render(request, "phone/phone_create_form.html", {"form": form})


def phone_update_form(request, pk):
    phone = get_object_or_404(Phone, id=pk)
    if request.method == 'POST':
        form = PhoneForm(request.POST or None, request.FILES, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('phone-detail', pk)
    else:
        form = PhoneForm(instance=phone)
    return render(request, 'phone/phone_update_form.html', {'form': form, 'phone': phone})