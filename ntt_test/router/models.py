from django.db import models
from django.urls import reverse

class Router(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.IntegerField(default=None, null=True, blank=True)


    def get_absolute_url(self):
        return reverse("router:router-detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.name