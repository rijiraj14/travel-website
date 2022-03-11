from django.urls import path
from.import views
urlpatterns=[
    path('index2',views.index2,name='index2'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('condata',views.condata,name='condata'),
    path('contable',views.contable,name='contable'),
    path('register',views.register,name='register'),
    path('regi',views.regi,name='regi'),
    path('registration',views.registration,name='registration'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('userin',views.userin,name='userin'),
    path('logout',views.logout,name='logout')

]