from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from ToDo.forms import TaskModelForm
from ToDo.models import TaskModel


def index(request):
    q = request.GET.get('q')

    if q:
        data = TaskModel.objects.filter(Q(title__icontains=q)).order_by('-id')
    else:
        data = TaskModel.objects.all()

    context = {
        'data': data
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = TaskModelForm()

        context = {
            'form': form

        }

        return render(request, 'form.html', context)


def delete(request):
    data = get_object_or_404(TaskModel)
    data.delete()
    return redirect('/')


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

def edit(request, pk):
    data = get_object_or_404(TaskModel, pk=pk)

    if request.method == 'POST':
        form = TaskModelForm(request.POST, files=request.FILES, instance=data)

        if form.is_valid():
            form.save()

            return redirect('/')
    else:

        form = TaskModelForm(instance=data)

        context = {
            'form': form
        }

        return render(request, 'form.html', context)
