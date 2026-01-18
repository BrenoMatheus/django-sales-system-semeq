from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from customers.models import Customer

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("/")  # redireciona após login

        return render(request, "accounts/login.html", {"error": True})

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("/accounts/login/") 

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )

            # cria o customer vinculado
            Customer.objects.create(
                user=user,
                name=user.username,
                email=user.email
            )

            login(request, user)
            return redirect("/produtos/")
    else:
        # 👇 agora sim o GET também cria form
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})
