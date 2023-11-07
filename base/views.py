from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .models import Projects
from .utils import *

# Create your views here.
def index(request):
    content = {"greeting": greeting, "today_date": today_date}
    return render(request, "home.html", content)

def login_user(request):
    print(request)
    if request.method == "POST":
        try:
            fetch_username = request.POST["username"]
            fetch_password = request.POST["password"]

            print(fetch_username, fetch_password)

            user = authenticate(
                request, username=fetch_username, password=fetch_password
            )
            print(user)
            if user is not None:
                login(request, user)

                return HttpResponse("Login successful.")
            else:
                return HttpResponse("Invalid credentials.")
        except Exception as e:
            print(e)
            return HttpResponse("Error occur in login.")
    else:
        return render(request, "registration/login.html")


def logout_user(request):
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        return HttpResponse(f"Logout successful. User '{username}' has been logged out.")
    else:
        return HttpResponse("No user is currently logged in.")

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()

            return redirect('login')
            
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})

def project_view(request, project_id):
    project = Projects.objects.filter(project_id=project_id)

    return render(request, "project.html", {"project": project})
