from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from django.contrib.auth.models import User


from .models import Projects, ProjectUsers, Tasks
from .utils import *
from .form import ProfilePictureForm, CreateProjectForm


# Create your views here.
@login_required
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

                return redirect("home")
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
        print(f"Logout successful. User '{username}' has been logged out.")
        return redirect("login")
    else:
        return HttpResponse("No user is currently logged in.")


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            form.save()

            return redirect("login")

    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})

@login_required
def user_profile(request, username):
    return render(request, "profile.html")

@login_required
def upload_profile_picture(request):
    if request.method == "POST":
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            # Redirect or render success page
    else:
        form = ProfilePictureForm()
    return render(request, "upload_profile_picture.html", {"form": form})


def project_view(request, project_id):
    project_queryset = Projects.objects.filter(project_id=project_id)[0]
    task_instances = Tasks.objects.filter(project_id=project_id)
    memberlist_instances = ProjectUsers.objects.filter(project_id=project_id)

    for member in memberlist_instances:
        user = member.user_id.username
        is_owner = member.is_project_owner
        print(user)
        print(is_owner)

    # Retrieve and print all fields
    fields = project_queryset._meta.fields

    for field in fields:
        print(f"{field.name}: {getattr(project_queryset, field.name)}")

    context = {
        "project_id": project_id,
        "project_queryset": project_queryset,
        "project_title": capitalized_string(project_queryset.project_name),
        "task_instances": task_instances,
        "memberlist_instances": memberlist_instances,
    }

    return render(request, "project.html", context)


@login_required
def create_project(request):
    user_projects = Projects.objects.filter(Q(projectusers__user_id__username=request.user.username) & Q(projectusers__is_project_owner = True))
    print(user_projects)

    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = form.save(
                commit=False
            )  # Prevent saving the form before modifying it
            project.save()  # Save the project first to get the project ID

            # Now, create the relationship between the project and the current user
            project_user = ProjectUsers.objects.create(
                user_id=request.user,
                project_id=project,
                is_project_owner=True,
                user_role="Project Owner",
            )

    else:
        form = CreateProjectForm()

    return render(request, "create_project.html", {"form": form, 'created_project_lst': user_projects})
