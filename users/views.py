from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "that user name is already taken")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "that email is already registered")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        password=password,
                    )
                    # auth.login(request, user)
                    # messages.success(request, "You are now logged in")
                    # return redirect("home")
                    user.save()
                    messages.success(request, "Registered! now you can login")
                    return redirect("login")

        else:
            messages.error(request, "Passwords do not match")
            return redirect("register")

    else:
        return render(request, "users/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "logged in")
            return redirect("contact")
    else:
        return render(request, "users/login.html")


def logout(request):
    return redirect("home")

