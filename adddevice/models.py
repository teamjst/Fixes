from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AddDevice(models.Model):
    ip = models.GenericIPAddressField(protocol='both')
    #owner = models.ForeignKey(User, default=None)

    def __str__(self):
        return self.ip
