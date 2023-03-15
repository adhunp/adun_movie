from django.shortcuts import render,redirect
from HEADER.models import Hlogin
from USER.models import Userdetails
from random import randint
from django.core.mail import send_mail
from towner.models import Moviedetails,Tdetails,time_table,Theater_screen,BookingDetails,SeatsName

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

def haction(request,category):
    details=Moviedetails.objects.filter(general=category)
    # language=Moviedetails.objects.filter(language=lan)
    admin= Hlogin.objects.get(id=request.session['a_id'])
    return render (request,'ahome.html',{'admin':admin.username,'det':details,})

def hlanguage(request,language):
    details=Moviedetails.objects.filter(language=language)
    # language=Moviedetails.objects.filter(language=lan)
    admin= Hlogin.objects.get(id=request.session['a_id'])
    return render (request,'ahome.html',{'admin':admin.username,'det':details,})   

def up(request):
    admin= Hlogin.objects.get(id=request.session['a_id'])
    return render (request,'upcoming.html',{'admin':admin})

def theater(request):
    admin= Hlogin.objects.get(id=request.session['a_id'])
    time_table1=time_table.objects.all()

    return render (request,'theater.html',{'admin':admin,'table':time_table1})

def booking(request,table_id):
    moviedetail = Moviedetails.objects.get(id=table_id)
    print(moviedetail.movie_name)

    time_table1= time_table.objects.filter(movie_id=table_id)
    towner= Tdetails.objects.all()

    admin= Hlogin.objects.get(id=request.session['a_id'])
    return render (request,'booking.html',{'admin':admin,'movie':moviedetail,'table':time_table1,'theater':towner})

# def u_booking(request,table_id):
#     time_table1= time_table.objects.filter(movie_id=table_id)
#     user= Userdetails.objects.get(id=request.session['u_id'])   
#     towner= Tdetails.objects.all()
#     moviedetail = Moviedetails.objects.get(id=table_id)
#     print(moviedetail.movie_name)
#     return render (request,'user_booking.html',{'movie':moviedetail,'user':user,'table':time_table1,'theater':towner})

def carter(request,m_id):
    details=Moviedetails.objects.get(id=m_id)
    # theater_details=Tdetails.objects.all()
    admin= Hlogin.objects.get(id=request.session['a_id'])
    return render (request,'carter.html',{'admin':admin,'movie':details})

# def seats(request):
#     admin= Hlogin.objects.get(id=request.session['a_id'])
    
#     if request.method == 'POST':
#         no_seats=request.POST['count']   
#         obj1=  Userdetails.objects.get(id = request.session['c_id'])
#         email= obj1.uemail
#         msg= str(no_seats)+"seats are booked"
        
#         send_mail(
#             'no.of seats booked',
#                msg ,
#             'adhunp8@gmail.com',           
#             [email,],
#             fail_silently = False,
#         )

#     return render (request,'seats.html',{'admin':admin})

def seats(request, sid,timeid):
    admin= Hlogin.objects.get(id=request.session['a_id'])

    bookingdetails=BookingDetails.objects.filter(timetable_id=timeid)
    seat_name=[]
    s_name1=""
    for booking in bookingdetails:
        s_name1 += booking.seats       
       
    s_name2=s_name1[:len(s_name1)-1]

  
    seatsdetails=SeatsName.objects.all()
    Time_table= time_table.objects.all()
    user= Userdetails.objects.get(id=request.session['u_id'])


    seatsObj = Theater_screen.objects.get(theater_id=request.session['c_id'],id=sid)
    
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
        return redirect('HEADER:payment',obj.id)


    return render (request,'seats.html',{'seatsObj':seatsObj,'admin':admin,'seatno':ss,'seatt':seatsdetails,'Time_table':Time_table,'book':bookingdetails,'booked_seat':s_name2})


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

def payment(request,bookid):
    user= Userdetails.objects.get(id=request.session['u_id'])
    bookingdetails=BookingDetails.objects.get(id=bookid)
    return render (request,'user_payment.html',{'user':user,'book':bookingdetails,})