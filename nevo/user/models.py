from django.db import models

# Create your models here yes here is the model which we have created so far.


class UserDetail(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=200,blank=False, default='',unique=True)
    user_name = models.CharField(max_length=200,blank=False, default='',unique=True)
    password = models.CharField(max_length=100,blank=False,default='')
    gender = models.CharField(max_length=10,blank=False,default='')
    date_of_birth = models.DateField(auto_now=False,blank=False,default='')
    
