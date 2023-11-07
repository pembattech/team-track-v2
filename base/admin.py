from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Projects)
admin.site.register(ProjectUsers)
admin.site.register(Tasks)
admin.site.register(RecentActivity)

