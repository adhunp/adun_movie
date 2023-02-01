from django.db import models


# Create your models here.
class Tdetails(models.Model):
    cname = models.CharField(max_length = 20)
    tname = models.CharField(max_length = 20)
    tscreen = models.CharField(max_length = 20)
    taddress = models.CharField(max_length = 20)
    tprice = models.CharField(max_length = 20)
    tuname = models.CharField(max_length=30)
    temail = models.CharField(max_length = 20)
    tphone = models.BigIntegerField()
    tpassword = models.CharField(max_length=30) 
    tgender = models.CharField(max_length = 20)


class Moviedetails(models.Model):
    movie_name = models.CharField(max_length = 20)
    release_date = models.CharField(max_length = 20)
    movie_screen = models.CharField(max_length = 20)
    time_am = models.CharField(max_length = 20)
    time_pm = models.CharField(max_length = 20)
    price = models.CharField(max_length = 20)
    details = models.CharField(max_length = 20)
    picture = models.ImageField(upload_to = 'movie/' )
    theater = models.ForeignKey(Tdetails,on_delete=models.CASCADE, default= '')


class Theater_screen(models.Model):
    screen_name = models.CharField(max_length = 20)
    seats = models.BigIntegerField()
    theater = models.ForeignKey(Tdetails,on_delete=models.CASCADE, default= '')


class Theater_seats(models.Model):
    screen_id = models.ForeignKey(Theater_screen,on_delete=models.CASCADE)

class Date(models.Model):
    name=models.CharField(max_length = 20)
    datees=models.CharField(max_length = 20)   


class time_table(models.Model):
    date = models.ForeignKey(Date,on_delete=models.CASCADE)
    time_one= models.CharField(max_length = 20)
    time_two= models.CharField(max_length = 20)
    time_three= models.CharField(max_length = 20)
    gender = models.CharField(max_length = 20, default= '')
    language = models.CharField(max_length = 20, default= '')
    theater = models.ForeignKey(Tdetails,on_delete=models.CASCADE)
    screen = models.ForeignKey(Theater_screen,on_delete=models.CASCADE)
    movie = models.ForeignKey(Moviedetails,on_delete=models.CASCADE)

class Towner_seats(models.Model):
    screen = models.ForeignKey(Theater_screen,on_delete=models.CASCADE)
    seats = models.CharField(max_length = 20, default= '')
    status = models.CharField(max_length = 20, default= 'Vacant')
 
class SeatsName(models.Model):
    screen = models.ForeignKey(Theater_screen,on_delete=models.CASCADE)
    seats = models.CharField(max_length = 20, default= '')
    status = models.CharField(max_length = 20, default= 'Vacant')
    theater = models.ForeignKey(Tdetails,on_delete=models.CASCADE)


class SeatsName(models.Model):
    screen = models.ForeignKey(Theater_screen,on_delete=models.CASCADE)
    seats = models.CharField(max_length = 20, default= '')
    status = models.CharField(max_length = 20, default= 'Vacant')
    theater = models.ForeignKey(Tdetails,on_delete=models.CASCADE)

class Seatdetails(models.Model):
    screen = models.ForeignKey(Theater_screen,on_delete=models.CASCADE)
    seats = models.CharField(max_length = 20, default= '')
    status = models.CharField(max_length = 20, default= 'Vacant')
    theater = models.ForeignKey(Tdetails,on_delete=models.CASCADE)    



class SeatInfo(models.Model):
    seat = models.ForeignKey(Seatdetails,on_delete=models.CASCADE,default= '')
    noofseats = models.CharField(max_length = 20)
    rupes = models.CharField(max_length = 20)
    timetable = models.ForeignKey(time_table,on_delete=models.CASCADE)
    customer = models.ForeignKey(Tdetails,on_delete=models.CASCADE, default= '')

class Booking(models.Model):
    seat = models.ForeignKey(Seatdetails,on_delete=models.CASCADE,default= '')
    noofseats = models.CharField(max_length = 20)
    amount = models.CharField(max_length = 20)
    timetable = models.ForeignKey(time_table,on_delete=models.CASCADE)
    customer = models.ForeignKey(Tdetails,on_delete=models.CASCADE, default= '')