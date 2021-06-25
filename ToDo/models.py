from django.db import models


# Create your models here.

class TaskModel(models.Model):
    title = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
