from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.loginpage),
    path('logout/', views.logoutpa),
    path('', views.home,name='home'),
    path('add/', views.addoc),
    path('addp/', views.addpatient),
    path('up/<int:id>', views.up),
    path('del/<int:id>', views.deletee),
    path('doctors/', views.doctors),
    path('patient/', views.patient),
    path('updatep/<int:id>', views.updatepatient),
    path('upa/<int:id>', views.uaddapoint),
    path('delp/<int:id>', views.deletep),
    path('app/', views.addapoint),
    path('showa/', views.sappo),
    path('dela/<int:id>', views.dapp),








   

]