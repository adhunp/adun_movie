from django.shortcuts import render,redirect
from USER.models import Userdetails
from django.core.mail import send_mail
from towner.models import Moviedetails

# Create your views here.
def ulogin(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw'] 

        try:
            ulogin = Userdetails.objects.get(username=username,password=password)
            request.session['u_id'] = ulogin.id
            
            return redirect("USER:ahome")
        except:
            msg = "invalid username or password"
            print('niiuwdhiu ')
            return render(request,"ulogin.html",{"error_message":msg})
    return render (request,'ulogin.html')

def usignup(request):
    if request.method== 'POST':
 
        name = request.POST['fullname'] # inputname 
        username = request.POST['username']
        email = request.POST['email']
        phnumber = request.POST['phnumber']
        password = request.POST['password']
        birthday = request.POST['dob']
        gender = request.POST['gender']
        obj =Userdetails(uname = name,
                         username = username,
                         uemail = email,
                         uphone = phnumber,
                         password = password,
                         udob = birthday,
                         ugender = gender,
                    
                    )
        obj.save()
    return render (request,'usignup.html')


def ahome(request):
    details=Moviedetails.objects.all()
    user= Userdetails.objects.get(id=request.session['u_id'])
    return render (request,'user_home.html',{'uname':user.uname,'det':details,})

def up(request):
    user= Userdetails.objects.get(id=request.session['u_id'])
    return render (request,'user_upcoming.html',{'user':user})

def theater(request):
    user= Userdetails.objects.get(id=request.session['u_id'])
    return render (request,'u_theater.html',{'user':user})

def booking(request,m_id):
    details=Moviedetails.objects.get(id=m_id)
    user= Userdetails.objects.get(id=request.session['u_id'])
    return render (request,'user_booking.html',{'user':user,'movie':details})

def carter(request,m_id):
    details=Moviedetails.objects.get(id=m_id)
    user= Userdetails.objects.get(id=request.session['u_id'])
    return render (request,'u_carter.html',{'user':user,'movie':details})


def seats(request):
    user= Userdetails.objects.get(id=request.session['u_id'])
    
    if request.method == 'POST':
        no_seats=request.POST['count']   
        obj1=  Userdetails.objects.get(id = request.session['u_id'])
        email= obj1.uemail
        msg= str(no_seats)+"seats are booked"
        send_mail(
            'no.of seats booked',
               msg ,
            'adhunp8@gmail.com',           
            [email,],
            fail_silently = False,
        )

    return render (request,'u_seats.html',{'user':user})


def cw_psw(request):
    user= Userdetails.objects.get(id=request.session['u_id'])
    msg = ""
    if request.method == 'POST':
        user_oldpsw = request.POST['oldpsw']
        user_newpsw = request.POST['newpsw']
        user_confirmpwd = request.POST['confirmpsw']

        user = Userdetails.objects.get(id =request.session['u_id'])
        # teacher.password = '007'
        # teacher.save()
        if user.password == user_oldpsw:
            if user_newpsw == user_confirmpwd:
                user.password = user_newpsw
                user.save()
                msg = "password changed"
            else:
                msg = "password doesnot match"
        else:
            msg ="incorrect password"
    return render (request,'user_chpsw.html',{'status':msg ,'user':user})


def logout(request):
    del request.session['u_id']
    request.session.flush()
    return redirect('USER:ulogin')