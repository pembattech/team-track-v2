from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path("login/", login_user, name ="login"),
    path("logout/", logout_user, name ="logout"),
    path("register/", register_user, name ="register"),
    path("user/<str:username>", user_profile, name="user_profile"),
    path("upload-profilepic", upload_profile_picture, name="upload_profile_picture"),
    path("project-view/<int:project_id>", project_view, name ="project_view"),
    path("create-project", create_project, name="create_project")
    
]
