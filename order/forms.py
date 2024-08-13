from django import forms


class AddCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=10, label='تعداد')


class OutputForm(forms.Form):
    start_date = forms.DateTimeField(label='از این تاریخ')
    end_date = forms.DateTimeField(label='تا این تاریخ')

