from django.http import HttpResponse
from django.shortcuts import redirect, render
from . models import *
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required





def signup(request):
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            return HttpResponse('password not matching try again')
        else:
            User.objects.create_user(username=name,email=email,password=password1)
            return redirect("success <a href='/home'>Go Back</a>")
    return render(request,'signup.html')

def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        
        elif not username or not password:
            return HttpResponse("Please fill in all the required fields.<a href='/login'>Go Back</a> ")

        else:
            return HttpResponse("username and password dosent match <a href='/login'>Go Back</a> ")
    return render(request,'login.html')


@login_required(login_url="/login")
def logoutpa(request):
    logout(request)
    return redirect('/login')

@login_required(login_url="/login")
def home(request):
    c=Appointment.objects.all()
    appoint=0;    
    for i in c:
        appoint+=1
    return render(request,'home.html',{'a':appoint})

@login_required(login_url="/login")
def doctors(request):
    query = request.GET.get('q')

    if query:
        doctors = Doctor.objects.filter(
            models.Q(name__icontains=query) |
            models.Q(number__icontains=query) |
            models.Q(specialization__icontains=query)
        )
    else:
        doctors = Doctor.objects.all()

    return render(request, 'doctors.html', {'d': doctors, 'query': query})

@login_required(login_url="/login")
def addoc(request):
    if request.method=='POST':
        name=request.POST.get('name')
        num=request.POST.get('number')
        spe=request.POST.get('specialization')
        data=Doctor.objects.create(name=name,number=num,specialization=spe)
        return HttpResponse("<a href='/doctors'> successfully added</a>")

    return render(request,'adddoctor.html')


@login_required(login_url="/login")
def up(request,id):
    new=Doctor.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        num=request.POST.get('number')
        spe=request.POST.get('specialization')
        new.name=name
        new.number=num
        new.specialization=spe
        new.save()
        return redirect('/doctors')
      
    return render(request,'updatedoc.html',{'d':new})

@login_required(login_url="/login")
def deletee(request,id):
    if request.method=='POST':
        data=Doctor.objects.get(id=id)
        data.delete()
        return redirect('/doctors')
        

@login_required(login_url="/login")
def addpatient(request): 
    if request.method=='POST':
        name=request.POST.get('name')
        num=request.POST.get('number')
        add=request.POST.get('address')
        gen=request.POST.get('gender')
        data=Patient.objects.create(name=name,number=num,address=add,gender=gen)
        return HttpResponse("<a href='/patient'> successfully added</a>")
    return render(request,'addpatient.html')

@login_required(login_url="/login")
def patient(request):
    query = request.GET.get('q')

    if query:
        data = Patient.objects.filter(
            models.Q(name__icontains=query) |
            models.Q(number__icontains=query) |
            models.Q(gender__icontains=query) |
            models.Q(address__icontains=query)
        )
    else:
        data=Patient.objects.all()
    return render(request,'patient.html',{'p':data,'query': query})

@login_required(login_url="/login")
def updatepatient(request,id):
    data=Patient.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        num=request.POST.get('number')
        add=request.POST.get('address')
        gen=request.POST.get('gender')
        data.name=name
        data.number=num 
        data.address=add
        data.gender=gen
        data.save()
        return HttpResponse("<a href='/patient'> successfully Update</a>")
  
    return render(request,'updatepatient.html',{'d':data})

@login_required(login_url="/login")
def deletep(request,id):
    if request.method=='POST':
        data=Patient.objects.get(id=id)
        data.delete()
        return redirect('/patient')


@login_required(login_url="/login")
def addapoint(request):
    data1=Doctor.objects.all()
    data2=Patient.objects.all()
    if request.method=='POST':
        do=request.POST.get('doctor')
        p=request.POST.get('patient')
        d=request.POST.get('date')
        t=request.POST.get('time')
        dd=Doctor.objects.get(id=do)
        pp=Patient.objects.get(id=p)

        Appointment.objects.create(doctor=dd,patient=pp,date=d,time=t)
        return HttpResponse("<a href='/showa'>Success</a> ")
    return render(request,'appointment.html',{'d':data1,'p':data2})



@login_required(login_url="/login")
def uaddapoint(request,id):
    data=Appointment.objects.get(id=id)
    data1=Doctor.objects.all()
    data2=Patient.objects.all()
    if request.method=='POST':
        do=request.POST.get('doctor')
        p=request.POST.get('patient')
        d=request.POST.get('date')
        t=request.POST.get('time')
        dd=Doctor.objects.get(id=do)
        pp=Patient.objects.get(id=p)

        data.doctor=dd
        data.patient=pp
        data.date=d
        data.time=t
        data.save()
        return HttpResponse("<a href='/showa'>Success</a> ")
    return render(request,'uappoint.html',{'d':data1,'p':data2,'ii':data})




@login_required(login_url="/login")
def sappo(request):
    data=Appointment.objects.all()
    todaydate=date.today()
    dat=Appointment.objects.filter(date=todaydate)
    dat.delete()
    return render(request,'allappoint.html',{'a':data})

@login_required(login_url="/login")
def dapp(request,id):
    if request.method=='POST':
        data=Appointment.objects.get(id=id)
        data.delete()
        return HttpResponse("<a href='/showa'>Success</a> ")
 
