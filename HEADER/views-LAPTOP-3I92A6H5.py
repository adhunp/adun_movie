from django.shortcuts import render,redirect
from HEADER.models import Hlogin
from random import randint
from django.core.mail import send_mail

# Create your views here.

def mnm(request):
    return render (request,'mnm.html')

def hlogin(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']

        try:
            alogin = Hlogin.objects.get(username=username,password=password)
            
            return redirect("HEADER:ahome")
        except:
            msg = "invalid username or password"
            print('niiuwdhiu ')
            return render(request,"hlogin.html",{"error_message":msg})

    return render (request,'hlogin.html')
    

def ahome(request):
    return render (request,'ahome.html')

def up(request):
    return render (request,'upcoming.html')

def theater(request):
    return render (request,'theater.html')

def booking(request):
    return render (request,'booking.html')

def carter(request):
    return render (request,'carter.html')

def seats(request):

    otp = randint(1000, 9999)

    send_mail(
        'no.of seats booked',
         str (otp),
        'adhunp8@gmail.com',
        [userdata.email],
        fail_silently = False,
    )

    return render (request,'seats.html')

def cu_home(request):
    return render (request,'cu_home.html')

def movie_add(request):
    return render (request,'movie_add.html')

