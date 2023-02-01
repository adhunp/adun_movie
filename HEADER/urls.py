from django.urls import path
from .import views
app_name="HEADER"
urlpatterns=[
    path('hlogin',views.hlogin,name='hlogin'),
    path('ahome',views.ahome,name='ahome'),
    path('up',views.up,name='up'),
    path('theater',views.theater,name='theater'),
    path('carter/<int:m_id>',views.carter,name='carter'),
    path('seats',views.seats,name='seats'),
    path('booking/<int:m_id>',views.booking,name='booking'),
    path('c_psw',views.c_psw,name='c_psw'),

]