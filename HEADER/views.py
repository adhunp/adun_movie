from django.shortcuts import render,redirect
from HEADER.models import Hlogin
from USER.models import Userdetails
from random import randint
from django.core.mail import send_mail
from towner.models import Moviedetails,Tdetails

# Create your views here.



def hlogin(request):
    msg=""
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']

        try:
            alogin = Hlogin.objects.get(username=username,password=password)
            request.session['a_id'] = alogin.id
            return redirect("HEADER:ahome")
        except:
            msg = "invalid username or password"
            print('niiuwdhiu ')
            return render(request,"hlogin.html",{"error_message":msg})

    return render (request,'hlogin.html')
    

def ahome(request):
    details=Moviedetails.objects.all()
    admin= Hlogin.objects.get(id=request.session['a_id'])
    return render (request,'ahome.html',{'det':details,'admin':admin.username})


def up(request):
    admin= Hlogin.objects.get(id=request.session['a_id'])
    return render (request,'upcoming.html',{'admin':admin})

def theater(request):
    admin= Hlogin.objects.get(id=request.session['a_id'])
    return render (request,'theater.html',{'admin':admin})

def booking(request,m_id):
    details=Moviedetails.objects.get(id=m_id)
    admin= Hlogin.objects.get(id=request.session['a_id'])
    return render (request,'booking.html',{'admin':admin,'movie':details})

def carter(request,m_id):
    details=Moviedetails.objects.get(id=m_id)
    # theater_details=Tdetails.objects.all()
    # admin= Hlogin.objects.get(id=request.session['a_id'])
    return render (request,'carter.html',{'movie':details})

def seats(request):
    admin= Hlogin.objects.get(id=request.session['a_id'])
    
    if request.method == 'POST':
        no_seats=request.POST['count']   
        obj1=  Userdetails.objects.get(id = request.session['c_id'])
        email= obj1.uemail
        msg= str(no_seats)+"seats are booked"
        
        send_mail(
            'no.of seats booked',
               msg ,
            'adhunp8@gmail.com',           
            [email,],
            fail_silently = False,
        )

    return render (request,'seats.html',{'admin':admin})

def c_psw(request):
    admin= Hlogin.objects.get(id=request.session['a_id'])
    msg = ""
    if request.method == 'POST':
        # admin = Hlogin.objects.get(id = 1)
        admin = Hlogin.objects.get(id =request.session['a_id'])

        admin_oldpsw = request.POST['oldpsw']
        admin_newpsw = request.POST['newpsw']
        admin_confirmpwd = request.POST['confirmpsw']

        
        # teacher.password = '007'
        # teacher.save()
        print(admin.password, admin_oldpsw, admin_newpsw, admin_confirmpwd)
        if admin.password == admin_oldpsw:
            if admin_newpsw == admin_confirmpwd:
                admin.password = admin_newpsw
                admin.save()
                msg = "password changed"
            else:
                msg = "password doesnot match"
        else:
            msg ="incorrect password"
    return render (request,'change_psw.html',{'status':msg,'admin':admin})

def logout(request):
    del request.session['a_id']
    request.session.flush()
    return redirect('HEADER:hlogin')