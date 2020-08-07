from django import forms


class UrlDataForm(forms.Form):
    url = forms.CharField(label='Url', max_length=500)
