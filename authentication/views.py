from django.shortcuts import render,redirect

from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .emails import send_otp_via_email
from .models import User


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        bio = request.POST.get('bio')
        location = request.POST.get('location')
        password = request.POST.get('password')
        confirm_password = request.POST.get('check_password')
        existing_user = User.objects.filter(email=email).exists()
        
        if not existing_user :
            if password == confirm_password:
                user = User.objects.create(email=email, first_name=first_name, last_name=last_name, mobile_number=mobile_number, bio=bio, location=location)
                user.set_password(password)
                user.save()
                send_mail(
                    'User Registration',
                    (f'Registeration Success\n Password :{password} '),
                    'more.omkar.testing@gmail.com',
                    [email],
                    fail_silently = False
                )
                registration  = True
                return render(request,"authentication/login.html",{
                    "success": registration
                })
                
            else :
                error = True
                return render(request,"authentication/register.html",{
                    "error" : error
                })
        else:
            error = True
            return render(request,"authentication/register.html",{
                    "existing_user" : error
            })

    return render(request,"authentication/register.html")

email = ""
password = ""

def login_user(request):
    if request.method == 'POST':
        global email,password
        email = request.POST.get('email')
        password = request.POST.get('password')
        valid_user = authenticate(email=email, password=password)
        if not valid_user:
            return render(request, "authentication/login.html", {
                        "error" : True
                    })
        send_otp_via_email(email)
        
    return render(request, "authentication/login.html")
                

def otp_verification(request):
    """
        loging in user using otp verification 
    """
    if request.method == 'POST':
        global email,password
        print(email)
        print(password)
        otp_to_verify = request.POST.get('user_otp')
        print(otp_to_verify)
        user = User.objects.filter(email=email).first()
       
        if user.otp == otp_to_verify:
            valid_user = authenticate(email=email, password=password)
            if valid_user:   
                login(request, valid_user)
                
                return redirect('user-profile/dashboard')
            
            else:
               return render(request, "authentication/login.html", {
                        "wrong_otp" : True
                    }) 
    return render(request, "authentication/login.html")

def logout_user(request) :
    """
        logging out using builtin logout function
    """
    logout(request)
    return render(request, "authentication/login.html")