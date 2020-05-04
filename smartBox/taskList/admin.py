from django.contrib import admin
from .models import TaskList

class TaskAdmin(admin.ModelAdmin):
	pass

admin.site.register(TaskList, TaskAdmin)
