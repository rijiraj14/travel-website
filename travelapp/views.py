from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from webtravelapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


def index(request):
    ucount=traveldb.objects.all().count()
    ucount1=contactdb.objects.all().count()
    ucount2=registerdb.objects.all().count()
    return render(request,'index.html',{'count1':ucount,'count2':ucount1,'count3':ucount2})


def add_destination(request):
    return render(request,'add_destination.html')


    
def view_destination(request):
    data=traveldb.objects.all()
    return render(request,'view_destination.html',{'data':data})


def getdata (request):
    if request.method=='POST':
        destination = request.POST.get('destination')
        location = request.POST.get('location')
        image=request.FILES['image']
        price = request.POST.get('price') 
        data = traveldb(destination=destination,location=location,photo=image,price=price)
        data.save()
        return redirect(view_destination)


def edit(request,traid):
        data=traveldb.objects.filter(id=traid)
        return render(request,'edit.html',{'data':data})


def update(request,traid):
    if request.method=='POST':
        des=request.POST.get('destination')
        loc=request.POST.get('location')
        pr=request.POST.get('price')
        try:
            image=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file=traveldb.objects.get(id=traid).photo
        traveldb.objects.filter(id=traid).update(destination=des,location=loc,photo=file,price=pr)
        return redirect('view_destination')


def delete(request,traid):
    data=traveldb.objects.filter(id=traid).delete()
    return redirect('view_destination')


def adminlogin(request):
    return render(request,'login.html')


def adlogin(request):
    username_a = request.POST.get('username')
    password_a = request.POST.get('password')
    if User.objects.filter(username__contains=username_a).exists():
        user = authenticate(username=username_a,password=password_a)
        if user is not None:
            login(request,user)
            print(user)
            return redirect('index')
        else:
            return render(request,'login.html',{'msg':"Sorry... Invalid username or password"})
    else:
        return redirect('adminlogin')

