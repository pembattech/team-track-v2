from django import template
from django.contrib.auth.models import User

from ..models import Projects

register = template.Library()


@register.simple_tag
def hello():
    return "hello world"


@register.simple_tag
def list_of_projects(username):
    desired_user = User.objects.get(username=username)
    user_projects = Projects.objects.filter(projectusers__user_id=desired_user)

    return user_projects

