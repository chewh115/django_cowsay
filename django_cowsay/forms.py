from django import forms

class CowSayForm(forms.Form):
    text = forms.CharField(max_length=50, initial="")