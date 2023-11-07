from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path("login/", login_user, name ="login"),
    path("logout/", logout_user, name ="logout"),
    path("register/", register_user, name ="register"),
    path("project_view/<int:project_id>", project_view, name ="project_view"),
    
]
