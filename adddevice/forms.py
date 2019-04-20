from django import forms
from . import models

class AddNewDevice(forms.ModelForm):
    class Meta:
        model = models.AddDevice
        fields = ['ip']
