from django.contrib import admin
from django.urls import path

# from ToDo.views import index
# from ToDo.views import TaskListView
from ToDo.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TaskListView.as_view())
    path('', index)
]
