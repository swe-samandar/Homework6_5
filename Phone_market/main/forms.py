from django import forms
from .models import Phone

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'

    def clean_brand(self):
        brand = self.cleaned_data.get('brand')
        if brand == 'nokia':
            raise forms.ValidationError("Nokia telefoni bizning platformamizda sotilmaydi!")
        return brand
        
    def clean_release_date(self):
        release_date = self.cleaned_data.get('release_date')
        if int(release_date[:4]) < 2000:
            raise forms.ValidationError("2000 yildan avval chiqqan telefonlar sotilmaydi!")
        return release_date

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if int(price) > 5000:
            raise forms.ValidationError("$5000.00 qimmat telefonlar sotilmaydi!")
        return price

    def clean_battery_capacity(self):
        battery_capacity = self.cleaned_data.get('battery_capacity')
        if battery_capacity < 3500:
            raise forms.ValidationError("Quvvat hajmi 3500 dan kam bo'lgan telefonlarni sotilmaydi!")
        return battery_capacity
    
    def clean_storage_capacity(self):
        storage_capacity = self.cleaned_data.get('storage_capacity')
        if len(storage_capacity) == 4 and int(storage_capacity[:2]) < 64:
            raise forms.ValidationError("Doimiy xotira hajmi 64GB dan kam bo'lgan telefonlarni sotilmaydi!")
        return storage_capacity