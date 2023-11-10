from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)

class Projects(models.Model):
    PRIORITY_CHOICES = [
        ("", "Select Priority"),
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    ]
    project_id = models.AutoField(primary_key=True)
    user_id = models.ManyToManyField(User, through="ProjectUsers")
    project_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default="")

    def __str__(self):
        return self.project_name


class ProjectUsers(models.Model):
    projectusers_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    project_id = models.ForeignKey(
        Projects, on_delete=models.CASCADE, blank=True, null=True
    )
    is_project_owner = models.BooleanField(default=False)
    user_role = models.CharField(max_length=50)


class Tasks(models.Model):
    PRIORITY_CHOICES = [
        ("", "Select Priority"),
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    ]

    task_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    project_id = models.ForeignKey(
        Projects, on_delete=models.CASCADE, blank=True, null=True
    )
    task_name = models.CharField(max_length=255)
    task_description = models.CharField(max_length=255)
    assignee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assignee"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default="")

    def __str__(self):
        return self.task_name


class RecentActivity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE, blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    project_id = models.ForeignKey(
        Projects, on_delete=models.CASCADE, blank=True, null=True
    )
    activity_type = models.CharField(max_length=255)
    activity_description = models.TextField(max_length=255)
    activity_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.activity_type
