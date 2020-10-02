from django import forms
from .models import Router

class RouterForm(forms.Form):
    name = forms.CharField(label="Router Name: ", max_length=100)
    ip_address = forms.IntegerField(label="Ip Address: ")
    
    class Meta:
        model = Router
        fields = [
            'name',
            'ip_address'
        ]
