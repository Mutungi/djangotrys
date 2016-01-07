from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.Home, name='Home'),
     url(r'^commentform/$',views.CommentEntryForm,name='CommentEntryForm'),




    
    url(r'^regista_success/$', views.register_success, name='register_success'),
    url(r'^regista/$', views.Regista, name='Regista'),
   
    url(r'^login/$', views.login, name='login'),
    url(r'^auth/$', views.auth_view, name='auth_view'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^loggedin/$', views.loggedin, name='loggedin'),
    url(r'^invalid/$', views.login, name='invalid_login' ),
     
    



    ]

