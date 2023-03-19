from django.db import models
from django.contrib.auth.models import AbstractUser
from Organisation.models import Organisation
from model_utils import Choices

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = None
    email = models.CharField(unique=True,max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(unique=True,null=True,blank=True,max_length=255)
    STATUS = Choices('active', 'suspended')
    status = models.CharField(choices=STATUS,null=False,default=STATUS.active,max_length=255)
    ROLE = Choices('admin','devops','developer')
    role = models.CharField(choices=ROLE,default=ROLE.admin,max_length=255)
    organisation = models.ForeignKey(Organisation,on_delete=models.CASCADE)
    class Meta:
        db_table = 'users'

    # Setting username by default equal to email
    USERNAME_FIELD = 'email'
    
    
    # Setting Required Field for User
    REQUIRED_FIELDS = [
        first_name,
        last_name,
        email,
        password
        ]
