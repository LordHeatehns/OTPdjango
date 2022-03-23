
from celery import  shared_task
import random
from django.core.mail import send_mail ,EmailMessage
from .models import OTP

@shared_task(bind =True)
def generated_otp(self):
    num = random.randint(1000,9999)
    return num

@shared_task(bind= True)
def send_email_otp(self , email ,user):
       otp = generated_otp()
       OTP.objects.filter(user = user).update(
           number =  otp
       )
       send_mail(
           "OTP",
           "Yournumber",
           f'otp = {otp}',
           [email]
       )
       



