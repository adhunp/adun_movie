from django.urls import path
from .import views

app_name='towner'
urlpatterns=[
    path('clogin',views.clogin,name='clogin'),
    path('csignup',views.csignup,name='csignup'),
    path('eg',views.eg,name='eg'),
    path('addmovies',views.addmovies,name='addmovies'),
    path('towner_home',views.towner_home,name='towner_home'),
    path('cw_psw',views.cw_psw,name='cw_psw'),
    path('de_movies',views.de_movies,name='de_movies'),
    path('delm/<int:mid>',views.del_movie,name='delmovies'),
    path('editm/<int:mid>',views.edit_movies,name='editmovie'),
    path('ahome',views.ahome,name='ahome'),
    path('carter/<int:m_id>',views.carter,name='carter'),
    path('up',views.up,name='up'),
    path('seats/<int:sid>/<int:tid>',views.seats,name='seats'),
    path('booking/<int:table_id>',views.booking,name='booking'),
    path('screen',views.screen,name='screen'),
    path('seats_name',views.seats_name,name='seats_name'),
    path('time_table',views.Time_table,name='time_table'),
    path('action',views.action,name='action'),
    path('seatsrefrence',views.seatsrefrence,name='seatsrefrence'),

]