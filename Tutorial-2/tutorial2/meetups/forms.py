from django import forms

from .models import Participant

# class RegistrationForm(forms.ModelForm):

#     # In this class, we defined what the related model should be
#     class Meta:
#         model = Participant

#         # Specify a list of fields that should be included in the form
#         fields = ["email"]


class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your Email')