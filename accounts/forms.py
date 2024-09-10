from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['full_name', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='برای عوض کردن پسورد  <a href=\"../password/\">کلیک کنید</a>.',
                                         label='رمز عبور')

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password', 'is_active', 'is_admin']


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control m-3 is-invalid', 'placeholder': 'رمز خود را وارد کنید'}))
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control m-3 is-invalid', 'placeholder': 'تکرار رمز عبور'}))

    class Meta:
        model = User
        fields = ['full_name', 'email']

        labels = {
            'full_name': 'نام و نام خانوادگی ',
            'email': 'ایمیل',
        }
        widgets = {
            'full_name': forms.TextInput(
                attrs={'class': 'form-control m-3 is-invalid', 'placeholder': 'نام و نام خانوادگی خود را وارد کنید'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control m-3 is-invalid', 'placeholder': 'ایمیل خود را وارد کنید'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError("ایمیل از قبل وجود دارد!")
        return email

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError("پسوردها یکی نیست دوباره تلاش کنید")
        return self.cleaned_data['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.CharField(max_length=100, widget=forms.EmailInput(
        attrs={'class': 'form-control m-3 is-invalid', 'placeholder': 'ایمیل خودرا وارد کنید'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control m-3 is-invalid', 'placeholder': 'رمز خود را وارد کنید'}))
