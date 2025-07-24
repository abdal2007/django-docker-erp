from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from django.core.mail import send_mail
from ERP_project.settings import EMAIL_HOST_USER
import random
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
def VerifyOTP(request):
    if request.method == 'POST':
        userotp = request.POST.get('otp')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        passwor1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if passwor1 == password2:
            form = User(first_name=first_name, last_name=last_name, username=username , email=email, password =passwor1)
            form.save()
        print("OTP",userotp)
    return JsonResponse({'data':'hello'}, status=200)

def SignUpView(request):
    form = CreateUserForm()
    if request.method=='POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        form= CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            otp = random.randint(100000, 999999)
            send_mail("User Data : ", f"verify your Mail by OTP : /n {otp} ", EMAIL_HOST_USER,[email], fail_silently=True)
            messages.success(request, "User saved successfully!")
            return render(request, 'website/verify.html',{'otp':otp, 'first_name': first_name, 'last_name': last_name, 'email':email, 'username':username, 'password1':password1, 'password2':password2})
        else:
            print('Form Error', form.errors)    
            messages.error(request, form.errors)
    context = {'form':form}
    return render(request,'website/signup.html',context)


@csrf_exempt
def VerifyLoginOTP(request):
    if request.method == 'POST':
        userotp = request.POST.get('otp')
        # email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None :
            login(request,user)
            print("login done!")

        print("OTP",userotp)
    return JsonResponse({'data':'hello'}, status=200)

def LoginView(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = User.objects.get(username=username).email

        print("Username: ",username)
        print("password: ",password)
        print("email: ",email)
        user = authenticate(request,username=username, password=password)
        if user is not None:
            otp = random.randint(100000, 999999)
            send_mail("User Data : ", f"verify your Mail by OTP : /n {otp} ", EMAIL_HOST_USER,[email], fail_silently=True)
            messages.success(request, "User saved successfully!")
            return render(request, 'website/verifylogin.html',{'otp':otp, 'username':username, 'password':password})
        #     login(request,user)
        #     print("Login done")
        #     messages.success(request, "Login successfully!")

        #     return redirect('/')
        else:
            print("some error")   
            messages.error(request, "Invalid Entry!") 
        

    context={}
    return render(request,'website/login.html', context)

def LogoutView(request):
    logout(request )
    print('logout successfully')
    messages.success(request, "Logout successfully!")
    return redirect("login")


def ForgetPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print('Email:', email)
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            print('User Exit')
            send_mail("Reset Your Password : ", f"Hey User: {user}! To reset password, click on the given link /n http://127.0.0.1:8000/newpasswordpage/{user}", EMAIL_HOST_USER,[email], fail_silently=True)
            messages.success(request,"User found") 
            return HttpResponse("Password Reset! link sent to your email")

              

        else:
            print("user not exist")  
            messages.error(request,"Email not found")  
        return render(request, 'website/forget_password.html')    
    return render(request, 'website/forget_password.html')    

def NewPasswordPage(request, user):
    userid = User.objects.get(username = user)
    print("userID: ",user)
    if request.method == 'POST':
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 == pass2:
            userid.set_password(pass1)
            userid.save()
            return HttpResponse("Password Reset!")

        print('pass1 and pass2: ', pass1, pass2)

    return render(request, 'website/new_password.html',)