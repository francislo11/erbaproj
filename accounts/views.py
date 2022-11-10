from urllib import response
from django.shortcuts import render, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
# from django.core.mail import send_mail
from contacts. models import Contact


def register(request):
    if request.method == 'POST':
        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # check password
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username exited!")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "User email is being used!")
                    return redirect('register')
                else:
                    # everything is fine by now
                    user = User.objects.create_user(username=username,
                                                    password=password,
                                                    email=email,
                                                    first_name=first_name,
                                                    last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered!')
                    return redirect('login')
        else:
            messages.error(request, "Password doesn't match")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # if not match then return None
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logging in !')
            response = redirect('inquiry')
            return response
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request, "You are now logging out !")
        response = redirect('/')
        return response
    else:
        return redirect('login')
