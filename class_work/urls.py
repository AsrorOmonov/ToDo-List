from django.contrib import admin
from django.urls import path

# from ToDo.views import index
# from ToDo.views import TaskListView
from ToDo.views import index, create, delete, edit

app_name = 'index'

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TaskListView.as_view())
    path('', index),
    path('create/', create),
    path('delete/', delete),
    path('edit/<int:pk>/', edit)

]
