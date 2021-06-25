from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView

from ToDo.models import TaskModel


def index(request):
    q = request.GET.get('q')

    if q:
        data = TaskModel.objects.filter(Q(title__icontains=q)).order_by('id')
    else:
        data = TaskModel.objects.all()

    context = {
        'data': data
    }
    return render(request, 'index.html', context)

# class TaskListView(LoginRequiredMixin, ListView):
#     """ data variable - object_list """
#     template_name = 'index.html'
#
#     # model = BookModel
#     # queryset = BookModel.objects.all()
#     # context_object_name = 'book' --> if we want the name of object to be book (not mandatory)
#     def get_queryset(self):
#         q = self.request.GET.get('q')
#         data = TaskModel.objects.order_by('id')
#
#         if q:
#             data = data.filter(Q(title__icontains=q)).order_by('id')
#         else:
#             data = TaskModel.objects.all()
#         return data
