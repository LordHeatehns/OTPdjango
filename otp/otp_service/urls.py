from django.urls import path , include
from . import views
urlpatterns = [
   
    path('',views.OTPS.as_view(), name = "login"),
    path('api/',views.VerifyOTP.as_view(), name = "verify")
]
