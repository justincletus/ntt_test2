from django import forms
from .models import Router

class RouterForm(forms.Form):
    sap_id = forms.IntegerField(label="Router Name: ")
    hostname = forms.CharField(label="Hostname: ")
    ip_address = forms.CharField(label="IP Address: ")
    mac_address = forms.CharField(label="Mac Address: ")
    
    class Meta:
        model = Router
        fields = [
            'sap_id',
            'hostname',
            'ip_address',
            'mac_address'
        ]
