from django.db import models

class Userdetails(models.Model):
    uname = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    uemail = models.CharField(max_length = 20)
    uphone = models.BigIntegerField()
    password = models.CharField(max_length=30)
    udob = models.CharField(max_length = 20)
    ugender = models.CharField(max_length = 20)
    
    class Meta:
        db_table = 'user_user'

# Create your models here.
