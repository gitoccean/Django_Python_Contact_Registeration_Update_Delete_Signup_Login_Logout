from django.db import models

# Create your models here.


class SignupModel(models.Model):
    Name=      models.CharField(max_length=20,null=False)
    Email=     models.EmailField(null=False)
    Username=  models.CharField(max_length=30,null=False)
    Password=  models.CharField(max_length=30,null=False)
    Confirm_Password= models.CharField(max_length=30,null=False)

   

class SigninModel(models.Model):
       Username= models.CharField(max_length=30,null=False)
       Password= models.CharField(null=False,max_length=30)
       


class RegisterModel(models.Model):
      name  = models.CharField(max_length=30,null=False)
      email = models.EmailField(null=False)
      phone = models.IntegerField(null=False)
      city  = models.CharField(max_length=30,null=False)
      province=models.CharField(max_length=30,null=False)
      country=models.CharField(max_length=30,null=False)
