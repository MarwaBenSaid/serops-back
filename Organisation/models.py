from django.db import models

# Create your models here.
class Organisation(models.Model):
    name = models.CharField(unique=True,null=False,max_length=255)
    website = models.URLField(null=True,max_length=255)
    class Meta:
        db_table = 'organisations'
