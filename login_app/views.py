from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def login_user(request):
    if request.user.is_authenticated == True:
        return redirect("heme:heme")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        login_user = authenticate(request, username=username, password=password)
        if login_user is not None:
            login(request, login_user)
            return redirect("heme:heme")
    return render(request, "login_app/logo.html", {})


def regester(request):
    context = {'errors': []}

    if request.user.is_authenticated == True:
        return redirect("heme:heme")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            context["errors"].append('ERROR Passwords are not the same')
            return render(request, "login_app/redjster.html", context)
        user = User.objects.create(username=username, email=email, password=password1)
        login(request, user)
        return redirect('heme:heme')
    return render(request, "login_app/redjster.html", {})


def logout_user(request):
    logout(request)
    return redirect("heme:heme")
