from django.urls import path
from .import views
app_name="HEADER"
urlpatterns=[
    path('hlogin',views.hlogin,name='hlogin'),
    path('ahome',views.ahome,name='ahome'),
    path('haction/<str:category>',views.haction,name='haction'),
    path('hlanguage/<str:language>',views.hlanguage,name='hlanguage'),
    path('up',views.up,name='up'),
    path('theater',views.theater,name='theater'),
    path('carter/<int:m_id>',views.carter,name='carter'),
    path('seats/<int:sid>/<int:timeid>',views.seats,name='seats'),
    path('booking/<int:table_id>',views.booking,name='booking'),
    path('payment/<int:bookid>',views.payment,name='payment'),
    path('c_psw',views.c_psw,name='c_psw'),

]