from django.db import models
from Organisations.models import Organisations

# Create your models here.
class Projects(models.Model):
    name = models.CharField(unique=True,null=False,max_length=255)
    type = models.CharField(null=True,max_length=255)
    organisation = models.ForeignKey(Organisations,on_delete=models.CASCADE)
    class Meta:
        db_table = 'Projects'


