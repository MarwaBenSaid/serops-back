from django.db import models


# Create your models here.
class Servers(models.Model):
    name = models.CharField(unique=False,null=False,max_length=255)
    ip = models.CharField(null=True,max_length=255)
    key = models.CharField(null=True,max_length=255)
    password = models.CharField(null=True,max_length=255)
    class Meta:
        db_table = 'Servers'
