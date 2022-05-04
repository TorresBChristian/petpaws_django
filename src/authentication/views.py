from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from authentication.models import PetPost

def index(request):
    return render(request, 'authentication/base_index.html')

def signin(request):
    if request.method == 'POST':
        user_name = request.POST['email']
        user_password = request.POST['password']
        user_login = authenticate(username=user_name, password=user_password)

        if user_login is not None:
            login(request, user_login)
            messages.success(request, "Logged in sucessfully.")
            return redirect('/index')
        else:
            messages.warning(request, "Wrong username or password. Try again.")

    return render(request, 'authentication/base_signin.html')

def signup(request):
    if request.method == 'POST':
        username=request.POST['email']  # to signin with an email
        password=request.POST['pass1']
        password2=request.POST['pass2']
        email=request.POST['email']
        first_name=request.POST['names']
        if password != password2:
            messages.warning(request, "Passwords are different. Please try again.")
            redirect('signup')
        if User.objects.filter(username=username):
            messages.warning(request, "Email is already registered. Please try another email.")
            redirect('signup')

        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.save()
        messages.success(request, "Account created sucessfully.")
        return redirect('signin')

    return render(request, 'authentication/base_signup.html')

def signout(request):
    logout(request)
    return redirect('index')

def adoptar(request):
    return render(request, 'authentication/adoptar.html')

def dar_en_adopcion(request):
    if request.method == 'POST':
        pet_name = request.POST['name']
        pet_size = request.POST['size']
        pet_age = request.POST['age']
        pet_gender = request.POST['gender']
        post_desc = request.POST['description']
        post_picture = request.POST['picture']
        post_pub = timezone.now()
        owner_name = request.POST['owner_name']
        owner_lastname = request.POST['owner_lastname']
        owner_email = request.POST['owner_email']
        owner_phonenumber = request.POST['owner_phonenumber']

        new_post = PetPost.objects.create_user(pet_name, pet_size, pet_age, pet_gender, post_desc,
                                               post_picture, post_pub, owner_name, owner_lastname,
                                               owner_email, owner_phonenumber)
        new_post.save()
        messages.success(request, "Pet adoption posted sucessfully.")
        return redirect('adoptar')
    return render(request, 'authentication/dar_en_adopcion.html')
