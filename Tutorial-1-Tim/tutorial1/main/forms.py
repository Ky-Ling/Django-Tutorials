from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(max_length=64, label="Name")
    check = forms.BooleanField()
