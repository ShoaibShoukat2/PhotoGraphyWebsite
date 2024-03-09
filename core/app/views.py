from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')


def signup(request):
    return render(request,'signup.html')


def login(request):
    return render(request,'login.html')



def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')


def blog(request):
    return render(request,'blog.html')


def media(request):
    return render(request,'media.html')




def cart(request):
    return render(request,'cart.html')



def Call_Booking(request):
    return render(request,'call.html')

def D3Page(request):
    return render(request,'3D.html')



def Code(request):
    return render(request,'Code.html')