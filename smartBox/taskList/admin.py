from django.contrib import admin
from .models import TaskList

class TaskListAdmin(admin.ModelAdmin):
	pass

admin.site.register(TaskList, TaskListAdmin)