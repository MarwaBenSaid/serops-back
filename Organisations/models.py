from django.db import models

# Create your models here.
class Orgnisation(models.Model):
    name = models.CharField(unique=True,null=False,max_length=255)
    website = models.CharField(null=True,max_length=255)
    class Meta:
        db_table = 'orgnisations'
