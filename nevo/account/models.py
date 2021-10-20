from codecs import backslashreplace_errors
from django.contrib.auth import base_user
from django.db import  models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class manager(BaseUserManager):
	def create_user(self, email,name,username,gender,password=None,is_active=True,is_staff=False,is_admin=True):
		if not email:
			raise ValueError("user must have an email address")
		if not password:
			raise ValueError("user must have an password")
		user_obj = self.model(email = self.normalize_email(email))
		user_obj.set_password(password)
		user_obj.name = name
		user_obj.gender = gender
		user_obj.username = username
		user_obj.staff = is_staff
		user_obj.active = is_active
		user_obj.admin = is_admin 
		user_obj.save(using = self.db)
		return user_obj
	
	def create_staffuser(self,email,name,username,gender,password=None):
		user_obj = self.create_user(email,name,username,gender,password=password,is_staff=True)
		return user_obj


	def create_superuser(self,email,name,username,gender,password=None):
		user_obj = self.create_user(email,name,username,gender,password=password,is_staff=True,is_admin=True)
		return user_obj

class AccountUser(AbstractBaseUser):
	email = models.EmailField(max_length=250,unique=True)
	name = models.CharField(max_length=200,unique=False,default='')
	username = models.CharField(max_length=200,unique=True,default='')
	active =  models.BooleanField(default=True)
	staff = models.BooleanField(default=False) # staff user non-superuser
	admin = models.BooleanField(default=False) #superuser
	gender = models.CharField(max_length=200,unique=False)
	date_joined = models.DateTimeField(auto_now_add=True,blank=True,null=True)
	last_login = models.DateTimeField(auto_now=True,blank=True,null=True)
	manager = manager()


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name','password','username','gender']

	def __str__(self):
		return self.email 
	@property
	def is_staff(self):
		return self.staff
	@property
	def is_active(self):
		return self.active
	@property
	def is_admin(self):
		return self.admin
