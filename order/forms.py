from django import forms
from django.core.exceptions import ValidationError


class AddCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10, label='تعداد')


class OutputForm(forms.Form):
    start_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label='از این تاریخ')
    end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}), label='تا این تاریخ')


class AddAddressForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'شماره تلفن خود را وارد کنید'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'آدرس خود را وارد کنید'}))

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) > 11:
            raise ValidationError("شماره تلفن باید کمتر از ۱۱ عدد باشد")
        return phone


class AddPeygiriCode(forms.Form):
    code = forms.CharField(label='کد',
                           widget=forms.TextInput(attrs={'class': 'form-control m-3 is-invalid',
                                                         'placeholder': 'کد پیگیری خود را وارد کنید'}))
