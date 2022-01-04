from django.db import models

# Create your models here.

class Phone(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    serial_no = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    