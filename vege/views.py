from django.shortcuts import render, redirect
from.models import Receipe
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q

@login_required(login_url="/login")
def receipe(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_des = data.get("receipe_des")
        receipe_img = request.FILES.get('receipe_img')
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_des=receipe_des,
            receipe_img=receipe_img,
        )
        return redirect('/receipe')
    
    set=Receipe.objects.all()
    context={'receipes': set}
    return render(request, 'receipe.html', context)

def delete_rec(request,id):
    set=Receipe.objects.get(id=id)
    set.delete()
    return redirect('/receipe')

def update_rec(request,id):
    set=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_des=data.get('receipe_des')
        receipe_img=request.FILES.get('receipe_img')
        set.receipe_name=receipe_name
        set.receipe_des=receipe_des

        if receipe_img:
                set.receipe_img=receipe_img
        
        set.save()
        return redirect('/receipe')

    context={'receipe':set}
    return render(request,'update_rec.html',context)


def login_page(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid username")
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'worng password')
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect('/receipe/')
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get("password")

        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(request,'username aleredy exists')
            return redirect('/register/')
  
        user=User.objects.create(
            username=username
        )
        user.set_password(password)
        user.save()
        return redirect('/register/')

    return render(request,'register.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

okay
def get_students(request):
    set=Student.objects.all()
    
    if request.GET.get('search'):
        searchs=request.GET.get('search')
        set=set.filter(
            Q(student_name__icontains=searchs)|
            Q(student_email__icontains=searchs)|
          
            Q(student_adress__icontains=searchs)|
            Q(department__department__icontains=searchs)|
            Q(student_id__student_id__icontains=searchs)
            )
    paginator = Paginator(set, 25)  
    page_number = request.GET.get("page",1)
    marks_set=SubjectMarks.objects.all()
    page_obj = paginator.get_page(page_number)
    return render(request, "students.html", {'set':page_obj})
