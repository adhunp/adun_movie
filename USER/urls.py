from django.urls import path
from .import views

app_name='USER'
urlpatterns=[
    path('ulogin',views.ulogin,name='ulogin'),
    path('usignup',views.usignup,name='usignup'),
    path('email_exit',views.email_exit,name='email_exit'),
    path('ahome',views.ahome,name='ahome'),
    path('getaction/<str:category>',views.getaction,name='getaction'),
    path('getlanguage/<str:language>',views.getlanguage,name='getlanguage'),
    path('up',views.up,name='up'),
    path('theater',views.theater,name='theater'),
    path('carter/<int:m_id>',views.carter,name='carter'),
    path('user_seats/<int:sid>/<int:timeid>',views.user_seats,name='user_seats'),
    path('u_booking/<int:table_id>',views.u_booking,name='u_booking'),
    path('cw_psw',views.cw_psw,name='cw_psw'),
    path('payment/<int:bookid>',views.payment,name='payment'),
    # path('seats/<int:sid>/<int:tid>',views.seats,name='seats'),
    # path('booking/<int:table_id>',views.booking,name='booking'),

]