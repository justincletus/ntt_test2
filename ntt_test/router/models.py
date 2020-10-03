from django.db import models
from django.urls import reverse

class Router(models.Model):
    sap_id = models.IntegerField(default=1)
    hostname = models.CharField(max_length=100, default=None, null=True, blank=True)
    ip_address = models.CharField(max_length=100, default=None, null=True, blank=True)
    mac_address = models.CharField(max_length=100, default=None, null=True, blank=True)


    def get_absolute_url(self):
        return reverse("router:router-detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.sap_id