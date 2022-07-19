from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginForms, UserEditForms

def login_user(request):
    if request.user.is_authenticated == True:
        return redirect("heme:heme")

    if request.method == "POST":
        form = LoginForms(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get("username"))
            login(request, user)
            return redirect('heme:heme')
    else:
        form = LoginForms()
    return render(request, "login_app/logo.html", {"form": form})


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


def profile_Edit(request):
    user = request.user
    form = UserEditForms(instance=user)
    if request.method == "POST":
        form = UserEditForms(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
    return render(request, "login_app/Edit_user.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("heme:heme")
