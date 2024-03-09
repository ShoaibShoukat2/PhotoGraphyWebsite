from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name="index-page"),
    path('signup/',signup,name="signup-page"),
    path('login/',login,name="login-page"),
    path('about/',about,name="about-page"),
    path('services/',services,name="services-page"),
    path('blog/',blog,name="blog-page"),
    path('media/',media,name="media-page"),
    path('cart/',cart,name="cart-page"),
    path('call-booking/',Call_Booking,name="callbooking-page"),
    path('3D/',D3Page,name="3DPage-page"),
    path('code/',Code,name="code-page")
]