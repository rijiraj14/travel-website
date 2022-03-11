from django.shortcuts import render,redirect
from django.http import HttpResponse
from travelapp. models import *
from . models import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def index2(request):
    data = traveldb.objects.all()
    return render(request,'index2.html', {'data':data})


def contact(request):
    data = traveldb.objects.all()
    return render(request,'contact.html',{'data':data})


def about(request):
    data= traveldb.objects.all()
    return render (request,'about.html',{'data':data})


def condata(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone') 
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = contactdb(name=name,email=email,phone=phone,subject=subject,message=message)
        data.save()
    return redirect('index2')

    
def contable(request):
    data=contactdb.objects.all()
    return render(request,'contable.html',{'data':data})



def register(request):
    return render(request,'register.html')


def regi(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        phonenumber=request.POST.get('phonenumber')
        username=request.POST.get('username')
        password=request.POST.get('password')
        data=registerdb(firstname=firstname,lastname=lastname,phonenumber=phonenumber,username=username,password=password)
        data.save()
    return redirect('index2')
    

def registration(request):
    data=registerdb.objects.all()
    return render(request,'registration.html',{'data':data})


def userlogin(request):
    return render(request,'userlogin.html')

def userin(request):
    if request.method=="POST":
        username_a=request.POST.get('username')
        password_a=request.POST.get('password')
        print(password_a)
        print(username_a)
        if registerdb.objects.filter(username=username_a,password=password_a).exists():
            data=registerdb.objects.filter(username=username_a,password=password_a).values('firstname','lastname','phonenumber','id').first()
            request.session['firstname']=data['firstname']
            request.session['lastname']=data['lastname']
            request.session['phonenumber']=data['phonenumber']
            request.session['username']=username_a
            request.session['password']= password_a
            request.session['id']=data['id']
            return redirect('index2')
        else:
            return render(request,'userlogin.html',{'msg':"sorry... invalid username or password"})
    else:
        return redirect('userlogin')
    
def logout(request):
    del request.session['firstname']
    del request.session['lastname']
    del request.session['phonenumber']
    del request.session['username']
    del request.session['password']
    del request.session['id']
    return redirect('index2')
