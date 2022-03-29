from django.contrib import auth,messages
from django.shortcuts import render, redirect
from .models import Employee
from django.contrib.auth.models import User
# Create your views here.

def fn_home(request):
    workers=Employee.objects.all()
    workers_count=workers.count()
    return render(request,'home.html',{'workers_count':workers_count})
def fn_register(request):
    return render(request,'register.html')
def fn_login(request):
    return render(request,'login.html')
def fn_emplist(request):
    emp_list = Employee.objects.all()
    return render(request, 'employeeList.html', {'emp_list': emp_list})
    # return render(request,'employeeList.html')
def fn_view(request,empid):
    emp_obj=Employee.objects.get(id=empid)
    return render(request,'view.html',{'emp':emp_obj})

def fn_add(request):
    if request.method == 'POST':
        EmpName = request.POST.get('txtEmpName')
        # image = request.FILES['img']
        Image = request.FILES.get('img')
        Phone = request.POST.get('txtPhone')
        Address = request.POST.get('txtAdderss')
        Email = request.POST.get('txtEmail')
        Password = request.POST.get('txtPassword')
        emp_obj = Employee(name=EmpName,image=Image,phone=Phone,address=Address,email=Email,password=Password)
        emp_obj.save()
        user = User.objects.create_user(username=Email, first_name=EmpName,
                                        email=Email, password=Password)
        user.save();
        return redirect('/')
    return render(request,'register.html')

# def fn_allemp(request):
#     emp_list = Employee.objects.all()
#     return render(request,'employeeList.html',{'emp_list':emp_list})

def fn_Emplogin(request):
    if request.method == 'POST':
        Username=request.POST.get('txtUsername')
        Password = request.POST.get('txtPassword')
        user = auth.authenticate(username=Username, password=Password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')

def fn_logout(request):
    auth.logout(request)
    return redirect('/')





