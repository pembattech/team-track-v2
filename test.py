from datetime import date
from django.contrib.auth.models import User
from base.models import Projects, ProjectUsers, Tasks, RecentActivity

# Create a user
user = User.objects.create(username='john_doe', email='john@example.com')

# Create a project
project = Projects.objects.create(
    project_name='Sample Project',
    description='This is a sample project',
    start_date=date(2023, 1, 1),
    end_date=date(2023, 12, 31),
    priority='H'
)

# Associate the user with the project
project_user = ProjectUsers.objects.create(
    user_id=user,
    project_id=project,
    is_project_owner=True,
    user_role='Project Manager'
)

# Create a task
task = Tasks.objects.create(
    user_id=user,
    project_id=project,
    task_name='Sample Task',
    task_description='This is a sample task for the project',
    assignee=user,
    start_date=date(2023, 2, 1),
    end_date=date(2023, 2, 28),
    status='In Progress',
    priority='M'
)

# Create recent activity related to the task
activity = RecentActivity.objects.create(
    task_id=task,
    user_id=user,
    project_id=project,
    activity_type='Task Creation',
    activity_description='Task created for the project',
    activity_date=date(2023, 2, 1)
)
