from django import forms

from ToDo.models import TaskModel


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        exclude = ['created_at']
