from django.db import models

# Create your models here.
class Hlogin(models.Model):
    username = models.CharField(max_length = 20) 
    password = models.CharField(max_length = 20)

    class Meta:
        db_table = 'header_login'

class Theater(models.Model):
    theater_name = models.CharField(max_length = 20)   
    movie_name = models.CharField(max_length = 20)   
    time = models.CharField(max_length = 20) 
   

class Showtime(models.Model):   
    movie_name = models.CharField(max_length = 20)   
    time = models.CharField(max_length = 20)        


