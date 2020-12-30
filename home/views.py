from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import redirect

# Create your views here.

def home_page(request):
    #print("about to render home page")
    return render(request, 'home/home-page.html', {})


def navigator(request):
    context_dict = {}
    return render(request, 'home/navigator.html', context_dict)

def handleSignup(request):
    if request.method == 'POST':
        fname = request.POST.get('exampleFirstName')
        lname = request.POST.get('exampleLastName')
        email_id = request.POST.get('exampleInputEmail1')
        pass1 = request.POST.get('exampleInputPassword1')
        pass2 = request.POST.get('exampleInputPassword2')
        print('fname : ', fname)
        print('lname : ', lname)
        print('email id : ', email_id)
        print('pass1 : ', pass1)
        print('pass2 : ', pass2)
        if pass1 == pass2:
            ##create user 
            try:
                user = User.objects.create_user(fname, email = email_id, password = pass1, first_name = fname, last_name = lname)
                messages.add_message(request, messages.INFO, 'Signup completed !! Now you can login with your credentials')
                return render(request, 'home/home-page.html', {})
            except Exception as error:
                print("error is : ", error)
            finally:
                return render(request, 'home/home-page.html', {})
        else:
            messages.add_message(request, messages.INFO, 'Something went wrong.. Please try again...')
            return render(request, 'home/home-page.html', {})
    return render(request, 'home/home-page.html', {})


def handleLogin(request):
    if request.method == 'POST':
        username = request.POST.get('exampleInputEmail1')
        user_password = request.POST.get('exampleInputPassword1')
        user = authenticate(username = username, password = user_password)
        print("user : ", user)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.INFO, 'Login succesfull')
            return render(request, 'home/login-landing.html', {})
    return render(request, 'home/home-page.html', {})   


def handleLogout(request):
    logout(request)
    return redirect('/home')

def admin_page(request):
    print("Group : ", request.group)
    if request.user.is_superuser:
        return render(request, 'home/admin-page.html', {})
    else:
        return redirect('/home')
