from django.shortcuts import render, redirect
from apps.online_shop_index.models import User
from django.contrib import messages
import bcrypt

def index(request):
    if "user_id" in request.session:
            return redirect('/dashboard')
    return render(request, "online_shop_index/index.html", {})

def login(request):
    if request.method == "POST":
        if "user_id" in request.session:
            messages.error(request, "You are already Logged In")
            return redirect('/login')
        # get the user ID from database/ verify if this user is registered or not
        user_instance = User.objects.filter(email = request.POST['email'])
        # if user is not registered
        if(len(user_instance) == 0):
            messages.error(request, "Email is not registered")
            return redirect('/login')
        if not bcrypt.checkpw(request.POST['password'].encode(), user_instance[0].password.encode()):
            messages.error(request, "password is incorrect")
            return redirect('/login')
        request.session['user_id'] = user_instance[0].id
        return redirect('/')
    return render (request, "online_shop_index/login.html")

def register(request):
    if(request.method == "POST"):
        errors = User.objects.basic_validator(request.POST)
        if(len(errors) > 0):
            for (key,value) in errors.items():
                messages.error(request, value)
            return redirect("/register")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        phone_area_code = request.POST['phone_area_code']
        phone_number = phone_area_code + request.POST['phone_number']
        user = User.objects.create(first_name = first_name, last_name = last_name, password = password, email = email, phone_number = phone_number)
        request.session['user_id'] = user.id
        return redirect('/')
    return render(request, "online_shop_index/register.html", {})

def log_out(request):
    request.session.clear()
    return redirect('/')

def forgot_password(request):
    if request.method == "POST":
        return redirect('/')
    return render(request, "online_shop_index/forgot_password.html", {})



