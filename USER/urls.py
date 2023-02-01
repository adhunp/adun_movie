from django.urls import path
from .import views

app_name='USER'
urlpatterns=[
    path('ulogin',views.ulogin,name='ulogin'),
    path('usignup',views.usignup,name='usignup'),
    path('ahome',views.ahome,name='ahome'),
    path('up',views.up,name='up'),
    path('theater',views.theater,name='theater'),
    path('carter/<int:m_id>',views.carter,name='carter'),
    path('seats',views.seats,name='seats'),
    path('booking/<int:m_id>',views.booking,name='booking'),
    path('cw_psw',views.cw_psw,name='cw_psw'),

]