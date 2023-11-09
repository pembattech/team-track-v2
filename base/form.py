from django import forms
from .models import Projects


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ["project_name", "description", "start_date", "end_date", "priority"]

        widgets = {
            "project_name": forms.TextInput(attrs={"placeholder": "Enter the project name.", "id": "projectname", "class": "input-style"}),
            "description": forms.Textarea(attrs={"maxlength": "255", "rows": "4", "placeholder": "Enter the project description.", "id": "projectdesc", "class": "input-style"}),
            "start_date": forms.DateInput(attrs={"type": "date", "id": "createprojectStartDate", "class": "input-style"}),
            "end_date": forms.DateInput(attrs={"type": "date", "id": "createprojectEndDate", "class": "input-style"}),
             "priority": forms.Select(attrs={"id": "createpriority", "class": "input-style"})
        }


