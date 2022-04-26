from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'authentication/home.html')

def signin(request):
    if request.method == 'POST':
        user_name = request.POST['email']
        user_password = request.POST['password']
        user_login = authenticate(username=user_name, password=user_password)

        if user_login is not None:
            login(request, user_login)
            messages.success(request, "Logged in sucessfully.")
            return render(request, "authentication/home.html", {'name': user_login.first_name})
        else:
            messages.error(request, "Wrong username or password. Try again.")

    return render(request, 'authentication/signin.html')

def signup(request):
    if request.method == 'POST':
        username=request.POST['email']  # to signin with an email
        password=request.POST['pass1']
        password2=request.POST['pass2']
        email=request.POST['email']
        first_name=request.POST['names']
        if password != password2:
            messages.error(request, "Passwords are different. Please try again.")
            redirect('signin')
        if User.objects.filter(username=username):
            messages.error(request, "Email is already registered. Please try another email.")
            redirect('signin')

        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.save()
        messages.success(request, "Account created sucessfully.")
        return redirect('signin')

    return render(request, 'authentication/signup.html')

def adoptar(request):
    return render(request, 'authentication/adoptar.html')

def da_en_adopcion(request):
    return render(request, 'authentication/daEnAdopcion.html')
