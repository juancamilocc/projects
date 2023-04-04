from django.db import models

class tasksdb(models.Model):
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)

# Create your models here.
