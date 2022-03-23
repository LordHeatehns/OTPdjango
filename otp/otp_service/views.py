from asyncio import tasks
from webbrowser import get
from django import views
from django.shortcuts import render ,redirect
from django.views import View
from .tasks import send_email_otp
from django.http import HttpResponse, JsonResponse
from datetime import datetime , timedelta
from rest_framework.views import APIView 
from django.contrib.auth.models import Group, User , auth 
from .models import OTP

# Create your views here.



class OTPS(View):
   
    def get(self ,request):
        return render(request,'login.html')
    def login(self,request):
        return
    def post(self , request):
        print(request.POST['id'])
        print(request.POST['password'])
        username = request.POST['id']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        #login ,เงื่อนไข check ความถูกต้อง ของUser เเละ password
        if user is not None:
            auth.login(request,user)
            print(f"{username} login success")
            return redirect('verify')
        else:
            context = {
                'wrong':"not correct ?"
            }
            return render(request,'login.html',context)
     


        
class VerifyOTP(View):
    def get(self , request):
        return render(request,'verifyOTP.html')
    
    def post(self ,request):
        otp =request.POST.get('otp',None)

        email = request.POST.get('email',None)

        if email is not None :
            print(email)
            print(request.user)
            send_email_otp(email=email,user=request.user)
            return render(request,'verifyOTP.html',{'email':email})
        
        elif otp is not None:
            result = OTP.objects.get(user = request.user , number = otp)
            print(result)

            return render(request,'verifyOTP.html',{'result':result})
        

        
       

    
    