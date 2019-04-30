from django import forms
from . import models

class AddNewDevice(forms.ModelForm):
    ip = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'placeholder': 'Enter Ip address'
                }
            )
        )
    
    class Meta:
        model = models.AddDevice
        fields = ['ip']
        
    