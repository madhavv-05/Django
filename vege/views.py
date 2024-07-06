from django.shortcuts import render, redirect
from.models import Receipe
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q,Sum

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
    
    query=Receipe.objects.all()
    context={'receipes': query}
    return render(request, 'receipe.html', context)

def delete_rec(request,id):
    query=Receipe.objects.get(id=id)
    query.delete()
    return redirect('/receipe')

def update_rec(request,id):
    query=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_des=data.get('receipe_des')
        receipe_img=request.FILES.get('receipe_img')
        query.receipe_name=receipe_name
        query.receipe_des=receipe_des

        if receipe_img:
                query.receipe_img=receipe_img
        
        query.save()
        return redirect('/receipe')

    context={'receipe':query}
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


def get_students(request):
    query=Student.objects.all()
    
    
    if request.GET.get('search'):
        searchs=request.GET.get('search')
        query=query.filter(
            Q(student_name__icontains=searchs)|
            Q(student_email__icontains=searchs)|
          
            Q(student_adress__icontains=searchs)|
            Q(department__department__icontains=searchs)|
            Q(student_id__student_id__icontains=searchs)
            )
    paginator = Paginator(query, 25)  
    page_number = request.GET.get("page",1)
    marks_set=SubjectMarks.objects.all()
    page_obj = paginator.get_page(page_number)
    return render(request, "students.html", {'query':page_obj})


from .seed import *

def see_marks(request, student_id):
    #
    # report_card()
    query=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks=query.aggregate(total_marks=Sum('marks'))
    current_rank=-1
    i=1
    ranks= Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('marks')
    for rank in ranks:
        if student_id==rank.student_id.student_id:
            current_rank=i  
            break
        i=i+1
    return render(request, "see_marks.html", {'query':query,'total_marks':total_marks,'current_rank':current_rank,})