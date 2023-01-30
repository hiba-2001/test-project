from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from testapp.forms import Stud_Form, user_register, Admin_Form, Mark_Form
from testapp.models import Student_reg, MARK


# Create your views here.
def home(request):
    return render(request,'homepage.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user is not None and user.is_admin:
                return redirect('admin_page')
            elif user is not None and user.is_student:
                return redirect('student_page')
        else:
            messages.info(request, 'invalid credentials')
    return render(request, 'login_page.html')

def student_sign(request):
    u_form = user_register()
    s_form = Stud_Form()
    if request.method=="POST":
        u_form = user_register(request.POST)
        s_form = Stud_Form(request.POST,request.FILES)
        if u_form.is_valid() and s_form.is_valid():
            user = u_form.save(commit=False)
            user.is_student = True
            user.save()
            student = s_form.save(commit=False)
            student.user = user
            student.save()
            messages.info(request, 'student registration successful')
            return redirect('login_page')

    return render(request, 'student_reg.html',{'u_form':u_form,'s_form':s_form})


def admin_sign(request):
    u_form = user_register()
    a_form = Admin_Form()
    if request.method=="POST":
        u_form = user_register(request.POST)
        a_form = Stud_Form(request.POST,request.FILES)
        if u_form.is_valid() and a_form.is_valid():
            user = u_form.save(commit=False)
            user.is_admin = True
            user.save()
            admin = a_form.save(commit=False)
            admin.user = user
            admin.save()
            messages.info(request, 'student registration successful')
            return redirect('login_page')

    return render(request, 'admin_reg.html',{'u_form':u_form,'a_form':a_form})

def admin_page(request):

    return render(request, 'admin_page.html')

def student_page(request):

    return render(request, 'student_page.html')

def student_view(request):
    data=Student_reg.objects.all()
    return render(request, 'view_student.html',{'data':data})



def add_mark(request):
    form= Mark_Form()
    if request.method=='POST':
        form=Mark_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_mark')
    return render(request, 'add_mark.html',{'form':form})

def view_mark(request):
    data=MARK.objects.all()
    return render(request, 'view_mark.html', {'data':data})

def mark_update(request,id):
    m=MARK.objects.get(id=id)
    form=Mark_Form(instance=m)
    if request.method=='POST':
        form=Mark_Form(request.POST,instance=m)
    if form.is_valid():
        form.save()
        return redirect('view_mark')
    return render(request, 'add_mark.html',{'form':form})



def mark_delete(request,id):

        MARK.objects.get(id=id).delete()
        return redirect('view_mark')


def view_stud_mark(request):
    u = Student_reg.objects.get(user=request.user)
    data = MARK.objects.filter(name=u)
    return render(request, 'view_stud_mark.html', {'data':data})


def view_profile(request):
    student=Student_reg.objects.get(user=request.user)
    return render(request, 'view_profile.html', {'student':student})

def update_profile(request):
    pro=Student_reg.objects.get(user=request.user)
    form=Stud_Form(instance=pro)
    if request.method=='POST':
        form=Stud_Form(request.POST,request.FILES,instance=pro)
    if form.is_valid():
        form.save()
        return redirect('view_profile')
    return render(request, 'update_profile.html',{'form':form})

def logout_page(request):
    logout(request)
    return redirect('login_page')