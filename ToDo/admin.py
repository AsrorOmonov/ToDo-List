from django.contrib import admin

# Register your models here.
from ToDo.models import TaskModel


@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'done']
    list_filter = ['title', 'created_at']
