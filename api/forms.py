from django import forms

class DescriptionForm(forms.Form):
    your_name = forms.CharField(label='HouseDescription', max_length=1000)