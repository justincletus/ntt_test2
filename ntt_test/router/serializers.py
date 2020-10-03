from rest_framework import serializers
from .models import Router

class RouterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Router
        fields = [
            'sap_id',
            'hostname',
            'ip_address',
            'mac_address'
        ]

    # def create(self, validate_data):
    #     router = Router.objects.create(**validate_data)
    #     router.save()
    #     return router
