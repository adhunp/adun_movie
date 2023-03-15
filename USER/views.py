from django.shortcuts import render,redirect
from USER.models import Userdetails
from django.core.mail import send_mail
from USER.decorators import auth_user
from towner.models import Moviedetails,BookingDetails,Theater_screen,time_table,SeatsName,Tdetails,BookingDetails
from django.http import JsonResponse

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

        email_exist = Userdetails.objects.filter(uemail = email).exists()
        if not email_exist:
            
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

def email_exit(request):
    uemail=request.POST['email']
    email_exit = Userdetails.objects.filter( uemail = uemail).exists()
    return JsonResponse({'status':email_exit})

@auth_user
def ahome(request):
    details=Moviedetails.objects.all()
    user= Userdetails.objects.get(id=request.session['u_id'])
    return render (request,'user_home.html',{'uname':user.uname,'det':details,})

def getaction(request,category):
    details=Moviedetails.objects.filter(general=category)
    # language=Moviedetails.objects.filter(language=lan)
    user= Userdetails.objects.get(id=request.session['u_id'])
    return render (request,'user_home.html',{'uname':user.uname,'det':details,})

def getlanguage(request,language):
    details=Moviedetails.objects.filter(language=language)
    # language=Moviedetails.objects.filter(language=lan)
    user= Userdetails.objects.get(id=request.session['u_id'])
    return render (request,'user_home.html',{'uname':user.uname,'det':details,})    
@auth_user
def up(request):
    user= Userdetails.objects.get(id=request.session['u_id'])
    return render (request,'user_upcoming.html',{'user':user})
@auth_user
def theater(request):
    user= Userdetails.objects.get(id=request.session['u_id'])
    time_table1=time_table.objects.all()
    return render (request,'u_theater.html',{'user':user,'table':time_table1})

# def booking(request,m_id):
#     time_table1= time_table.objects.filter(movie_id=table_id)    
#     user= Userdetails.objects.get(id=request.session['u_id'])
#     moviedatail = Moviedetails.objects.get(id=table_id)
#     print(moviedatail.movie_name)
#     return render (request,'user_booking.html',{'user':user,'movie':moviedatail,'table':time_table1,'theater':towner})
@auth_user
def u_booking(request,table_id):
    time_table1= time_table.objects.filter(movie_id=table_id)
    user= Userdetails.objects.get(id=request.session['u_id'])   
    towner= Tdetails.objects.all()
    moviedetail = Moviedetails.objects.get(id=table_id)
    print(moviedetail.movie_name)
    return render (request,'user_booking.html',{'movie':moviedetail,'user':user,'table':time_table1,'theater':towner})

@auth_user
def carter(request,m_id):
    details=Moviedetails.objects.get(id=m_id)
    user= Userdetails.objects.get(id=request.session['u_id'])
    return render (request,'u_carter.html',{'user':user,'movie':details})

@auth_user
def user_seats(request, sid,timeid):
    bookingdetails=BookingDetails.objects.filter(timetable_id=timeid)
    seat_name=[]
    s_name1=""
    for booking in bookingdetails:
        s_name1 += booking.seats       
       
    s_name2=s_name1[:len(s_name1)-1]

  
    seatsdetails=SeatsName.objects.all()
    Time_table= time_table.objects.all()
    user= Userdetails.objects.get(id=request.session['u_id'])


    seatsObj = Theater_screen.objects.get(id=sid)
    
    ss=int(seatsObj.seats)
    print(seatsObj.seats)


    if request.method== 'POST'  :   
        noofseats = request.POST['count']
        amount = request.POST['price']
        seats = request.POST['seat']
        
        

        timetable=time_table.objects.get(id=timeid)
        # price=int(amount)
        # print(type(price))
        # mid=int(price)
        # print(type(price))
        # obb=BookingDetails.objects.get(id=mid)
        # print(obb)
        obj = BookingDetails(
                         noofseats = noofseats,
                         rupes = amount,
                         seats = seats,
                         timetable_id = timetable.id,

                    )
        obj.save()
        return redirect('USER:payment',obj.id)


    return render (request,'user_seats.html',{'seatsObj':seatsObj,'user':user,'seatno':ss,'seatt':seatsdetails,'Time_table':Time_table,'book':bookingdetails,'booked_seat':s_name2})


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

@auth_user
def payment(request,bookid):
    user= Userdetails.objects.get(id=request.session['u_id'])
    bookingdetails=BookingDetails.objects.get(id=bookid)

    # userid=request.session['u_id']
    # products_orderdata =BookingDetails.objects.filter(user=userid, status='added_to bag')
    # amount = request.POST['price']
    # order_currency = 'INR'
    # order_recepit = 'order_rcptid_11'
    # notes = {'Shipping address' : 'Bommanahali,Banglore'}
    # type(amount)
    # client = razorpay.Client(auth=('rzp_test_jznmHCFBf6ZMUd','hMGwzen13b1QwDmJxDtyAUNy'))
    # payment = client.order.create{{"amount":amount,"currency":order_currency,"receipt":order_receipt,'notes':notes}}
    # return JsonResponse(payment)

    return render (request,'user_payment.html',{'user':user,'book':bookingdetails,})

