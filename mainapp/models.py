from django.db import models

# Create your models here.

class Lists(models.Model):
    sno = models.AutoField(primary_key=True)
    item = models.CharField(max_length=50)