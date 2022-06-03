from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm

# Create your views here.

def user_login(request):
    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
        user = form.get_user()

        if user:
            messages.success(request, "You logged in succesfully")
            login(request, user)
            return redirect("home")
    return render(request, "users/login.html", {"form" : form})





def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You registered succesfully")
            return redirect("home")

    context = {
        "form" : form
    }

    return render(request, "users/register.html" ,context)






### Önemli: django ya ait func ismi logout oldugundan, bizim farkli bir isim ile view olusturmamiz lazim. Aksi takdirde sonsuz döngüye giriyor.

def user_logout(request):
    # messages.success(request, "You logged out succesfully")
    logout(request)
    # return redirect("home")
    return render(request, "users/logout.html")










# def user_logout(request):
#     messages.success(request, "You logged out")
#     logout(request)
#     return redirect("home")