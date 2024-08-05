from django import forms


class AddCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10, label='تعداد')

