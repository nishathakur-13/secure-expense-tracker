from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, plain_password=password)
        return redirect("login")
    return render(request, "register.html")