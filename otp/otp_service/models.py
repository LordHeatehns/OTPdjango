from django.db import models
from django.contrib.auth.models import  User

# Create your models here.




class OTP(models.Model):
    user = models.OneToOneField(User , blank=True, null= True , on_delete=models.CASCADE)
    number =  models.CharField(max_length=4 , blank=True, null=True)
    correct = models.BooleanField(default=False)




