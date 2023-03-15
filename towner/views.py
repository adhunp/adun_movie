from django.shortcuts import render,redirect
from towner.models import Tdetails,Moviedetails,Theater_screen,SeatsName,time_table,Date,Seatdetails,BookingDetails
from django.http import JsonResponse
from datetime import datetime, timedelta


# Create your views here.

def clogin(request):
    if request.method == 'POST':
        tuname = request.POST['username']
        tpassword = request.POST['password'] 

        try:
            clogin = Tdetails.objects.get(tuname=tuname,tpassword=tpassword)
            request.session['c_id'] = clogin.id
            
            return redirect("towner:towner_home")
        except:
            msg = "invalid username or password"
            print('niiuwdhiu ')
            return render(request,"clogin.html",{"error_message":msg})
    return render (request,'clogin.html')

def csignup(request):
    if request.method== 'POST':

        cname = request.POST['townername']
        tname = request.POST['tname']
        tscreen = request.POST['tscreen']
        tad = request.POST['add']
        # tprice = request.POST['tprice']
        tuname = request.POST['tusername']
        temail = request.POST['temail']
        tphone =  request.POST['tnumber']
        tpassword = request.POST['tpassword']
        tgender = request.POST['tgender']
        obj =Tdetails(cname = cname,
                        tname = tname,
                        tscreen = tscreen,
                        taddress = tad,
                        # tprice = tprice,
                        tuname = tuname,
                        temail = temail,
                        tphone = tphone,
                        tpassword = tpassword,
                        tgender = tgender,                   
                    )
        obj.save()
    return render (request,'csignup.html')



def addmovies(request):
    towner= Tdetails.objects.get(id=request.session['c_id'])
    if request.method== 'POST':

        movie_name = request.POST['m_name'] # inputname 
        r_date = request.POST['r_date']
        screen = request.POST['screen']
        # time_am = request.POST['time_am']
        # time_pm = request.POST['time_pm']
        general = request.POST['gender']
        language = request.POST['language']
        # price = request.POST['price']
        details = request.POST['add']
        image = request.FILES['pic']
        t_id =request.session['c_id']
        obj =Moviedetails(movie_name = movie_name,
                         release_date = r_date,
                         movie_screen = screen,
                        #  time_am = time_am,
                        #  time_pm = time_pm,
                         general = general,
                         language = language,
                        #  price = price,
                         details = details,
                         picture = image,
                         theater_id =t_id,
                    )
        obj.save()
        msg = "Movie added succesfuly"
    else:
        msg=""
    return render (request,'add_movies.html',{'customer':towner,'status':msg})



def eg(request):
    return render (request,'eg.html')

def towner_home(request):
    towner= Tdetails.objects.get(id=request.session['c_id'])
    return render (request,'towner_home.html',{'customer':towner})


def cw_psw(request):
    towner= Tdetails.objects.get(id=request.session['c_id'])
    msg = ""
    if request.method == 'POST':
        toldpsw = request.POST['oldpsw']
        tnewpsw = request.POST['newpsw']
        tconfirmpwd = request.POST['confirmpsw']

        towner = Tdetails.objects.get(id =request.session['c_id'])
        if towner.tpassword == toldpsw:
            if tnewpsw == tconfirmpwd:
                towner.tpassword = tnewpsw
                towner.save()
                msg = "password changed"
            else:
                msg = "password doesnot match"
        else:
            msg ="incorrect password"
    return render (request,'towner_chpsw.html',{'status':msg,'customer':towner})


def de_movies(request):
    towner= Tdetails.objects.get(id=request.session['c_id'])
    movie = Moviedetails.objects.all()
    print(movie)
    return render (request,'delete_movies.html',{'movie_details':movie,'customer':towner})

def del_movie(request,mid):
    movie = Moviedetails.objects.get(id = mid)
    movies = Moviedetails.objects.all()
    movie.delete()
    msg='movie deletyed succesfully'
    return render (request,'delete_movies.html',{'movie_details':movies,'status':msg })

def edit_movies(request,mid):
    towner= Tdetails.objects.get(id=request.session['c_id'])
    movie = Moviedetails.objects.get(id=mid)
    msg=''
    if request.method=='POST':
        movie.movie_name = request.POST['m_name']
        movie.release_date = request.POST['r_date']
        movie.movie_screen = request.POST['screen']
        # movie.time_am = request.POST['time_am']
        # movie.time_pm = request.POST['time_pm']
        movie.general = request.POST['gender']
        movie.language = request.POST['language']
        # movie.price = request.POST['price']
        movie.details = request.POST['add']
        # movie.picture = request.FILES['pic']
        movie.save()
        msg='movie edited succesfully'

    return render (request,'towner_edit.html',{'movie_details':movie,'status':msg,'customer':towner})

def img_edit(request,mid):
    towner= Tdetails.objects.get(id=request.session['c_id'])
    movie = Moviedetails.objects.get(id=mid)
    msg=''
    if request.method=='POST':
        movie.picture = request.FILES['pic']
        movie.save()
        msg='movie edited succesfully'

    return render (request,'image_edit.html',{'movie_details':movie,'status':msg,'customer':towner})

def logout(request):
    del request.session['c_id']
    request.session.flush()
    return redirect('towner:clogin')

def ahome(request):
    towner= Tdetails.objects.get(id=request.session['c_id'])
    details=Moviedetails.objects.all()

    Time_table=time_table.objects.all()
    presentday = datetime.now()
    tomorrow = presentday + timedelta(1)
    dayafter = presentday + timedelta(2)
    Todaysdate=presentday.strftime('%d-%m-%Y')
    Tomorrowsdate=tomorrow.strftime('%d-%m-%Y')
    Dayafterdate=dayafter.strftime('%d-%m-%Y')

    Today=Date.objects.get(id=1)
    Today.datees=Todaysdate
    Today.save()

    Tmrw=Date.objects.get(id=2)
    Tmrw.datees=Tomorrowsdate
    Tmrw.save()

    Dayft=Date.objects.get(id=3)
    Dayft.datees=Dayafterdate
    Dayft.save()
  
    return render (request,'movie_home.html',{'det':details,'customer':towner.tuname,'gender':Time_table})
    
def carter(request,m_id):
    details=Moviedetails.objects.get(id=m_id)
    towner= Tdetails.objects.get(id=request.session['c_id'])
    return render (request,'towner_carter.html',{'customer':towner,'movie':details})

def up(request):
    towner= Tdetails.objects.get(id=request.session['c_id'])
    return render (request,'towner_upcoming.html',{'customer':towner})


def seats(request, sid,tid):
    towner= Tdetails.objects.get(id=tid)
    seatsdetails=Seatdetails.objects.filter(screen_id=sid,theater_id=tid)
    print(seatsdetails)
    seatsObj = Theater_screen.objects.get(theater_id=tid,id=sid)
    
    ss=int(seatsObj.seats)
    print(seatsObj.seats)
    
    # bookdetails=SeatInfo.objects.all()

    return render (request,'towner_seats.html',{'customer':towner, 'seatsObj':seatsObj,'seatno':ss,'seatt':seatsdetails })

def booking(request,table_id):
    time_table1= time_table.objects.filter(movie_id=table_id)  
      
    towner= Tdetails.objects.get(id=request.session['c_id'])
    moviedetail = Moviedetails.objects.get(id=table_id)
    print(moviedetail.movie_name)
    return render (request,'towner_booking.html',{'movie':moviedetail,'table':time_table1,'customer':towner})


def screen(request):
    towner= Tdetails.objects.get(id=request.session['c_id'])
    if request.method== 'POST':
        screen = request.POST['screen'] # inputname 
        seats = request.POST['seats']
        t_id =request.session['c_id']

        obj =Theater_screen(screen_name = screen,
                         seats = seats,
                         theater_id =t_id,
                        
                    )
        obj.save()
    return render (request,'towner_screen.html',{'customer':towner})

def seats_name(request):
    details=Theater_screen.objects.all()

    towner= Tdetails.objects.get(id=request.session['c_id'])
    if request.method== 'POST'  :   
        screens = request.POST['screen_name']
        seats = request.POST['seats']
        status='vacant'
    

        scid=int(screens)
        print(scid)
        theaterdetails=Tdetails.objects.get(id=request.session['c_id'])
        obb=Theater_screen.objects.get(id=scid)
        print(obb.id)
        
        obj =Seatdetails(
                         seats = seats,
                         screen_id = obb.id,
                         status=status,
                         theater_id=theaterdetails.id  
                    )
        obj.save()
    return render (request,'towner_seatsname.html',{'customer':towner,'det':details})


def Time_table(request):

    movie= Moviedetails.objects.all()
    details=Theater_screen.objects.all()   
    towner= Tdetails.objects.get(id=request.session['c_id'])
    Dat=Date.objects.all()
    if request.method== 'POST':
        dates = request.POST['date'] # inputname 
        time_one = request.POST['time_one']
        time_two = request.POST['time_two']
        time_three = request.POST['time_three']
        # gender = request.POST['gender']
        # language = request.POST['language']
        t_id =request.session['c_id']
        screens = request.POST['screen_name']
        movies = request.POST['mmid']
        scid=int(screens)
        print(type(scid))
        mid=int(movies)
        oid=int(dates)
        omp=Date.objects.get(id=oid)
        print(type(scid))
        obp=Moviedetails.objects.get(id=mid)
        obb=Theater_screen.objects.get(id=scid)
        print(obb)
        print(obp)
        print(omp)

        obj = time_table(
                         time_one = time_one,
                         time_two = time_two,
                         time_three = time_three,
                        #  gender = gender,
                        #  language = language,
                         screen_id = obb.id,
                         theater_id =t_id,
                         movie_id = obp.id,
                         date_id = omp.id,
                    )
        obj.save()
    return render (request,'time_table.html',{'customer':towner,'det':details,'movie':movie,'date':Dat})



def action(request):
    towner= Tdetails.objects.get(id=request.session['c_id'])
    return render (request,'t_action.html',{'customer':towner})



def seatsrefrence(request, sid):
    towner= Tdetails.objects.get(id=request.session['c_id'])
    seatsdetails=SeatsName.objects.all()
    Time_table= time_table.objects.all()


    seatsObj = Theater_screen.objects.get(theater_id=request.session['c_id'],id=sid)
    ss=int(seatsObj.seats)
    print(seatsObj.seats)

    if request.method== 'POST'  :   
        noofseats = request.POST['count']
        seats = request.POST['seat']
        amount = request.POST['price']
        timetable=request.session['Time_table']
        # price=int(amount)
        # print(type(price))
        # mid=int(price)
        # print(type(price))
        # obb=BookingDetails.objects.get(id=mid)
        # print(obb)
        obj = BookingDetails(
                         noofseats = noofseats,
                         seats = seats,
                         rupes = amount,
                         timetable = timetable,

                    )
        obj.save()


    return render (request,'seatsrefrence.html',{'customer':towner, 'seatsObj':seatsObj,'seatno':ss,'seatt':seatsdetails,'Time_table':Time_table })